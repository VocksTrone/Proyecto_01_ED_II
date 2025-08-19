RESET   = "\033[0m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

class Mensajes:
    @staticmethod
    def local_services():
        print("\n ")
        print(GREEN + "╔════════════════════════════════════════╗" + RESET)
        print(GREEN + "║ " + WHITE + "          SERVICIOS  LOCALES          " + GREEN + " ║" + RESET)
        print(GREEN + "╚════════════════════════════════════════╝" + RESET)

    @staticmethod
    def register_provider():
        print("\n ")
        print(YELLOW + "╔════════════════════════════════════════╗" + RESET)
        print(YELLOW + "║ " + WHITE + "          REGISTRAR PROVEEDOR         " + YELLOW + " ║" + RESET)
        print(YELLOW + "╚════════════════════════════════════════╝" + RESET)

    @staticmethod
    def search_service():
        print("\n ")
        print(BLUE + "╔════════════════════════════════════════╗" + RESET)
        print(BLUE + "║ " + WHITE + "            BUSCAR SERVICIO           " + BLUE + " ║" + RESET)
        print(BLUE + "╚════════════════════════════════════════╝" + RESET)

    @staticmethod
    def show_providers():
        print("\n ")
        print(MAGENTA + "╔════════════════════════════════════════╗" + RESET)
        print(MAGENTA + "║ " + WHITE + "         LISTA DE PROVEEDORES         " + MAGENTA + " ║" + RESET)
        print(MAGENTA + "╚════════════════════════════════════════╝" + RESET)

    @staticmethod
    def top5_providers():
        print("\n ")
        print(CYAN + "╔════════════════════════════════════════╗" + RESET)
        print(CYAN + "║ " + WHITE + "           TOP 5 PROVEEDORES          " + CYAN + " ║" + RESET)
        print(CYAN + "╚════════════════════════════════════════╝" + RESET)
