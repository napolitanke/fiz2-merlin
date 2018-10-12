# Astronaut iz fiz 2

print("Sa spacevima unesite redom: T0 T K")
print("primjer: 0.90149 2.21283 605.6")

line = input(">>>")

arr = line.split()

if(len(arr) != 3):
    print("Unesi 3 varijable!")
    exit()

T0 = float(arr[0])
T = float(arr[1])
k = float(arr[2])

m0 = T0*T0*k/((2*3.141592)**2)
m = T*T*k/((2*3.141592)**2)

print("Masa astronauta je = ", m-m0)
