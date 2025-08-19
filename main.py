from btree import BTree, Provider
from random import randint, uniform
from mensajes import Mensajes
import time
from provider import rating_to_stars

RESET   = "\033[0m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

general_continue = True

def main():
    t = 2
    btree = BTree(t)
    while general_continue:
        try:
            option = menu()
            switch(option, btree)
        except ValueError:
            print(RED + "\nERROR!, Ingrese un dato válido" + RESET)

def menu():
    print("\n ")
    Mensajes.local_services()
    print("1. Registrar Proveedor")
    print("2. Buscar Servicio")
    print("3. Mostrar Proveedores")
    print("4. Clasificación Top 5 Proveedores")
    print("5. Salir")
    option = int(input(YELLOW + "Ingrese una opción: " + RESET))
    return option

def switch(option, btree):
    match option:
        case 1:
            Mensajes.register_provider()
            register_provider(btree)
        case 2:
            Mensajes.search_service()
            search_service(btree)
        case 3:
            Mensajes.show_providers()
            show_providers(btree)
        case 4:
            Mensajes.top5_providers()
            ranking_menu(btree)
        case 5:
            go_out()
        case _:
            print(RED + "\nERROR!, Ingrese una opción válida (1 - 5)" + RESET)

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
    print(GREEN + f"\nProveedor registrado exitosamente" + RESET)

def calculate_rating():
    quantity = randint(10, 20)
    calification = [uniform(0, 5) for _ in range(quantity)]
    average = sum(calification) / quantity
    return round(average, 1)

def search_service(btree):
    if btree.is_empty():
        print(YELLOW + "\nNo hay proveedores registrados" + RESET)
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
                    print(YELLOW + f"\nContrato iniciado con {selected.name} ({selected.service})..." + RESET)
                    time.sleep(5)
                    print("\nContrato finalizado")
                    while True:
                        try:
                            new_rating = float(input("Califique el servicio (1.0 - 5.0): "))
                            if 1.0 <= new_rating <= 5.0:
                                selected.rating = round((selected.rating + new_rating) / 2, 1)
                                print(f"\nNueva calificación promedio de {selected.name}: {selected.rating:.1f} {rating_to_stars(selected.rating)}")
                                break
                            else:
                                print(YELLOW + "Ingrese un valor entre 1.0 y 5.0" + RESET)
                        except ValueError:
                            print(YELLOW + "Ingrese un número válido" + RESET)
                else:
                    print(RED + "\nNo se encontró un proveedor con ese ID" + RESET)
            except ValueError:
                print(RED + "\nIngrese un número válido" + RESET)
    else:
        print(RED + "\nNo se encontraron proveedores para el servicio solicitado" + RESET)


def show_providers(btree):
    if btree.is_empty():
        print(RED + "\nNo hay proveedores registrados" + RESET)
        return
    print("\nLista de Proveedores:")
    btree.traverse()

def show_top5_global(btree):
    providers = []
    btree._collect(btree.root, providers)
    providers.sort(key=lambda p: p.rating, reverse=True)

    print("\nClasificación Top 5 Global")
    for i, provider in enumerate(providers[:5], start=1):
        print(f"{i}. {provider}")

def show_top5_by_service(btree):
    service = input("\nIngrese el servicio para ver el Top 5: ")
    results = btree.search_by_service(service)

    if results:
        results.sort(key=lambda p: p.rating, reverse=True)
        print(f"\nClasificación Top 5 de {service.capitalize()}")
        for i, provider in enumerate(results[:5], start=1):
            print(f"{i}. {provider}")
    else:
        print(f"\nNo se encontraron proveedores para el servicio '{service}'")

def ranking_menu(btree):
    if btree.is_empty():
        print("\nNo hay proveedores registrados")
        return
        
    print("1. Top 5 Global")
    print("2. Top 5 por Servicio")
    try:
        opt = int(input("Seleccione una opción: "))
        if opt == 1:
            show_top5_global(btree)
        elif opt == 2:
            show_top5_by_service(btree)
        else:
            print(RED + "Opción inválida" + RESET)
    except ValueError:
        print(RED + "Ingrese un número válido" + RESET)

def go_out():
    global general_continue
    print("\nSaliendo del programa")
    exit()

main()