#Password versión 2

#Muestro por pantalla las siguientes instrucciones.
print("1.-La longitud de la contraseña tiene que tener entre 6 y 8 caracteres.")
print("2.-Forzar los siguientes valores según la posición indicada:")
print("    Posición 1: Un número mayor o igual a 1 y menor o igual a 5.")
print("    Posición 2: Una letra en minúscula.")
print("    Posición 3: Una letra en mayúscula.")
print("    Posición 4: Uno de los siguinetes sí­mbolos *, _, @")
print("    Posición 5: Una letra minúscula.")
print("    Posición 6: Un número mayor o igual a 6 y menor o igual a 9.")
print("    Posición 7: Uno de los siguientes sí­mbolos &, /, #")
print("    Posición 8: Un número menor o igual que 5.")

error=False
letra=""
posicion=0
posicion_2=0
simbolos="*_@"
    
for i in range(3):
    password=str(input("Introduce la contraseña: "))
    
    if len(password) < 6 or len(password) > 8:
        print(f"Error, el password tiene una longitud de {len(password)} caracteres y no cumple los requisitos.")
        error = True
            
    if password.isupper() or password.islower() in password:
        print("Tiene una mayúscula o minúscula.")
        
    if password==simbolos:
        print("Tiene símbolos.")
        
        
    
