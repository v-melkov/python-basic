sample_dictionary = {'name': 'Otus', 'site':'otus.ru'}

try:
    print(sample_dictionary['site'])
except BaseException as ex:
    print(f'{ex} does not exist')