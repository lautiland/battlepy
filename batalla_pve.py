import batalla_clases as cp
import random
import os

Personaje = cp.Personaje
Mago = cp.Mago
Guerrero = cp.Guerrero

def elegir_decision():
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
¿Que clase quieres ser?
1. Mago
2. Guerrero

""")
    while clase != "1" and clase != "2":
        os.system("cls")
        print("\nOpción no válida\n")
        clase = input("""
¿Que clase quieres ser?
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
        print("¿Que hechizo quieres usar? ", end="")
        print("Tenés", usuario.get_mana_restante(), "/", usuario.get_mana_total(), "de maná")
        hechizo = input("""
1. Bola de fuego (daño: 20, coste: 10 de maná)
2. Rayo (daño: 15, coste: 10 de maná, ignora la defensa)
3. Atacar con fuerza

""")
    return int(hechizo)

def turno(usuario, enemigo, n_turno):
    
    opcion_usuario = elegir_decision()
    opcion_enemigo = random.randint(1, 2)

    os.system("cls")

    if opcion_usuario == 1 and usuario.get_clase() == "Mago":
        hechizo_usuario = elegir_hechizo(usuario)
    if opcion_enemigo == 1 and enemigo.get_clase() == "Mago":
        hechizo_enemigo = random.randint(1, 3)

    os.system("cls")

    print("\nTurno:", n_turno, "\n")

    usuario.quitar_defensa()
    enemigo.quitar_defensa()

    print("Acciones:")

    if opcion_usuario == 1 and opcion_enemigo == 1:
        if usuario.get_clase() == "Mago":
            usuario.atacar(enemigo, hechizo_usuario)
        elif usuario.get_clase() == "Guerrero":
            usuario.atacar(enemigo)
        if enemigo.get_clase() == "Mago":
            enemigo.atacar(usuario, hechizo_enemigo)
        elif enemigo.get_clase() == "Guerrero":
            enemigo.atacar(usuario)
    elif opcion_usuario == 1 and opcion_enemigo == 2:
        enemigo.defender()
        if usuario.get_clase() == "Mago":
            usuario.atacar(enemigo, hechizo_usuario)
        elif usuario.get_clase() == "Guerrero":
            usuario.atacar(enemigo)
    elif opcion_usuario == 2 and opcion_enemigo == 1:
        usuario.defender()
        if enemigo.get_clase() == "Mago":
            enemigo.atacar(usuario, hechizo_enemigo)
        elif enemigo.get_clase() == "Guerrero":
            enemigo.atacar(usuario)
    elif opcion_usuario == 2 and opcion_enemigo == 2:
        usuario.defender()
        enemigo.defender()
        print("Ambos se han defendido, no pasa nada")

    print("\nEstadisticas:")

    usuario.mostrar_atributos()
    print("\n")
    enemigo.mostrar_atributos()
    print("\n")

def crear_personaje(nombre = None, clase = None):
    if nombre == None:
        nombre = input("\nIngresa el nombre de tu personaje: ")
    if clase == None:
        clase = elegir_clase()
    if clase == 1:
        personaje = Mago(nombre)
    elif clase == 2:
        personaje = Guerrero(nombre)

    return personaje

def main():
    
    nombres = ["Gandalf", "Aragorn", "Legolas", "Gimli", "Frodo", "Sam", "Merry", "Pippin", "Boromir", "Gollum"]

    usuario = crear_personaje()
    enemigo = crear_personaje(random.choice(nombres), random.randint(1, 2))

    os.system("cls")

    print("La batalla entre", usuario.get_nombre(), "y", enemigo.get_nombre(), "ha comenzado")

    usuario.mostrar_atributos()
    print("\n")
    enemigo.mostrar_atributos()
    print("\n")

    n_turno = 1

    while usuario.esta_vivo() and enemigo.esta_vivo():
        os.system("pause")
        os.system("cls")
        print("\nTurno:", n_turno)
        turno(usuario, enemigo, n_turno)
        n_turno += 1
    
    os.system("pause")
    os.system("cls")

    if usuario.esta_vivo():
        os.system("cls")
        print("\n\nHas ganado la batalla")
    else:
        os.system("cls")
        print("\n\nHas perdido la batalla")
    
main()