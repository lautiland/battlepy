import os

def main():
    opcion = ""
    while opcion != "3":
        opcion = input("""\n
    Bienvenido al simulador de batalla 
    1. Jugar PVE (Player vs Enviroment)
    2. Jugar PVP (Player vs Player)
    3. Salir 

    """)
        while opcion not in ["1", "2", "3"]:
            os.system("cls")
            print("\nOpcion invalida, intenta de nuevo")
            opcion = input("""\n
    Bienvenido al simulador de batalla 
    1. Jugar PVE (Player vs Enviroment)
    2. Jugar PVP (Player vs Player)
    3. Salir 

    """)
        if opcion == "1":
            os.system("cls")
            os.system("py batalla_pve.py")
            os.system("cls")
        elif opcion == "2":
            os.system("cls")
            os.system("py batalla_pvp.py")
            os.system("cls")
        elif opcion == "3":
            os.system("cls")
            print("\nGracias por jugar, hasta luego")
            os.system("pause")

main()