#20.-A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclado números entre 0 y 10

var_1=int(input("Introduce un n�mero: "))
var_2=int(input("Introduce otro n�mero: "))

if var_1>10 or var_1<(-1):
    print("Uno o los dos n�meros est�n fuera de los l�mites establecidos")
    
elif var_2>10 or var_1<(-1):
    print("Uno o los dos n�meros est�n fuera de los l�mites establecidos")
    
else:

    if var_1>var_2:
        print(f"El n�mero {var_1} es superior al n�mero {var_2}")

    elif var_1<var_2:
        print(f"El n�mero {var_2} es superior al n�mero {var_1}")
    
    else:
        print(f"El n�mero {var_1} es igual al n�mero {var_2}")

