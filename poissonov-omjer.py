# Zadatak sa istezanjem, iz fiz 2
# Sipka se istegnula X%, volumen se promjenio Y%
# Trazi se poissonov omjer

print("Unesi redom (odvojeno spacevima):")
print("Promjena duljine u postocima, promjena volumena u postocima")
print("primjer: 5 3 [to je za 5% i 3%]")

line = input(">>>")

arr = line.split()

dL = float(arr[0])/100
dV = float(arr[1])/100

dR = (dV - dL)/2

v = -dR/dL

print("Poissonov omjer : ", v)
