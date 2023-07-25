def hello_to(name='ali'):
    return f'Hello, {name}'


def salary(hours, salary_by_hour):
    """
    расчет зп сотрудника
    :param hours:
    :param salary_by_hour:
    :return:
    """
    k=3
    return hours*salary_by_hour*k
