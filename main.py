from btree import BTree, Provider
from random import randint, uniform
import time

general_continue = True

def main():
    t = 2
    btree = BTree(t)
    while general_continue:
        try:
            option = menu()
            switch(option, btree)
        except ValueError:
            print("\nERROR!, Ingrese un dato válido")

def menu():
    print("\n---Servicios Locales---")
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
            print("\nERROR!, Ingrese una opción válida (1 - 4)")

def register_provider(btree):
    provider_id = randint(1000, 9999)
    print(f"\nID del Proveedor: {provider_id}")
    if btree.exists_id(provider_id):
        print("\nERROR!, El ID del proveedor ya existe")
        return
    name = input("Ingrese el nombre del proveedor: ")
    service = input("Ingrese el servicio principal del proveedor: ")
    rating = calculate_rating()
    provider = Provider(provider_id, name, service, rating)
    btree.insert(provider)
    print(f"\nProveedor registrado exitosamente")

def calculate_rating():
    quantity = randint(10, 20)
    calification = [uniform(0, 5) for _ in range(quantity)]
    average = sum(calification) / quantity
    return round(average, 1)

def search_service(btree):
    if btree.is_empty():
        print("\nNo hay proveedores registrados")
        return

    service = input("\nIngrese el servicio a buscar: ")
    results = btree.search_by_service(service)

    if results:
        print(f"\nProveedores que ofrecen el servicio -{service}-:")
        ordered = sorted(results, key=lambda x: x.rating, reverse=True)
        for provider in ordered:
            print(provider)

        contratar = input("\n¿Desea contratar un servicio? (s/n): ").strip().lower()
        if contratar == "s":
            try:
                prov_id = int(input("\nIngrese el ID del proveedor que desea contratar: "))
                selected = next((p for p in ordered if p.provider_id == prov_id), None)

                if selected:
                    print(f"\nContrato iniciado con {selected.name} ({selected.service})...")
                    time.sleep(5)
                    print("\nContrato finalizado")
                    while True:
                        try:
                            new_rating = float(input("Califique el servicio (1.0 - 5.0): "))
                            if 1.0 <= new_rating <= 5.0:
                                selected.rating = round((selected.rating + new_rating) / 2, 1)
                                print(f"\nNueva calificación promedio de {selected.name}: {selected.rating}★")
                                break
                            else:
                                print("Ingrese un valor entre 1.0 y 5.0")
                        except ValueError:
                            print("Ingrese un número válido")
                else:
                    print("\nNo se encontró un proveedor con ese ID")
            except ValueError:
                print("\nIngrese un número válido")
    else:
        print("\nNo se encontraron proveedores para el servicio solicitado")


def show_providers(btree):
    if btree.is_empty():
        print("\nNo hay proveedores registrados")
        return
    print("\nLista de Proveedores:")
    btree.traverse()

def go_out():
    global general_continue
    print("\nSaliendo del programa")
    exit()

main()