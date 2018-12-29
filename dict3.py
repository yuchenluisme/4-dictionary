d={}
d['names']=['ali','bety']
#d.get('name')
#['ali', 'bety']

#item中每个元素都是一个key，一个value
d={'title':'python','url':'yuchenlu'}
d.items()
#dict_items([('title', 'python'), ('url', 'yuchenlu')])

#popd={'x':1,'y':2}
d.pop('x')
1
#listpop弹出最后一个元素，listitem弹出随机的

#更新Update d={'key':'value'}
d={'title':'p','url':'org'}
x={'name':'ij'}
d.update(x)
#{'title': 'p', 'url': 'org', 'name': 'ij'}

d={}
d[0]=1
d[1]=12
#d
#{0: 1, 1: 12}