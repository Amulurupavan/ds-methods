emp={
    'id':101,
    'ename':"pavan",
    'sal':45000,
    'loc':['banglore','tirupati','chennai']
}

print(emp.get('loc')[1])
print(emp.get('sal'))
print(emp.get('ename'))
print(emp.get('id'))

print(emp.items)
for key,values in emp.items():
    print(key, ':', values)