from collections import defaultdict, Counter

'''
5, 5, 4, 7, 8, 9, 5, 6, 3, 1, 2, 2, 4, 8, 6, 4, 5, 9, 9, 2, 1, 0
10, 30, 1, 5

Написати функцію, яка буде рахувати кількість появи кожного числа які вона 
виведе найчастіше число у термінал
'''

# 1. Прочитати рядки с файла 

#'3, 1, 2, 2, 4, 8, 6, 4\n'

def read_lines_from_file(file_path: str) -> list[str]:
    with open(file_path, encoding= 'utf-8') as file:
        return file.readlines()
    
#print(read_lines_from_file('./folder/counter.txt')) # начинает искать в папке 2025-03-22, поэтому указать путь/папку в которой искать

# 2. З цього рядка дістати окремі числа

'''
my_str = '3, 1, 2, 2, 4, 8, 6, 4\n'.strip()
print(my_str.split(', '))

[3, 1, 2, 2, 4, 8, 6, 4]

'''

def conver_file_line_to_numbers_list(line: str) -> list[int]:
    numbers_list = []
    numbers_str_list = line.strip().split(', ')
    for number_str in numbers_str_list:
        numbers_list.append(int(number_str))
    return numbers_list
#print(conver_file_line_to_numbers_list('3, 1, 2, 2, 4, 8, 6, 4\n'))


#[3, 1, 2, 2, 4, 8, 6, 4]

# 3 -> 1, 1 -> 1, 2 -> 2, 4-> 2, 8 -> 1, 6 -> 1
# {3:1, 1: 1}

# 3. Потрібно пройтися по числам та порахувати повторення кожного

def calculate_statistics(element_list: list[int]) -> dict[int, int]:
    statistics_dict = {}
    for element in element_list:
        # зустрічаємо єлемент 1 раз
        if element not in statistics_dict:
            # Створити новий ключ та задати значення як 1
            statistics_dict[element] = 1
        # Зустрічаемо елемент не вперше count+1
        else:
            # Прочитати попередне значення та збільшити його на 1
            statistics_dict[element] +=1     
    return statistics_dict

# более упрощенная версия

def calculate_statistics_default_dict(element_list: list[int]) -> dict[int, int]:
    statistics_dict = defaultdict(int)
    for element in element_list:
            statistics_dict[element] +=1     
    return statistics_dict

def calculate_statistics_counter(element_list: list[int]) -> Counter:
    return Counter (element_list)

#print(Counter)

#print(calculate_statistics_default_dict([3, 1, 2, 2, 4, 8, 6, 4]))


def main():
    file_path = './folder/counter.txt'
    lines = read_lines_from_file(file_path) 
    numbers_list = []
    for line in lines:
        numbers_list.extend(conver_file_line_to_numbers_list(line))
    print(calculate_statistics_counter(numbers_list))

main()

#my_list = [1, 2, 3, 4]
#print(9 in my_list) #False

#my_dict = {'a' : 1, 'b' : 2}
#print(b in my_dict) #False

#my_dict = {}

#my_defaultdict = defaultdict(int)
#print(my_defaultdict)

#my_defaultdict[10] += 1
#print(my_defaultdict)

#my_defaultdict = defaultdict(list)
#print(my_defaultdict)

#my_defaultdict[10].append('s')
#print(my_defaultdict)