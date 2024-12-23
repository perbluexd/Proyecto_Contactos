# -*- coding: utf-8 -*-
contactos = {}

def agregarCategoria(contactos):
    while True:
        categoria = input("Escribe el nombre de la categoría de contactos que deseas agregar: ")
        if categoria in contactos:
            print("La categoría ya existe, sigue intentando")
        else:
            contactos[categoria] = []
            print(f"Categoría '{categoria}' agregada exitosamente.")
        
        salida = input("Si deseas salir presiona 's', si deseas continuar presiona 'c': ").lower()
        if salida == "s":
            print("¡Hasta pronto!")
            break

def agregarContacto(contactos):
    categoria = input("Escribe el nombre de la categoría donde quieres agregar el contacto: ")
    if categoria not in contactos:
        print("Por favor crea la categoría antes de ingresar contactos, ¡Hasta pronto!")
        return
    while True:
        nombre = input("Ingresa el nombre del contacto: ")
        if any(nombre in contacto for contacto in contactos[categoria]):
            print("El contacto ya existe en esta categoría. Intenta con otro nombre.")
            continue

        try:
            numero = int(input("Ingresa el número del contacto: "))
            contactos[categoria].append({nombre: numero})
            print(f"Contacto '{nombre}' agregado exitosamente.")
        except ValueError:
            print("Ingresa un número válido.")
        
        opcion = input("Si deseas agregar más contactos a la categoría presiona 'c', si deseas salir presiona 's': ").lower()
        if opcion == "s":
            print("¡Hasta pronto!")
            break
        
def eliminarContacto(contactos):
    categoria = input("Escribe la categoría desde la cual quieres eliminar un contacto: ")
    if categoria not in contactos:
        print("La categoría no se encuentra en el listado, inténtalo de nuevo.")
        return
    
    while True:
        contacto = input("Ingresa el nombre del contacto que deseas eliminar: ")
        for i, item in enumerate(contactos[categoria]):
            if contacto in item:
                contactos[categoria].pop(i)
                print(f"Contacto '{contacto}' eliminado con éxito.")
                return
        print("El contacto no se ha encontrado, intenta de nuevo.")

def editarContacto(contactos):
    categoria = input("Ingresa el nombre de la categoría donde quieres editar el contacto: ")
    if categoria not in contactos:
        print("La categoría no se encuentra, intenta crearla primero.")
        return

    while True:
        opcion = input("Si deseas editar el nombre presiona 'n', si deseas editar el número presiona 'p': ").lower()
        
        if opcion == "n":
            nombreactual = input("Ingresa el nombre actual del contacto: ")
            for contacto in contactos[categoria]:
                if nombreactual in contacto:
                    nombrenuevo = input("Ingresa el nuevo nombre del contacto: ")
                    contacto[nombrenuevo] = contacto.pop(nombreactual)
                    print(f"Contacto '{nombreactual}' actualizado a '{nombrenuevo}'.")
                    return
            print("El contacto no se encontró.")
        
        elif opcion == "p":
            nombreactual = input("Ingresa el nombre del contacto que deseas editar: ")
            for contacto in contactos[categoria]:
                if nombreactual in contacto:
                    nuevonumero = int(input("Ingresa el nuevo número del contacto: "))
                    contacto[nombreactual] = nuevonumero
                    print(f"El número de '{nombreactual}' ha sido actualizado.")
                    return
            print("El contacto no se encontró.")
            
def mostrarContactos(contactos):
    for categoria, lista_contactos in contactos.items():
        print(f"Categoría: {categoria}")
        for contacto in lista_contactos:
            for nombre, numero in contacto.items():
                print(f"  Nombre: {nombre}, Número: {numero}")

def buscarContacto(contactos):
    categoria = input("De qué categoría es el contacto que deseas buscar: ")
    if categoria not in contactos:
        print("La categoría no se encuentra. Vuelve a intentarlo.")
        return
    
    nombre = input("Ingresa el nombre del contacto que deseas buscar: ")
    for contacto in contactos[categoria]:
        if nombre in contacto:
            print(f"Contacto encontrado: {nombre} - {contacto[nombre]}")
            return
    print("El contacto no se encontró.")
        
        
def menu():
    while True:
        opcion = input("Este es el menú de opciones que tienes en nuestro listado de contactos \n1. Agregar Categoría \n2. Agregar Contacto \n3. Eliminar Contacto \n4. Editar Contacto \n5. Mostrar Contactos \n6. Buscar Contacto \n7. Salir del Menú \nSelecciona un número: ")
        if opcion == "1":
            agregarCategoria(contactos)
        elif opcion == "2":
            agregarContacto(contactos)
        elif opcion == "3":
            eliminarContacto(contactos)
        elif opcion == "4":
            editarContacto(contactos)
        elif opcion == "5":
            mostrarContactos(contactos)
        elif opcion == "6":
            buscarContacto(contactos)
        elif opcion == "7":
            print("Gracias por usar la lista de contactos, hasta pronto :)")
            break

if __name__ == "__main__":
    menu()
        
        
        
