a = 1234
b = 10.1
c = "a의 변수 값은 %d이고 b는 %.1lf" % (a, b)
print(c)  

d = "b의 변수 값은 {1}이고 a는{0}". format(a,b)
print(d)

e = "{: ^30}". format("안녕")
print(e)