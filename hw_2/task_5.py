# https://drive.google.com/file/d/1ZjrvyLAf32wFuO0kuRHnriHYgN-6VopM/view?usp=sharing

# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def task_5(table='', pos=32):
    if pos > 127:
        return table

    if table != '':
        end_ch = '\n' if not (pos - 1) % 10 else ' '
    else:
        end_ch = ''
    new_table = f'{table}{end_ch}{pos:>3d} - {chr(pos)}'
    return task_5(new_table, pos + 1)


table = task_5()
print(table)
