'''import sys
from collections import OrderedDict
with open('sample_file.txt', mode = 'w+') as spell_file:
    spell_file.write('Assalamu aleikum')
    spell_file.seek(0)
    print(spell_file.read())
print(sys.getdefaultencoding())
print(ord('A'))
s = 'hello'
enc_ascii = s.encode('ascii')
print("enc_ascii")
dict_1 = {
    'Someone_1' : 789,
    'Someone_2' : 45664
    }
print(type(dict_1))
dict_2 = OrderedDict()
dict_2['a'] = 'F'
dict_2['b'] = 'G'
print(type(dict_2))
person = ("a", "b", "c", "d",)
print(type(person))
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(type(mySet))
myLiest = [1, 2, 3, 5 , 3, 9, 1]
mySet = set(myLiest)
print(mySet)
mySet2 = {1,2,3,6,4}
print(mySet.issubset(mySet2))'''
numbers = [1, 2, 3, 4, 6, 7, 8, 9]
for i, item in enumerate(numbers):
    numbers = item ** i
    print(numbers)
