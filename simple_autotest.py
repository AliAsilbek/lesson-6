from main import *
'''
 test which uses assets
'''

hello_to('max')

# assert 2>1
# assert 4>1
# assert 3>1
# assert 1==1
#
# # here would be a mistake
# assert 1>90, 'Text which appears when there is an error'
# print('это не выполнится')
assert hello_to(1) == 'Hello, 1', hello_to(1)
assert salary(2,2) == 12
assert salary(1,2) == 6
