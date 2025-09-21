#operasi logika
# NOT
a = False
c = not a
print('data a =',a)
print('data c =',c)
# OR (JIKA SALAH SATU TRUE, MAKA HASILNYA TRUE)
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)
# AND(Jika dua buah nilai true,maka akan true)
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)
#XOR (akan true jika salah satu true)
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
