#Password_versión_2

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

for i in range(3):
    letras=0
    digitos=0
    simbolo=0
    password=str(input("Introduce una contraseña: "))
    
    for j in password:
        
        if j.isalpha()==True:
            letras+=1
            
        elif j.isdigit()==True:
            digitos+=1
            
        elif j in "@#~%¬&/()=":
            simbolo+=1
            
    if letras<3:
        print("No tiene tres letras.")
        
    if digitos<3:
        print("No tiene tres digitos.")
        
    if simbolo<2:
        print("No tiene dos símbolos.")
        
    else:
        print("Cumple con los criterios")
        
