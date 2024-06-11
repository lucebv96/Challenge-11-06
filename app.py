
def invertir_caracteres(cadena_de_caracteres):
    if len(cadena_de_caracteres) == 0:
        print("")
        return " "
    else:
        return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1])
    

#Se pide al usuario que ingrese la palabra a invertir

palabra = input('Ingrese la palabra que desea invertir: ')

#Se envia la palabra a la funcion para invertirla y el retorno se guarda en la variable resultado
resultado = invertir_caracteres(palabra)


if len(palabra) > 0:
#Se muestra en pantalla la palabra invertida
    print("La palabra invertida es: ", resultado)
else: 
    #En caso de haber dejado el campo vacio se le informa al usuario que no ha ingresado nada
    print ("No ha ingresado ninguna palabra")