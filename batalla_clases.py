import random

class Personaje:

    #Constructor

    def __init__(self, nombre, clase):
        #Método constructor
        self.__nombre = nombre  #los guiones bajos hacen que el atributo sea privado
        self.__clase = clase
        self.__fuerza = 10 + random.randint(-5, 5)
        self.__defensa = 10 + random.randint(-5, 5)
        self.__vida_total = 100 + random.randint(-10, 10)
        self.__vida_restante = self.__vida_total
        self.__defendiendo = False

    #Métodos privados

    def __morir(self):      #los guiones bajos hacen que el método sea privado
        #Método que se ejecuta cuando el personaje muere
        print("El personaje", self.__nombre, "ha muerto")
        self.__vida_restante = 0

    #Getters y setters

    def get_nombre(self):
        #Método que devuelve el nombre del personaje
        return self.__nombre

    def esta_vivo(self):
        #Método que devuelve True si el personaje está vivo
        if self.__vida_restante > 0:
            return True
        else:
            return False

    def defender(self):
        #Método que se ejecuta cuando el personaje se defiende
        self.__defendiendo = True
    
    def quitar_defensa(self):
        #Método que se ejecuta cuando el personaje deja de defenderse
        self.__defendiendo = False

    def get_clase(self):
        #Método que devuelve la clase del personaje
        return self.__clase

    def get_fuerza(self):
        #Método que devuelve la fuerza del personaje
        return self.__fuerza

    def set_fuerza(self, fuerza):
        #Método que modifica la fuerza del personaje
        self.__fuerza = fuerza
    
    def get_defensa(self):
        #Método que devuelve la defensa del personaje
        return self.__defensa

    def set_defensa(self, defensa):
        #Método que modifica la defensa del personaje
        self.__defensa = defensa

    def get_defendiendo(self):
        #Método que devuelve True si el personaje se está defendiendo
        return self.__defendiendo

    #Métodos públicos

    def recibir_danio(self, daño):
        #Método que se ejecuta cuando el personaje recibe daño
        self.__vida_restante -= daño
        if not self.esta_vivo():
            self.__morir()

    def mostrar_atributos(self):
        #Método que muestra los atributos del personaje
        print("")
        print("Nombre:", self.__nombre)
        print("Clase:", self.__clase)
        print("Fuerza:", self.__fuerza)
        print("Defensa:", self.__defensa)
        self.mostrar_vida()
        print("")
        if self.__clase == "Mago":
            self.mostrar_mana()

    def mostrar_vida(self):
        #Método que muestra la vida del personaje
        print("Vida:", self.__vida_restante, "/", self.__vida_total)
        for punto_de_vida in range(0, self.__vida_total, 10):
            if punto_de_vida < self.__vida_restante:
                print("0 ", end="")
            else:
                print("O ", end="")      

    def atacar(self, enemigo):
        #Método que se ejecuta cuando el personaje ataca a otro
        if self.esta_vivo() and enemigo.esta_vivo():

            defendiendo = enemigo.get_defendiendo()

            d20 = random.randint(1, 20)

            if d20 == 20:
                d6 = random.randint(1, 6)
                daño = self.get_fuerza() * 2 + d6
                if defendiendo:
                    print("¡Golpe crítico de " + self.get_nombre() + " a " + enemigo.get_nombre() + " de", daño, "rompiendo su defensa!")
                else:
                    print("¡Golpe crítico de " + self.get_nombre() + " a " + enemigo.get_nombre() + " de", daño, "puntos de daño!")
            elif d20 in range(7, 20):
                if defendiendo:
                    if self.get_fuerza() > enemigo.get_defensa():
                        daño = self.get_fuerza() - enemigo.get_defensa()
                        print(self.get_nombre(), "ataca a", enemigo.get_nombre(), "y le hace", daño, "puntos de daño aunque este se defienda")
                    else:
                        daño = 0
                        print(self.get_nombre(), "ataca a", enemigo.get_nombre(), "pero su defensa es demasiado resistente y no le hace daño")
                else:
                    daño = self.get_fuerza()
                    print(self.get_nombre(), "ataca a", enemigo.get_nombre(), "y le hace", daño, "puntos de daño")
            elif d20 in range(2, 7):
                if defendiendo:
                    daño = 0
                    print(self.get_nombre(), "ataca a", enemigo.get_nombre(), "pero este lo esquiva completamente mientras se defiende")
                else:
                    if self.get_fuerza() > enemigo.get_defensa():
                        daño = self.get_fuerza() - enemigo.get_defensa()
                        print(self.get_nombre(), "ataca a", enemigo.get_nombre(), "y casi erra el golpe, pero al menos le hace", daño, "puntos de daño")
                    else:
                        daño = 0
                        print(self.get_nombre(), "ataca a", enemigo.get_nombre(), " y casi erra el golpe pero solo le llega a rasguñar la armadura")
            elif d20 == 1:
                daño = 0
                print(self.get_nombre(), "ataca a", enemigo.get_nombre(), "pero erra completamente y no le hace daño alguno")
                if defendiendo:
                    self.recibir_danio(enemigo.get_fuerza())
                    print(self.get_nombre(), "se hiere a sí mismo por atacar a", enemigo.get_nombre(), "que se estaba defendiendo y recibe", enemigo.get_fuerza(), "puntos de daño")

            enemigo.recibir_danio(daño)

class Mago(Personaje):

    #Constructor

    def __init__(self, nombre):
        #Método constructor
        super().__init__(nombre, "Mago")
        self.__mana_total = 40 + random.randint(-10, 10)
        self.__mana_restante = self.__mana_total

    #Getters y setters

    def mostrar_mana(self):
        #Método que muestra el mana del personaje
        print("Maná:", self.__mana_restante, "/", self.__mana_total)
        for punto_de_mana in range(0, self.__mana_total, 5):
            if punto_de_mana < self.__mana_restante:
                print("0 ", end="")
            else:
                print("O ", end="")

    def get_mana_restante(self):
        return self.__mana_restante

    def get_mana_total(self):
        return self.__mana_total

    def restar_mana(self, mana):
        self.__mana_restante -= mana

    #Métodos públicos

    def atacar(self, enemigo, hechizo):
        if self.esta_vivo() and enemigo.esta_vivo():
            if hechizo == 1:
                if self.get_mana_restante() >= 10:
                    self.restar_mana(10)
                    defendiendo = enemigo.get_defendiendo()
                    d20 = random.randint(1, 20)
                    if d20 == 20:
                        daño = 20 + random.randint(1, 6)
                        if defendiendo:
                            print("¡Golpe crítico con una bola de fuego de " + self.get_nombre() + " a " + enemigo.get_nombre() + " de", daño, "ignorando su defensa!")
                        else:
                            print("¡Golpe crítico de una bola de fuego de " + self.get_nombre() + " a " + enemigo.get_nombre() + " de", daño, "puntos de daño!")
                    elif d20 in range(7, 20):
                        if defendiendo:
                            if 20 > enemigo.get_defensa():
                                daño = 20 - enemigo.get_defensa()
                                print(self.get_nombre(), "lanza una bola de fuego", enemigo.get_nombre(), "y le hace", daño, "puntos de daño aunque este se defienda")
                            else:
                                daño = 0
                                print(self.get_nombre(), "lanza una bola de fuego a", enemigo.get_nombre(), "pero su defensa es demasiado resistente y solo le chamusca un poco la armadura")
                        else:
                            daño = 20
                            print(self.get_nombre(), "lanza una bola de fuego a", enemigo.get_nombre(), "y le hace", daño, "puntos de daño")
                    elif d20 in range(2, 7):
                        if defendiendo:
                            daño = 0
                            print(self.get_nombre(), "lanza una bola de fuego a", enemigo.get_nombre(), "pero este la esquiva completamente mientras se defiende")
                        else:
                            if 15 > enemigo.get_defensa():
                                daño = 15 - enemigo.get_defensa()
                                print(self.get_nombre(), "lanza una bola de fuego a", enemigo.get_nombre(), "y casi erra el golpe, pero al menos le hace", daño, "puntos de daño")
                            else:
                                daño = 0
                                print(self.get_nombre(), "lanza una bola de fuego a", enemigo.get_nombre(), " y casi erra el golpe pero solo le chamusca un poco la armadura")
                    elif d20 == 1:
                        daño = 0
                        print(self.get_nombre(), "lanza una bola de fuego a", enemigo.get_nombre(), "pero erra completamente y no le hace daño alguno")
                        if defendiendo:
                            self.recibir_danio(enemigo.get_fuerza())
                            print(self.get_nombre(), "se quema a sí mismo por atacar a", enemigo.get_nombre(), "que se estaba defendiendo y recibe 10 puntos de daño")
                            self.recibir_danio(10)
                    enemigo.recibir_danio(daño)
                else:
                    print(self.get_nombre(), "no tiene suficiente mana, atacará con su fuerza")
                    super().atacar(enemigo)
            
            elif hechizo == 2:
                if self.get_mana_restante() >= 7:
                    self.restar_mana(7)
                    daño = 15
                    print(self.get_nombre(), "lanza un rayo a", enemigo.get_nombre(), "y le hace", daño, "puntos de daño")
                    enemigo.recibir_danio(daño)
                else:
                    print(self.get_nombre(), "no tiene suficiente mana, atacará con su fuerza")
                    super().atacar(enemigo)
            elif hechizo == 3:
                super().atacar(enemigo)

class Guerrero(Personaje):

    #Constructor

    def __init__(self, nombre):
        #Método constructor
        super().__init__(nombre, "Guerrero")
        self.set_fuerza(self.get_fuerza() + random.randint(10, 15))
        self.set_defensa(self.get_defensa() + random.randint(10, 15))