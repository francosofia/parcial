#1. Traer keyss desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
#cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
#un personaje puede tener más de una raza y más de una habilidad.
#2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que
#corresponden a esa raza.
#3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
#personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
#repetirse en los distintos listados.
#4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
#deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.
#5. Jugar batalla: El usuario seleccionará un personaje. La máquina selecciona otro al azar. Gana la
#batalla el personaje que más poder de ataque tenga. El personaje que gana la batalla se deberá
#guardar en un archivo de texto, incluyendo la fecha de la batalla, el nombre del personaje que ganó y
#el nombre del perdedor. Este archivo anexará cada dato.
#6. Guardar Json: El usuario ingresa una raza y una habilidad. Generar un listado de los personajes que
#cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. Deberíamos
#guardar el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
#búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza.
#Por ejemplo: si el usuario ingresa Raza: Saiyan y Habilidad: Genki Dama
#Nombre del archivo:
#Saiyan_Genki_Dama.Json
#Datos :
#Goten - 3000 - Kamehameha + Tambor del trueno
#Goku - 5000000 - Kamehameha + Super Saiyan 2
#7. Leer Json: permitirá mostrar un listado con los personajes guardados en el archivo Json de la opción
#6.
#8. Salir del programa.

#1
#1. Traer keyss desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
#cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
#un personaje puede tener más de una raza y más de una habilidad.
import re
def guardar_archivo(nombre:str)->list:
    lista_personajes = []
    with open(nombre,"r+", encoding = "utf-8") as mi_archivo:
        for linea in mi_archivo:
            dato = re.split(",|\n",linea)
            keys = {}
            keys["id"] = int(dato[0])
            keys["nombre"] = dato[1]
            validacion_raza = re.search("-H",dato[2])
            if  validacion_raza != None:
                lista_raza = re.split("-",dato[2])
                keys["raza"]= lista_raza
            else:
                lista_raza =[]
                lista_raza.append(dato[2])
                keys["raza"] = lista_raza
            keys["poder_pelea"] = int(dato[3])
            keys["poder_ataque"] = int(dato[4])
            validacion_habilidades = re.search("|$%",dato[5])
            if  validacion_habilidades != None:
                lista_habilidades = re.split('[|$%]+',dato[5])
                keys["habilidades"] = lista_habilidades
            else:
                lista_habilidades = []
                lista_habilidades.append(dato[5])
                keys["habilidades"] = lista_habilidades
            lista_personajes.append(keys)

    return lista_personajes
#
#mostrar_primera = guardar_archivo("parcial_progra_labo01//dragonball.csv")
#print(mostrar_primera)
#
lista_trabajar = []
lista_trabajar = guardar_archivo("parcial_progra_labo01//dragonball.csv")

#2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que
#corresponden a esa raza.
def cantidad_raza(lista:list, clave:str):
    contador = {}
    for linea in lista:
        if clave in linea:
            valor = linea[clave]
            for razas in valor:
                if razas in contador:
                    contador[razas] += 1
                else:
                    contador[razas] = 1

    return  contador
#
#mostrar_segunda =cantidad_raza(lista_trabajar,"raza")
#print(mostrar_segunda)

#3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
#personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
#repetirse en los distintos listados.


#def listar_raza(lista:list,clave:str)->list:
#    diccionario_nombre_poder = {}
#    for linea in lista:
#        if clave in linea:
#            valor = linea[clave]
#            nombre = linea["nombre"]
#            poder_ataque = linea["poder_ataque"]
#            diccionario_nombre_poder["nombre"] = nombre
#            diccionario_nombre_poder["poder_ataque"] = poder_ataque
#            for raza in valor:
#                if  raza in diccionario_nombre_poder:
#                    diccionario_nombre_poder[clave] = raza
#                else:
#                    diccionario_nombre_poder[clave] = raza#

#def listar_raza(lista:list,clave:str)->dict:
#    diccionario_raza_personajes = {}
#    for linea in lista:
#        if clave in linea:
#            valor = linea[clave]
#            nombre = linea["nombre"]
#            poder_ataque = linea["poder_ataque"]
#            for raza in valor:
#                if raza in diccionario_raza_personajes:
#                    diccionario_raza_personajes[raza].append({"nombre": nombre, "poder_ataque": poder_ataque})
#                else:
#                    diccionario_raza_personajes[raza] = [{"nombre": nombre, "poder_ataque": poder_ataque}]
#    return diccionario_raza_personajes










def listar_raza():
    diccionario= {}
    lista=[]
    for linea in lista_trabajar:
        valor_raza= linea["raza"]

        for raza in valor_raza:
            if raza in valor_raza:
                diccionario[raza]+=[linea]
            else:
                diccionario[raza] = [linea]
    for raza in diccionario:
        print(f"{raza}")
        nombre=linea["nombre"]
        poder_ataque=linea["poder_ataque"]
        print(f"Nombre:{nombre} | Poder de ataque:{poder_ataque}")
        print()





#
#    return lista_raza
#
#mostrar = listar_raza()
#print(mostrar)
#
#4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
#deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.



#
#mostrar = listar_raza(lista_trabajar,"raza")
#print(mostrar)
#

#menu = []
#
#def mostrar_menu():
#    for opcion in menu:
#        print(opcion)
#
#seguir = True
#while seguir == True:
#    mostrar_menu()
#    respuesta = int(input("ingresa una opcion:"))
#    match respuesta:
#        case 1:
#            mostrar =guardar_archivo()
#        case 2:
#            seguir = False
#














































