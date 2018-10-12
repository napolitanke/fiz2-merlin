# Fiz 2 - zadatak sa utezima (m1, m2. m2 se otkvaci)
# - Trazi se amplituda

print("Sa spacevima unesite redom: m2 k")
print("primjer: 10 8")

line = input(">>>")

arr = line.split()

if(len(arr) != 2):
    print("Unesi 2 varijable!")
    exit()

m2 = float(arr[0])
k = float(arr[1])

print("Amax = ", m2*9.81/k)
