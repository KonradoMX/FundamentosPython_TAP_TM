def nuevoTema(tema):
    print("\n==========", tema, "=========\n")

#Este es un comentario de una línea
nuevoTema("Operadores aritméticos")
print("Operador división entera (10 // 3): ", 10 // 3)
print("Operador potencia (5 ** 3): ", 5 ** 3) #Operador **

''' Este es un
comentario de
varias líneas '''
nuevoTema("Operadores lógicos")
print("Operador and (True and False): ", True and False)
#Actividad: Imprimir la tabla de verdad de los operadores lógicos.

nuevoTema("Operadores de comparación")
print("2 == 3", 2 == 3)
#Actividad: Agregar los demás operadores de comparación.

nuevoTema("Variables")
variable1 = 10
_variable2 = 6.2456
Variable3 = "Juancho"
dosPalabras = "Hola"
dos_palabras = "Hello"

print(variable1, _variable2, Variable3, dosPalabras, dos_palabras)

a, b, c = 10, 5.16, "Palabra"
print(a, b, c)

nuevoTema("Enteros")
w = 105
x = 9898259827985732
y = -256
z = 0b00110011
h = 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Flotanes")
x = 1297.50
print(x, type(x))
y = 0.5637939
print(y, type(y))

nuevoTema("Números complejos")
x = -46j
y = 12 + 45j
z = 2j
print(x, type(x))
print(y, type(y))
print(z, type(z))

nuevoTema("Booleanos")
lis = [8]
print(lis, "es", bool(lis))
t = ()
print(t, "es", bool(t))
new = "Hello"
print(new, "es", bool(new))
num = 99
print(num, "es", bool(num))
comp = 1 + 0j
print(comp, "es", bool(comp))
val = None  #None equivale a Null
print(val, "es", bool(val))

nuevoTema("Listas") #No son arreglos.
a = [10, 20.5, "Python list"]
print(a)
print(a[1])
a[0] = "Hola"
print(a)

nuevoTema("Tuplas")
t = (25, "Tupla", 1 + 10j, 3.1416)
print(t)
print(t[2])
print("t[1:4]:", t[1:4])
#t[1] = 34 Operación no válida en tuplas.

nuevoTema("Conjuntos")
t = {50, 20, 30, 40, 10, 50}
print("Conjunto t=", t, type(t))

nuevoTema("Diccionario")
d = {1:"Valor1", "Valor2":2j}
print(d, type(d))
print("d[Valor2]:", d["Valor2"])

nuevoTema("Cadenas")
cadena1 = "Cadena con comillas dobles"
cadena2 = 'Cadena con comillas simples'

print(cadena1, type(cadena1))
print(cadena2, type(cadena2))

cadenaMultilinea = '''Esta es una cadena
de varias lineas    con     tabulares   y
            saltos
de
linea'''

print(cadenaMultilinea)
print("Segmentación de cadenas")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1 = "Hola"
cadena4 = (cadena1 + " ") * 5
print(cadena4)
cadena4 = cadena4.upper()
print(cadena4)
