# TODO Напишите функцию find_common_participants
def get_unique_words(a, b):
    c = a.split('|')
    v = b.split('|')
    x = list(set(c).intersection(v))
    x.sort()
    return x

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(get_unique_words(participants_second_group, participants_first_group))

# TODO Провеьте работу функции с разделителем отличным от запятой
