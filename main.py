from btree import BTree, Provider
from random import randint
general_continue = True

def main():
    t = 2
    btree = BTree(t)
    while general_continue:
        try:
            option = menu()
            switch(option, btree)
        except ValueError:
            print("ERROR!, Ingrese un dato válido")

def menu():
    print("\nServicios Locales")
    print("1. Registrar Proveedor")
    print("2. Buscar Servicio")
    print("3. Mostrar Proveedores")
    print("4. Salir")
    option = int(input("Ingrese una opción: "))
    return option

def switch(option, btree):
    match option:
        case 1:
            register_provider(btree)
        case 2:
            search_service(btree)
        case 3:
            show_providers(btree)
        case 4:
            go_out()
        case _:
            print("ERROR!, Ingrese una opción válida (1 - 4)")

def register_provider(btree):
    try:
        provider_id = int(input("Ingrese el ID del proveedor: "))
        if provider_id <= 0:
            print("ERROR!, El ID debe ser un número positivo")
            return
    except ValueError:
        print("ERROR!, ID inválido")
        return
    if btree.exists_id(provider_id):
        print("ERROR!, El ID del proveedor ya existe")
        return
    name = input("Ingrese el nombre del proveedor: ")
    service = input("Ingrese el servicio del proveedor: ")
    try:
        rating = float(input("Ingrese la calificación del proveedor (1-5): "))
        if rating < 1 or rating > 5:
            print("ERROR!, La calificación debe estar entre 1 y 5")
            return
    except ValueError:
        print("ERROR!, Calificación inválida")
        return
    provider = Provider(provider_id, name, service, rating)
    btree.insert(provider)
    print("Proveedor registrado exitosamente")

def search_service(btree):
    if btree.is_empty():
        print("No hay proveedores registrados")
        return
    service = input("Ingrese el servicio a buscar: ")
    results = btree.search_by_service(service)
    if results:
        print(f"Proveedores que ofrecen el servicio '{service}':")
        for provider in sorted(results, key = lambda x: (x.service, x.name)):
            print(provider)
    else:
        print("No se encontraron proveedores para el servicio solicitado")

def show_providers(btree):
    if btree.is_empty():
        print("No hay proveedores registrados")
        return
    print("Lista de Proveedores:")
    btree.traverse()

def go_out():
    global general_continue
    print("Saliendo del programa")
    exit()

main()