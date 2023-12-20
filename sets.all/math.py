s1={10,20,30,10,20}
s2={60,20,30,40,10,50}
a={10,20,30,40,50}
b={60,70,30,10,20}
x = {"pavan","venkat","abhi","amar","kiran","rayudu"}
y={"kishore","pavan","abhi"}

s1=s2.copy()
print(s1)

c=a.union(b)
print(c)

z=x.difference(y)
print(z)

d=a.intersection(b)
print(d)