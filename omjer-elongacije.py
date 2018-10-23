## Zadatak "razmotrite sustav... omjer elongacije A(T/2)/A(0)

e=2.7182818284590
pi=3.14159265359

print("Unesi redom, sa razmacima: ")
print("m k b")
print("primjer: >>> 1200 84000 8100")

lista = input("")
pri = lista.split()
m = int(pri[0])
k = int(pri[1])
b = int(pri[2])

w = (k/m - b**2/(4*m**2))**(1/2)
T = 2*pi/w
x = e**((-b*T)/(4*m))

print(x)
