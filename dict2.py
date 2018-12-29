#
phonebook={'zhang':'123','li':'234'}
"zhang's phone number is {zhang}".format_map(phonebook)
"zhang's phone number is 123"

#生复制和shallow copy浅复制
x={'username':'admin','machines':['a','b','c']}
y=x.copy()
y
{'username': 'admin', 'machines': ['a', 'b', 'c']}
x
{'username': 'admin', 'machines': ['a', 'b', 'c']}
y['username']='mlh'
y
{'username': 'mlh', 'machines': ['a', 'b', 'c']}
x
{'username': 'admin', 'machines': ['a', 'b', 'c']}

#
from copy import deepcopy
d={}
d['names']=['kity','loren']
#d
#{'names': ['kity', 'loren']}
c=d.copy()
e=deepcopy(d)
d['names'].append('clive')
#c
#{'names': ['kity', 'loren', 'clive']}
#d
#{'names': ['kity', 'loren', 'clive']}
#e
#{'names': ['kity', 'loren']}