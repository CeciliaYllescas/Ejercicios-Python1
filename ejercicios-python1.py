'''1) Escribe un programa muestre por pantalla “Hello World”.

print ('Hello World')
'''

'''2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.

suma = 3 + 5
print (suma)
'''

'''3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”

def saludo(nombre):
    return f'¡Hola {nombre}!'

nombre=input('Escriba su nombre ')
print (saludo(nombre)) 
'''


'''4) Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.

n1= int(input('Ingrese un número '))
n2= int(input('Ingrese otro numero '))
suma= n1 + n2

print (f'La suma de los numeros dados es {suma}')
'''

'''5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.

def numero_mayor (num1, num2):

    if num1>num2:
        mayor=num1
    elif num2>num1:
        mayor=num2
    else: #num1 == num2
        raise Exception ('Los números ingresados no pueden ser iguales')
    return mayor

num1=int(input('Ingrese un número '))
num2=int(input('Ingrese otro número '))
print (f'El número mayor de los ingresados es {numero_mayor(num1, num2)}')
'''

'''6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.

def mayor_de_tres (n1, n2, n3):
    if n1>n2 and n1>n3:
        resultado=n1
    elif n2>n1 and n2>n3:
        resultado= n2
    elif n3>n1 and n3>n2:
        resultado=n3
    else: #n1==n2==n3
        raise Exception ('Los número ingresados no deben ser iguales')
    return resultado

n1=int(input('Ingrese un número '))
n2=int(input('Ingrese otro número '))
n3=int(input('Ingrese un tercer número '))
print (f'El número mayor de los ingresados es {mayor_de_tres(n1,n2,n3)}')

'''

'''7) Escribe un programa que pida un número y diga si es divisible por 2

from unittest import result


def divisible (num):
    if num%2 == 0:
        resultado=f'{num} es divisible por 2'
    else:
        resultado=f'{num} no es divisible por 2'
    return resultado

num=int(input('Ingrese un número '))
print (divisible(num))

'''

'''8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 
(sólo hay que comprobar si lo es por uno de los cuatro)

def divisible (num):
    if num%2==0 or num%3==0 or num%5==0 or num%7==0:
        resultado= f'El numero ingresado {num} es divisible por 2, 3, 5 o 7'
    else:
        resultado=f'El numero ingresado {num} no es divisible por 2, 3, 5 o 7'
    return resultado

num=int(input('Ingrese un número '))
print (divisible(num))

'''

'''9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible 
(hay que decir todos por los que es divisible)'''



'''10) Escribir un programa que escriba en pantalla los divisores de un número dado 
'''
'''
# Con list comprehension
def divisores (num):
    resultado=[i for i in range (1, num+1) if num % i == 0]
    return resultado



#Con append en una lista nueva creada
def divisores(num):
    resultado=[]
    for i in range (1, num+1):
        if num % i == 0:
            resultado.append(i)
    return resultado

num=int(input('Ingrese un número '))
print (f'Los divisores de {num} son {divisores(num)}')
'''

'''11) Escribir un programa que nos diga si un número dado es primo 
(no es divisible por ninguno otro número que no sea él mismo o la unidad)

def numero_primo (num):
    contador=0
    for i in range (1, num+1):
        if num % i == 0:
            contador+= 1
            if contador == 2:
                resultado= 'es primo'
            else:
                resultado= 'no es primo'
    return resultado
num=int(input('Ingrese un número '))
print (f'{num} {numero_primo(num)}')

'''

'''12) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente

def calificacion (nota):
    if nota >=0 and nota<= 10:
        if nota < 3:
            resultado='Muy deficiente'
        elif nota < 5:
            resultado='Insuficiente'
        elif nota < 6:
            resultado='Suficiente'
        elif nota < 7:
            resultado='Bien'
        elif nota < 9:
            resultado='Notable'
        elif nota >= 9:
            resultado='Sobresaliente '
    else:
        resultado="La nota ingresada es inválida"
    return resultado

nota=int(input('Ingrese su nota: '))
print (f'Su nota es:  {calificacion(nota)}')

'''

'''13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma:
1
22
333
4444
55555
666666
……….


def piramide (altura):
    for fila in range (1, altura+1):
        for columna in range (1, fila+1):
            print (fila, end=' ')
        print ('')

altura=30
print (piramide(altura))
             
'''


'''14) Haz un programa que escriba una pirámide inversa de los números del 1 al número que indique el usuario de la siguiente forma (suponiendo que indica 6):
666666
55555
4444
333
22
1

def piramide_inversa (n):
    for fila in range (n, 0, -1):
        for columna in range (1, fila+1):
            print (fila, end=' ')
        print ('')
        

n=int(input('Ingrese un número '))
print(piramide_inversa(n))
'''

'''15) Crear un programa que escriba los números del 1 al 500, y que indique cuales son múltiplos
 de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por ejemplo:
1
2
3
4 (Múltiplo de 4)
5
------------------------------------------------------------
6
7
8 (Múltiplo de 4)
9 (Múltiplo de 9)
10


def lista_numeros (n):
    for n in range (1, n+1):
        if n % 4 == 0:
            print (f'{n} (Múltiplo de 4)')
        elif n % 9 == 0:
            print (f'{n} (Múltiplo de 9)')
        else:
            print (n)
        if n % 5 == 0:
            print ('-----------------------')

n=500
print (lista_numeros(n))

'''