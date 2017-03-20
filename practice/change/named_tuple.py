from collections import namedtuple

namedtuple('PersonEntry', ['phone', 'address'])
PersonEntry = namedtuple('PersonEntry', ['phone', 'address'])
z = PersonEntry('David', '503-555-9999')

x = ('David', '503-555-9999')
y = 1234