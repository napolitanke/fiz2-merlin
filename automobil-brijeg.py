#Zadatak 3.1 - Automobil mase...

print("Unesi redom (odvojeno razmacima):")
print("m(automobil) br.ljudi m(covjek) l(brijeg) v(maxA u km/h)")
line = input("")
lista = line.split(" ")

masaAuta = float(lista[0])
brOsoba = int(lista[1])
masaOsobe = float(lista[2])
lBrijeg = float(lista[3])
brzina = float(lista[4])/3.6

pi = 3.14159265359

print((masaOsobe * 9.81 * lBrijeg**2)/((masaAuta+brOsoba*masaOsobe)*pi**2*brzina**2) * 100)
