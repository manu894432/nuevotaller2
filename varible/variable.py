# variables.py
# Programa que evalúa una expresión matemática con operadores y paréntesis

# Pedir valores al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
d = float(input("Ingrese el cuarto número: "))
e = float(input("Ingrese el quinto número: "))

# Fórmula: ((a + b) * c) / (d + (e - a))
resultado = ((a + b) * c) / (d + (e - a))

# Mostrar el resultado
print("El resultado de la expresión es:", resultado)

