from calculator import sumar, restar, multiplicar, dividir

print("Calculadora")

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    print("Resultado:", sumar(a, b))
elif opcion == "2":
    print("Resultado:", restar(a, b))
elif opcion == "3":
    print("Resultado:", multiplicar(a, b))
elif opcion == "4":
    print("Resultado:", dividir(a, b))
else:
    print("Opción inválida")