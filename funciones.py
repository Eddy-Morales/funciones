#promedio de edades 
print("eliga la opcion qu desea ejecutar")
print("1) promedio de aulas")
print("2) promedio general de todas las aulas")
print("3) salir")
opcion= int(input("ingrese el numero: "))
while opcion>3 or opcion<0 : 
    print("error ingrese el numero correcto")
    print("1) promedio de aulas")
    print("2) promedio general de todas las aulas")
    print("3) salir")
    opcion= int(input("ingrese el numero:"))

    if opcion==1:
        conteo=0
        num_aulas=int(input("ingrese el numero de aulas: "))
        num_est=int(input("ingrese numero de estudiantes del aula: "))
        for i in range(1, num_aulas+1):
            edad_est=int(input(f"ingrese la edad {i}: "))
            num_aulas+1

        