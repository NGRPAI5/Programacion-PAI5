#Password_versi贸n_2

#Muestro por pantalla los datos que deber韆 tener la contrase馻.
print("1.-La longitud de la contrase帽a tiene que tener entre 6 y 8 caracteres")
print("2.-For莽ar los siguinetes valores seg煤n la posici贸n indicada:")
print("    Posici贸n 1: Un n煤mero mayor o igual a 1 i menor o igual a 5.")
print("    Posici贸n 2: Una letra en min煤scula.")
print("    Posici贸n 3: Una letra en may煤scula.")
print("    Posici贸n 4: Uno de los siguinetes s铆mbolos *, _, @")
print("    Posici贸n 5: Una letra min煤scula.")
print("    Posici贸n 6: Un n煤mero mayor o igual a 6 i menor o igual a 9.")
print("    Posici贸n 7: Uno de los siguinetes s铆mbolos &, /, #")
print("    Posici贸n 8: Un n煤mero menor o igual que 5.")

#Cominezo con un for que se repita 3 veces e inicializo todas las variables. Adem醩, pido al usuario que introduzca una contrase馻.
for i in range(3):
    letras=0
    digitos=0
    simbolo=0
    password=str(input("Introduce una contrase帽a: "))
    
    #En esta parte del c骴igo, si la contrase馻 no tiene entre 6 y 8 caracteres que muestre un print con error.
    if len(password) < 6 or len(password) > 8:
        print(f"Error, el password tiene una longitud de {len(password)} caracteres y no cumple los requisitos.")
    
    #Si la contrase馻 tuviera entre 6 y 8 caracteres, acontinuaci髇 que comience otro for que recorra la contrase馻 y clasifique si es una letra, un d韌ito o un s韒bolo. Dependiendo de cada uno, que sume 1 a cada variable.
    else:
        for j in password:
            if j.isalpha():
                letras+=1
                
            elif j.isdigit():
                digitos+=1
                
            else:
                simbolo+=1
        
        #He decidido crear la variable que si todo se cumple, que sea True y, luego en otra l韓ea muestre por pantalla que la contrase馻 estar� correcta.
        cumple_todo=True 
        
        #Si la variable letras es inferior a tres que muestre por pantalla que no tiene tres letras. Adem醩, la variable cumple_todo se convierte en false.
        if letras<3:
            print("No tiene tres letras.")
            cumple_todo=False
        
        #Si la variable digitos es inferior a tres que muestre por pantalla que no tiene tres digitos. Adem醩, la variable cumple_todo se convierte en false.
        if digitos<3:
            print("No tiene tres digitos.")
            cumple_todo=False
        
        #Si la variable simbolo es inferior a dos que muestre por pantalla que no tiene dos s韒bolos. Adem醩, la variable cumple_todo se convierte en false.
        if simbolo<2:
            print("No tiene dos s铆mbolos.")
            cumple_todo=False
        
        #Si la variable cumple_todo es correcta, que muestre por pantalla que funciona correctamente la contrase馻.
        if cumple_todo:
            print("Cumple con todos los criterios.")
