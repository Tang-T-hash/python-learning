a = 100
b = 200
c = 300

d = a
a = c
c = b
b = d
print(a, b, c)
print(type(a), type('hello'), type(True), type(False),type(None))

num = 123

print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,bool))