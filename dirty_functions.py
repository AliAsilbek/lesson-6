import random
import os
def random_famous(famous, count=2):
    '''
    недетерминированная функция
    :param famous:
    :param count:
    :return:
    '''
    return random.sample(famous, count)


def create_folder(name):
    os.mkdir(name)