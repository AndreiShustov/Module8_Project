# Практика "Исключения"
#
# В этом уроке будет рассмотрен реальный пример использования блоков try и except для обработки ошибок и
# исключительных ситуаций.
# В качестве примера будет использован текстовый файл под названием «data.txt», содержащий примерно 10 строк.
# Каждая строка будет состоять из трех элементов: сначала идет какое-то число, затем через пробел указана
# арифметическая операция (например, целочисленное деление), и после этого — второе число.
# Задача заключается в том, чтобы считать каждую строку из текстового файла и вывести результат
# арифметического выражения на консоль
# При работе с данными могут возникать ситуации, когда они оказываются некорректными.
# Например, одной из таких ситуаций является префиксная запись, при которой математический операнд располагается перед
# числами. В этом случае данные будут считаться некорректными, так как первое число будет записываться в
# первую переменную, второй операнд — во вторую, а третья переменная должна содержать второе число.
# Еще одной распространенной исключительной ситуацией является недостаток данных, например,
# отсутствие второго числа или математического операнда. Это также считается некорректными данными.
# Чтобы избежать остановки программы при возникновении таких ошибок, целесообразно использовать обработку исключений.
# Вместо того чтобы просто выводить ошибку, можно перехватывать возникающие исключения, выводить информацию о строке,
# в которой произошла ошибка, и сообщать об этом пользователю.

def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        print(f'Результат:  {operand_1 + operand_2}')
    if operation == '-':
        print(f'Результат:  {operand_1 - operand_2}')
    if operation == '/':
        print(f'Результат:  {operand_1 / operand_2}')
    if operation == '//':
        print(f'Результат:  {operand_1 // operand_2}')
    if operation == '%':
        print(f'Результат:  {operand_1 % operand_2}')
    if operation == '*':
        print(f'Результат:  {operand_1 * operand_2}')

cnt = 0

with open('data.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в линии {cnt}, не хватает данных для ответа')
            else:
                print(f'Ошибка в линии {cnt}, нельзя перевести в число')





