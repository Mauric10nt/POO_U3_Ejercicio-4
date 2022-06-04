from IngresadorTeclado import IngresadorTeclado
from ManejadorCalefactores import ManejadorCalefactores
from Menu import Menu


if __name__ == "__main__":
    unIngresador = IngresadorTeclado()
    dimension = unIngresador.inputInt("Ingrese el tamaño de la coleccion para almacenar los calefactores: ")
    while dimension <= 0:
        print("El tamaño debe ser mayor a 0")
        dimension = unIngresador.inputInt("Ingrese el tamaño de la coleccion para almacenar los calefactores: ")
    unManejadorCalefactores = ManejadorCalefactores(dimension)
    unManejadorCalefactores.cargarGascsv("calefactor-gas.csv")
    unManejadorCalefactores.cargarElectricoscsv("calefactor-electrico.csv")
    unMenu = Menu()
    unMenu.ejecutarMenu(unManejadorCalefactores)