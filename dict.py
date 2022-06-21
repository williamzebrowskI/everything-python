dict = {'hello': 1, 'there': 2, 'how': 3}

#print(dict)

del dict['how']
#print(dict)

dict['whoa'] = 2
#print(dict)

x = {v * 2 for k, v in dict}
print(x)