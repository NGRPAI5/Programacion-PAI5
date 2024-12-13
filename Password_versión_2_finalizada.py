#Password_versi√≥n_2

#Muestro por pantalla los datos que deberÌa tener la contraseÒa.
print("1.-La longitud de la contrase√±a tiene que tener entre 6 y 8 caracteres")
print("2.-For√ßar los siguinetes valores seg√∫n la posici√≥n indicada:")
print("    Posici√≥n 1: Un n√∫mero mayor o igual a 1 i menor o igual a 5.")
print("    Posici√≥n 2: Una letra en min√∫scula.")
print("    Posici√≥n 3: Una letra en may√∫scula.")
print("    Posici√≥n 4: Uno de los siguinetes s√≠mbolos *, _, @")
print("    Posici√≥n 5: Una letra min√∫scula.")
print("    Posici√≥n 6: Un n√∫mero mayor o igual a 6 i menor o igual a 9.")
print("    Posici√≥n 7: Uno de los siguinetes s√≠mbolos &, /, #")
print("    Posici√≥n 8: Un n√∫mero menor o igual que 5.")

#Cominezo con un for que se repita 3 veces e inicializo todas las variables. Adem·s, pido al usuario que introduzca una contraseÒa.
for i in range(3):
    letras=0
    digitos=0
    simbolo=0
    password=str(input("Introduce una contrase√±a: "))
    
    #En esta parte del cÛdigo, si la contraseÒa no tiene entre 6 y 8 caracteres que muestre un print con error.
    if len(password) < 6 or len(password) > 8:
        print(f"Error, el password tiene una longitud de {len(password)} caracteres y no cumple los requisitos.")
    
    #Si la contraseÒa tuviera entre 6 y 8 caracteres, acontinuaciÛn que comience otro for que recorra la contraseÒa y clasifique si es una letra, un dÌgito o un sÌmbolo. Dependiendo de cada uno, que sume 1 a cada variable.
    else:
        for j in password:
            if j.isalpha():
                letras+=1
                
            elif j.isdigit():
                digitos+=1
                
            else:
                simbolo+=1
        
        #He decidido crear la variable que si todo se cumple, que sea True y, luego en otra lÌnea muestre por pantalla que la contraseÒa estar· correcta.
        cumple_todo=True 
        
        #Si la variable letras es inferior a tres que muestre por pantalla que no tiene tres letras. Adem·s, la variable cumple_todo se convierte en false.
        if letras<3:
            print("No tiene tres letras.")
            cumple_todo=False
        
        #Si la variable digitos es inferior a tres que muestre por pantalla que no tiene tres digitos. Adem·s, la variable cumple_todo se convierte en false.
        if digitos<3:
            print("No tiene tres digitos.")
            cumple_todo=False
        
        #Si la variable simbolo es inferior a dos que muestre por pantalla que no tiene dos sÌmbolos. Adem·s, la variable cumple_todo se convierte en false.
        if simbolo<2:
            print("No tiene dos s√≠mbolos.")
            cumple_todo=False
        
        #Si la variable cumple_todo es correcta, que muestre por pantalla que funciona correctamente la contraseÒa.
        if cumple_todo:
            print("Cumple con todos los criterios.")
