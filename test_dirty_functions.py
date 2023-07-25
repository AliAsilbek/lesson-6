import os

from dirty_functions import random_famous

famous = ('max', 'leo', 'kate')


def test_random_famous():
    # кол возвращаемых элементов списка
    assert len(random_famous(famous, 2)) == 2
    # вернувшиеся элементы входят в состав списка
    for i in random_famous(famous, 2):
        assert i in famous

    # for i in random_famous(famous, 2):
    #     assert isinstance(i, str)

    # for i in random_famous(({'ali':20}, {'leo': 30}, {'saphia': 20}), 2):
    #     assert isinstance(i, str)
    result = []
    for i in range(800):
        person = random_famous(famous,1)[0]
        result.append(person)

    assert len(set(result)) >1



def test_mkdir():
    """Тест функции с побочным эффектом"""
    os.mkdir('folder')
    # папка есть на диске
    assert 'folder' in os.listdir()
    os.rmdir('folder')