class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list = iter([])  # Создаём итератор
        self.count_list = 0  # Счётчик списков
        return self

    def __next__(self):
        try:
            item = next(self.list)  # Тащим значение из списка
        except StopIteration:  # Если текущий список кончился:
            if self.count_list == len(self.list_of_list):  # И списки тоже закончились
                raise StopIteration  # То всё
            self.list = iter(self.list_of_list[self.count_list])  # Иначе переходим на следующий список
            self.count_list += 1  # и прибавляем счётчик
            item = next(self.list)  # Тащим значение из списка
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

print('Тест итератора завершён')


# if __name__ == '__main__':
#     test_1()
