Сводный график работы всех версий задачи - https://drive.google.com/file/d/1TIkcs1bTLzZZoblbdB1UoFQcTOGmBfht/view?usp=sharing

Анализ первого варианта алгоритма указывает на линейную зависимость. Алгоритм является эффективным, так как проход массива в 
алгоритме происходит только один раз, а промежуточные результаты сохраняются в словаре, у которого константное время для вставки
и поиска элементов.

Вторая версия алгоритма реализована с помощью двух вложенных циклов. Анализ работы а. указывает на квадратичную асимптотику
O(n^2). Данный вариант является значительно уступает первому варианту начиная с n > 250.

Третий вариант - применение трех вложенных циклов - неприемлемый алгоритм. Анадиз указывает на кубическую асимптотику O(n^3)
Рост функции очень стремителен и замедление работы наблюдается уже при n > 50.

Во 2-х крайних случаях cProfile указывает, что слабое место кода, является сам способ реализации решения задачи.

График наглядно указывает скороть изменения времени от количества входных данных. 