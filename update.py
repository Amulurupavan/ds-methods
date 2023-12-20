a=[]
l=[10,20,30,40]
l[0]=12.5
l[2]=10.5
#after updating.
print(l)

a=["pavan","venkat","abhi","amar","ganesh","nani"]
b=["kishal","kishore","megan"]
a.extend(b)
print(a)

a=["pavan","venkat","abhi","amar","ganesh","nani"]
b=["kishore","megan","sai"]
c=["siva"]
a.append(b)
a.append(c)
print(a)

a=["pavan","venkat","abhi","amar","ganesh","nani"]
a.insert(2,"kishore")
print(a)

l1=[10,20,30,40]
l1.reverse()
print(l1)

l1=[40, 30, 20, 10]
l1.sort()
print(l1)

l1=[40,30,20,10]
l2=[50,60,70,10]
l3=l2.copy()
print(l1)
print(l2)
print(l3)