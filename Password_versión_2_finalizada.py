#Password_versión_2

#Muestro por pantalla los datos que deber�a tener la contrase�a.
print("1.-La longitud de la contraseña tiene que tener entre 6 y 8 caracteres")
print("2.-Forçar los siguinetes valores según la posición indicada:")
print("    Posición 1: Un número mayor o igual a 1 i menor o igual a 5.")
print("    Posición 2: Una letra en minúscula.")
print("    Posición 3: Una letra en mayúscula.")
print("    Posición 4: Uno de los siguinetes símbolos *, _, @")
print("    Posición 5: Una letra minúscula.")
print("    Posición 6: Un número mayor o igual a 6 i menor o igual a 9.")
print("    Posición 7: Uno de los siguinetes símbolos &, /, #")
print("    Posición 8: Un número menor o igual que 5.")

#Cominezo con un for que se repita 3 veces e inicializo todas las variables. Adem�s, pido al usuario que introduzca una contrase�a.
for i in range(3):
    letras=0
    digitos=0
    simbolo=0
    password=str(input("Introduce una contraseña: "))
    
    #En esta parte del c�digo, si la contrase�a no tiene entre 6 y 8 caracteres que muestre un print con error.
    if len(password) < 6 or len(password) > 8:
        print(f"Error, el password tiene una longitud de {len(password)} caracteres y no cumple los requisitos.")
    
    #Si la contrase�a tuviera entre 6 y 8 caracteres, acontinuaci�n que comience otro for que recorra la contrase�a y clasifique si es una letra, un d�gito o un s�mbolo. Dependiendo de cada uno, que sume 1 a cada variable.
    else:
        for j in password:
            if j.isalpha():
                letras+=1
                
            elif j.isdigit():
                digitos+=1
                
            else:
                simbolo+=1
        
        #He decidido crear la variable que si todo se cumple, que sea True y, luego en otra l�nea muestre por pantalla que la contrase�a estar� correcta.
        cumple_todo=True 
        
        #Si la variable letras es inferior a tres que muestre por pantalla que no tiene tres letras. Adem�s, la variable cumple_todo se convierte en false.
        if letras<3:
            print("No tiene tres letras.")
            cumple_todo=False
        
        #Si la variable digitos es inferior a tres que muestre por pantalla que no tiene tres digitos. Adem�s, la variable cumple_todo se convierte en false.
        if digitos<3:
            print("No tiene tres digitos.")
            cumple_todo=False
        
        #Si la variable simbolo es inferior a dos que muestre por pantalla que no tiene dos s�mbolos. Adem�s, la variable cumple_todo se convierte en false.
        if simbolo<2:
            print("No tiene dos símbolos.")
            cumple_todo=False
        
        #Si la variable cumple_todo es correcta, que muestre por pantalla que funciona correctamente la contrase�a.
        if cumple_todo:
            print("Cumple con todos los criterios.")
