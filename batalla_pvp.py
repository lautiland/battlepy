import batalla_clases as cp
import random
import os

Personaje = cp.Personaje
Mago = cp.Mago
Guerrero = cp.Guerrero

def elegir_decision(n_turno, nombre_usuario):
    
    print("\nTurno:", n_turno, "de", nombre_usuario, "\n")
    decision = input("""
¿Que quieres hacer?
1. Atacar
2. Defender

""")
    while decision != "1" and decision != "2":
        os.system("cls")
        print("\nOpción no válida\n")
        decision = input("""
¿Que quieres hacer?
1. Atacar
2. Defender

""")
    return int(decision)

def elegir_clase():
    clase = input("""
¿Que clase quiere ser?
1. Mago
2. Guerrero

""")
    while clase != "1" and clase != "2":
        os.system("cls")
        print("\nOpción no válida\n")
        clase = input("""
¿Que clase quiere ser?
1. Mago
2. Guerrero

""")
    return int(clase)

def elegir_hechizo(usuario):
    print("¿Que hechizo quieres usar? ", end="")
    print("Tenés", usuario.get_mana_restante(), "/", usuario.get_mana_total(), "de maná")
    hechizo = input("""
1. Bola de fuego (daño: 20, coste: 10 de maná)
2. Rayo (daño: 15, coste: 7 de maná, ignora la defensa)
3. Atacar con fuerza

""")
    while hechizo not in ["1", "2", "3"]:
        os.system("cls")
        print("Opción no válida\n")
        print("¿Que hechizo quieres usar? ", end="")
        print("Tenés", usuario.get_mana_restante(), "/", usuario.get_mana_total(), "de maná")
        hechizo = input("""
1. Bola de fuego (daño: 20, coste: 10 de maná)
2. Rayo (daño: 15, coste: 10 de maná, ignora la defensa)
3. Atacar con fuerza

""")
    return int(hechizo)

def turno(usuario1, usuario2, n_turno):

    if n_turno % 2 == 0:

        os.system("cls")
        
        opcion_usuario1 = elegir_decision(n_turno, usuario1.get_nombre())   

        os.system("cls")

        if opcion_usuario1 == 1 and usuario1.get_clase() == "Mago":
            hechizo_usuario1 = elegir_hechizo(usuario1)

        os.system("cls")

        opcion_usuario2 = elegir_decision(n_turno, usuario2.get_nombre())

        os.system("cls")

        if opcion_usuario2 == 1 and usuario2.get_clase() == "Mago":
            hechizo_usuario2 = elegir_hechizo(usuario2)
    
    else:
            
            os.system("cls")
    
            opcion_usuario2 = elegir_decision(n_turno, usuario2.get_nombre())
    
            os.system("cls")
    
            if opcion_usuario2 == 1 and usuario2.get_clase() == "Mago":
                hechizo_usuario2 = elegir_hechizo(usuario2)
    
            os.system("cls")
    
            opcion_usuario1 = elegir_decision(n_turno, usuario1.get_nombre())
    
            os.system("cls")
    
            if opcion_usuario1 == 1 and usuario1.get_clase() == "Mago":
                hechizo_usuario1 = elegir_hechizo(usuario1)

    os.system("cls")

    print("\nTurno:", n_turno, "\n")

    usuario1.quitar_defensa()
    usuario2.quitar_defensa()

    print("Acciones:")

    if opcion_usuario1 == 1 and opcion_usuario2 == 1:
        if usuario1.get_clase() == "Mago":
            usuario1.atacar(usuario2, hechizo_usuario1)
        elif usuario1.get_clase() == "Guerrero":
            usuario1.atacar(usuario2)
        if usuario2.get_clase() == "Mago":
            usuario2.atacar(usuario1, hechizo_usuario2)
        elif usuario2.get_clase() == "Guerrero":
            usuario2.atacar(usuario1)
    elif opcion_usuario1 == 1 and opcion_usuario2 == 2:
        usuario2.defender()
        if usuario1.get_clase() == "Mago":
            usuario1.atacar(usuario2, hechizo_usuario1)
        elif usuario1.get_clase() == "Guerrero":
            usuario1.atacar(usuario2)
    elif opcion_usuario1 == 2 and opcion_usuario2 == 1:
        usuario1.defender()
        if usuario2.get_clase() == "Mago":
            usuario2.atacar(usuario1, hechizo_usuario2)
        elif usuario2.get_clase() == "Guerrero":
            usuario2.atacar(usuario1)
    elif opcion_usuario1 == 2 and opcion_usuario2 == 2:
        usuario1.defender()
        usuario2.defender()
        print("Ambos se han defendido, no pasa nada")

    print("\nEstadisticas:")

    usuario1.mostrar_atributos()
    print("\n")
    usuario2.mostrar_atributos()
    print("\n")

def crear_personaje(n_usuario):
    print("\nIngresa el nombre del personaje", n_usuario, ": ", end="")
    nombre = input("")
    clase = elegir_clase()

    if clase == 1:
        personaje = Mago(nombre)
    elif clase == 2:
        personaje = Guerrero(nombre)

    return personaje

def main():

    usuario1 = crear_personaje(1)
    os.system("cls")
    usuario2 = crear_personaje(2)

    os.system("cls")

    print("La batalla entre", usuario1.get_nombre(), "y", usuario2.get_nombre(), "ha comenzado")

    usuario1.mostrar_atributos()
    print("\n")
    usuario2.mostrar_atributos()
    print("\n")

    n_turno = 1


    while usuario1.esta_vivo() and usuario2.esta_vivo():
        os.system("pause")
        os.system("cls")
        turno(usuario1, usuario2, n_turno)
        n_turno += 1
    
    os.system("pause")
    os.system("cls")

    if usuario1.esta_vivo():
        os.system("cls")
        print("\n\nHas ganado la batalla")
    else:
        os.system("cls")
        print("\n\nHas perdido la batalla")
    
main()