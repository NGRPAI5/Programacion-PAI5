#Password versi�n 1

#Muestro por pantalla las siguientes instrucciones.
print("1.-La longitud de la contrase�a tiene que tener entre 6 y 8 caracteres.")
print("2.-Forzar los siguientes valores seg�n la posici�n indicada:")
print("    Posici�n 1: Un n�mero mayor o igual a 1 y menor o igual a 5.")
print("    Posici�n 2: Una letra en min�scula.")
print("    Posici�n 3: Una letra en may�scula.")
print("    Posici�n 4: Uno de los siguinetes s�mbolos *, _, @")
print("    Posici�n 5: Una letra min�scula.")
print("    Posici�n 6: Un n�mero mayor o igual a 6 y menor o igual a 9.")
print("    Posici�n 7: Uno de los siguientes s�mbolos &, /, #")
print("    Posici�n 8: Un n�mero menor o igual que 5.")

#Creo una variable password que pregunte por una contrase�a. Adem�s creo otra que empieza en False para luego poder mostrar que la contrase�a es correcta si sigue siendo False.
password=str(input("Introduce la contrase�a: "))
error=False

#Calculo la longitud del password y miro si es igual o m�s grande que 6 o igual o m�s peque�o que 8. Por �ltimo, si hay error que la variable sea True.
if len(password) < 6 or len(password) > 8:
    print(f"Error, el password tiene una longitud de {len(password)} caracteres y no cumple los requisitos.")
    error = True

#Si no fallase la longitud del password, es decir que est� comprendida entre 6 y 8, que compruebe lo siguiente:    
else:
    
    #Si el primer d�gito no es igual o superior a 1 o igual o inferior a 5, que muestre un print diciendo error.
    if not 1 <= int(password[0]) <= 5:
        print("Error en el caracter 1. ", end="")
        error = True
        
    #Si el segundo d�gito no es min�scula, que muestre un print diciendo error.
    if not password[1].islower():
        print("Error en el caracter 2. ", end="")
        error = True
        
    #Si el tercer d�gito no es may�scula, que muestre un print diciendo error.
    if not password[2].isupper():
        print("Error en el caracter 3. ", end="")
        error = True
    
    #Si el cuarto d�gito no es *, _, @, que muestre un print diciendo error.
    if password[3] not in "*_@":
        print("Error en el caracter 4. ", end="")
        error = True
    
    #Si el quinto d�gito no es min�scula, que muestre un print diciendo error.
    if not password[4].islower():
        print("Error en el caracter 5. ", end="")
        error = True
    
    #Si el sexto d�gito no est� comprendido entre el rango de 6 y 9, que muestre un print diciendo error.
    if not 6 <= int(password[5]) <= 9:
        print("Error en el caracter 6. ", end="")
        error = True
        
    #Si la contrase�a del password es superior a los 6 d�gitos, que prosiga con el siguiente print. De esta forma no salta error en la consola.
    if len(password) > 6:    
        #Si el s�ptimo d�gito no tiene &, /, #, que diga error en la consola.
        if password[6] not in "&/#":
            print("Error en el caracter 7. ", end="")
            error = True
    
    #Si la contrase�a del password es superior a los 7 d�gitos, que prosiga con el siguiente print. De esta forma no salta error.
    if len(password) > 7:
        #Si el s�ptimo d�gito no es superior a 5 o igual, que diga error.
        if not int(password[7]) < 5:
            print("Error en el caracter 8. ", end="")
            error = True

#Para acabar, si error no es True que muestre por pantalla que la contrase�a es correcta.        
if not error:
    print("El formato de password es correcto.")
