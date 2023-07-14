# implicitas: las hace Python automáticamente
print("IMPLICITAS")
num1 = 20
num2 = 20.5

print(type(num1))
print(type(num2))

num1 = num2 + num1
print(type(num1))

# explícita: la hacemos nosotros
print("\nEXPLÍCITAS")
num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3) # casting

print(type(num4))
print(num4)

edad = input("Dime tu edad: ")
edad = int(edad)
nueva_edad = edad + 1
print(nueva_edad)