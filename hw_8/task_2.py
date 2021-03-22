# Закодируйте любую строку по алгоритму Хаффмана.

from collections import deque
from collections import Counter
import hashlib


class Node:
    def __init__(self, char=None, cost=0, left=None, right=None):
        self.char = char
        self.cost = cost
        self.left = left
        self.right = right


class Archiver:

    def __init__(self):
        self._chars_codes = {}
        self._codes_chars = {}

        # используем для проверки соответствия таблиц с текстом, который необходимо раскодировать
        self._last_encoded_hash = 0

    def _save_data_hash(self, data):
        """
        Сохраняем хэш исходной строки
        :param data: str
        :return: None
        """
        self._last_encoded_hash = hashlib.md5(data.encode()).hexdigest()

    def archive(self, data: str) -> str:
        chars = sorted(Counter(data).items(), key=lambda pair: pair[1])
        items = deque()

        for item, cost in chars:
            items.append(Node(item, cost))

        while len(items) > 1:
            item_1 = items.popleft()
            item_2 = items.popleft()
            cost_sum = item_1.cost + item_2.cost

            # создается пустой дочерний узел, к которому будут соединены листья, извлеченные из очереди
            parent = Node()

            # соединаем с пустым родителем
            parent.left = item_1
            parent.right = item_2
            parent.cost = cost_sum

            # ищем позицию нового элемента, исходя из его цены (cost)
            idx = 0
            while idx < len(items):
                if items[idx].cost >= cost_sum:
                    break
                idx += 1
            items.insert(idx, parent)

        # метод для обхода графа в глубину
        def _depth_search(node, ch_code, code_ch, code=''):
            if node.char:
                ch_code[node.char] = code
                code_ch[code] = node.char
            if node.left is not None:
                _depth_search(node.left, ch_code, code_ch, f'{code}0')
            if node.right is not None:
                _depth_search(node.right, ch_code, code_ch, f'{code}1')

        _depth_search(items.pop(), self._chars_codes, self._codes_chars)

        self._save_data_hash(data)

        # кодирум исходную строку
        output = []
        for ch in data:
            output.append(self._chars_codes[ch])

        return ''.join(output)

    def unarchive(self, archive):

        decoded_chars = []
        position = 0
        code_length = 2

        while position < len(archive):
            coded_char = archive[position:code_length + position]
            decoded_char = self._codes_chars.get(coded_char)

            if decoded_char:
                decoded_chars.append(decoded_char)
                position = code_length + position
                code_length = 2
            else:
                code_length += 1

        unzipped = ''.join(decoded_chars)

        assert self._last_encoded_hash == hashlib.md5(
            unzipped.encode()).hexdigest(), 'Таблицы декодирования не соответствую для раскадированния данного теста'
        return unzipped


if __name__ == "__main__":
    archiver = Archiver()
    text = 'beep boop beer!'
    print(archiver.archive(text))

    test_cases = ['Lorem ipsum dolor sit amet',
                  'consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.',
                  'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam '
                  'felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.',
                  'Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, '
                  'imperdiet a, venenatis vitae, justo.']

    for text_case in test_cases:
        assert text == archiver.unarchive(
            archiver.archive(text)), 'Ошибка! Не соответствие текстов после архивации и разархивации'
    print('Tests OK')
