##importar datos de las credenciales
from modulo.credenciales_usuario import PASS , USERNAME


# user = input ("Ingrese User: \n")

# if user == USERNAME:
#     password = input ("Ingrese password: \n")
#     if password == '':
#         print("El password no puede estar vacio")
#     elif ' ' in password:
#         print("Ojo, que hay un espacio vacio")
#     elif not password.isdigit():
#         print("el password debe ser numerico")
#     else:
#         if password == PASS:
#             print("Bienvenido usuario")

# else:
#     print("usuario no valido")


## ___Hecho por mi mas saimple___

# user= input("INGRESE USUARIO: ")
# if user==USERNAME:
#     passw=input("ingrese contraseña: ")
#     if passw!=PASS:
#         print("contraseña incorrecta")
#     else:
#         print("bienvenido(a) al sistema")
# else:
#     print("usuario no valido")

# number = 0
# while number <10:
#     print(number)
#     number += 1 # number = number +1


# flag:bool = True
# chars_de_negacion = ['n', 'N', 'no', 'No', 'NO']

# while flag:

#     print("agregar usuario")

#     user_stopper = input("desea agregar otro usuario?")

#     if user_stopper in chars_de_negacion:
#         flag = not flag
#         print("Ya no se cargara un usuario")

    

# else: 
#     print("Se cerro la carga de usuarios y cerramos la base de datos")



# texto = "Hola mundo desde codo a codo"

# # for i in range(len(texto)):
# #     print(texto[i])

# inicio= "Inicio bucle"
# fin = "fin de procesos"

# print(f"{inicio:*^40}")

# for chars in texto:  # es igual a  for i in range(len(texto)):   // print(texto[i])
#     print(chars)
# else:
#     print("cierro bucle")
# print(f"{fin:*^40}")


#EJERCICIO °1   #min 54

import sqlite3
nombre_base_datos = 'libreria_23508.db'

conn = sqlite3.connect(nombre_base_datos)
cursor = conn.cursor()

ddl_query_table = f"""
CREATE TABLE IF NOT EXISTS USER (
id_user INTEGER PRIMARY KEY AUTOINCREMENT,
username VARCHAR,
password VARCHAR
)
""" 

cursor.execute(ddl_query_table)

flag:bool = True
chars_de_negacion = ['n', 'N', 'no', 'No', 'NO']

while flag:

    print("agregar usuario")
    user = input('ingrese el nombre del usuario:\t ')
    password = input('ingrese su contraseña:\t ')

    insert_query = f"""

    INSERT INTO USER
    (username, password)
    VALUES
    ('{user}','{password}');
    """

    cursor.execute(insert_query)


    user_stopper = input("desea agregar otro usuario?\t")

    if user_stopper in chars_de_negacion:
        flag = not flag
        print("Ya no se cargaran usuarios")
    else:
        print("Carga el siguiente usuario")
    

else: 
    conn.commit()
    print("Se commitiaron los cambios")
    conn.close()
    print("Se cierra la base de datos")


##EJERCICIO ° 2 AÑO BISIESTO

fecha_tope = int(input("fecha de tope:\t"))

for year in range(1940, fecha_tope):
    primera_condicion:bool = (year%400 == 0)
    segunda_condicion:bool = ((year%4 == 0) and (year%100 != 0))

    if primera_condicion or segunda_condicion:
        print(f'El año {year:~^10} es bisiesto😉')
    

