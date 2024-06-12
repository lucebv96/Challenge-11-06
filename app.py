#Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

#Se define 'n' como el numero que definira la tabla de multiplicar que desea ver el usuario :)
n = int(input("La tabla de que numero desea visualizar? "))

#Se inicializa las variables
resultado = 0 
i= 1 #Se define a i como contador

#Bucle que realiza e imprime la tabla
print('La tabla del ',n ,': ')
while i<=10:
    resultado = (n*i)
    print(n,' x ',i,': ',resultado) 
    i = i+1
