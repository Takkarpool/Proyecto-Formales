import random
from Habitacion import *
from Pasillo import *
from Puerta import *
from Enemigos import *
from Tesoro import *

class GeneracionMapa:
    """
    Clase que realiza la generación del mapa
    """
    def __init__(self, alto, ancho, numHabitaciones):
        """
        Constructor del mapa
        :param alto: alto del panel de pantalla
        :param ancho: ancho del panel de la pantalla
        """
        self.alto = alto
        self.ancho = ancho
        self.listaHabitaciones = []
        self.puertas = []
        self.enemigos = []
        self.tesoros = []
        self.minTamAlto = 0.10 * alto
        self.maxTamAlto = 0.25 * alto
        self.minTamAncho = 0.10 * ancho
        self.maxTamAncho = 0.25 * ancho

        self.creacionHabitaciones(numHabitaciones)
        self.generar_puertas()
        self.generar_Enemigos_Tesoros()

    def creacionHabitaciones(self, numeroHab):
        """
        Creación de habitaciones mediante grmáticas
        :param numeroHab: número de habitaciones del mapa
        :return: void
        """
        i = 0
        while numeroHab != 0:

            hab = Habitacion(random.randint(1, self.ancho), random.randint(1, self.alto),
                             random.randint(self.minTamAncho, self.maxTamAncho+1),
                             random.randint(self.minTamAlto, self.maxTamAlto+1),i)
            if self.comprobarColision(hab):
                self.listaHabitaciones.append(hab)
                numeroHab -= 1
                i += 1
        self.salaInicialYFinal()

    def comprobarColision(self, habitacion: Habitacion) -> bool:
        """
        Comprobar colisión de las habitaciones
        :param habitacion: habitación a comprobar
        :return: True si no colisionan y False si colisiona
        """
        if habitacion.alto+habitacion.y >= self.alto:
            return False
        if habitacion.ancho+habitacion.x >= self.ancho:
            return False
        for ha in self.listaHabitaciones:
            dx = min(ha.x+ha.ancho, habitacion.x+habitacion.ancho) - max(ha.x, habitacion.x)
            dy = min(ha.y+ha.alto, habitacion.y+habitacion.alto) - max(ha.y, habitacion.y)
            if (dx >= 0) and (dy >= 0):
                return False
        return True

    def conectarSalas(self):
        """
        Conectar salas mediante pasillos (en desuso)
        :return: lista de los pasillos
        """
        listaConectados = ([False for i in self.listaHabitaciones])
        listaPasillos = []
        hab_dic = {}
        for i in range(0, len(self.listaHabitaciones)-1):
            hab1: Habitacion = self.listaHabitaciones[i]
            hab2: Habitacion = self.listaHabitaciones[i+1]
            if hab2.x > hab1.x:
                inicialX = hab1.x+hab1.ancho
                inicialY = random.randint(hab1.y, hab1.y+hab1.alto)
                if hab2.y > hab1.y:
                    finalX = random.randint(hab2.x, hab2.x+hab2.ancho)
                    finalY = hab2.y+hab2.alto
                else:
                    finalX = random.randint(hab2.x, hab2.x + hab2.ancho)
                    finalY = hab2.y

            else:
                inicialX = hab1.x
                inicialY = random.randint(hab1.y, hab1.y + hab1.alto)
                if hab2.y > hab1.y:
                    finalX = random.randint(hab2.x, hab2.x + hab2.ancho)
                    finalY = hab2.y + hab2.alto
                else:
                    finalX = random.randint(hab2.x, hab2.x + hab2.ancho)
                    finalY = hab2.y

            listaPasillos.append([inicialX, inicialY, finalX, finalY])

        return listaPasillos

    def crear_pasillos(self):
        """
        Cración de los pasillos del juego (en desuso)
        :return: lista de pasillos
        """
        pasillos = []
        for i in range(0, len(self.listaHabitaciones)):
            for j in self.listaHabitaciones:
                if not j == self.listaHabitaciones[i]:
                    adj_rows, adj_cols = self.son_adyacentes(self.listaHabitaciones[i], j)

                    if len(adj_rows) != 0 and len(adj_cols) != 0:
                        pasillos.append(Pasillo(adj_cols, adj_rows))

        return pasillos

    def son_adyacentes(self, habitacion1: Habitacion, habitacion2: Habitacion):
        """
        Comprobación de que dos habitaciones son adjacentes (en desuso)
        :param habitacion1: primera habitación
        :param habitacion2: segunda habitación
        :return: las habitaciones contiuas
        """
        adj_rows = []
        adj_cols = []
        for r in range(habitacion1.y, habitacion1.y + habitacion1.alto):
            if habitacion2.y <= r < habitacion2.y + habitacion2.alto:
                adj_rows.append(r)

        for c in range(habitacion1.x, habitacion1.x + habitacion1.ancho):
            if habitacion2.x <= c < habitacion2.x + habitacion2.ancho:
                adj_cols.append(c)

        if len(adj_rows) != 0:
            if habitacion1.x > habitacion2.x:
                adj_cols.append(habitacion2.x+habitacion2.ancho)
                adj_cols.append(habitacion1.x)
            else:
                adj_cols.append(habitacion1.x + habitacion1.ancho)
                adj_cols.append(habitacion2.x)


        if len(adj_cols) != 0 and len(adj_rows) == 0:
            if habitacion1.y > habitacion2.y:
                adj_rows.append(habitacion2.y + habitacion2.alto)
                adj_rows.append(habitacion1.y)
            else:
                adj_rows.append(habitacion1.y + habitacion1.alto)
                adj_rows.append(habitacion2.y)

        return adj_rows, adj_cols

    def salaInicialYFinal(self):
        """
        Selección de la habitación Inicial y Final
        :return: void
        """
        self.salaInicial = self.listaHabitaciones[0]
        self.salaFinal = self.listaHabitaciones[1]

    def generar_puertas(self):
        """
        Generación de las puertas
        :return: void
        """
        posicion_puerta = random.uniform(0, 1)

        #Puerta final
        self.puertas.append(Puerta(self.listaHabitaciones[1],self.listaHabitaciones[random.randint(2,
                                    len(self.listaHabitaciones)-1)], self.posicionPuerta(posicion_puerta)))

        #Puerta inicial
        posicion_puerta = random.uniform(0, 1)
        self.puertas.append(
            Puerta(self.listaHabitaciones[0], self.listaHabitaciones[random.randint(2,
                                    len(self.listaHabitaciones) - 1)],self.posicionPuerta(posicion_puerta)))

        """
            Aquí definirías como poner las puertas si tienes un grafo de las salas por ejemplo """

        # Generación del resto de puertas
        for i in range(0,len(self.listaHabitaciones)-3):
            posicion_puerta = random.uniform(0, 1)
            habitacion1 = self.listaHabitaciones[random.randint(2, len(self.listaHabitaciones) - 1)]
            habitacion2 = self.listaHabitaciones[random.randint(2, len(self.listaHabitaciones) - 1)]

            # Comprobación de colisión
            while (not self.colisiona_puerta(habitacion1, posicion_puerta) and
                   not self.colisiona_puerta(habitacion2, posicion_puerta) ):
                posicion_puerta = random.uniform(0, 1)
                habitacion1 = self.listaHabitaciones[random.randint(2, len(self.listaHabitaciones) - 1)]
                habitacion2 = self.listaHabitaciones[random.randint(2, len(self.listaHabitaciones) - 1)]

            self.puertas.append(Puerta(habitacion1, habitacion2, self.posicionPuerta(posicion_puerta)))
        # Generar puertas en habitaciones sin puertas
        self.salasSinConectar()

    def salasSinConectar(self):
        """
        Conecta las salas sin puertas
        :return: void
        """
        habitaciones = []
        for i in self.puertas:
            habitaciones.append(i.habitacion1.numero)
            habitaciones.append(i.habitacion2.numero)

        # Mirar todas la habitaciones
        for i in range(2, len(self.listaHabitaciones)):
            # Si no tienen las habitaciones en la lista implica que no tienen puerta y hay que generar la puerta
            if i not in habitaciones:
                habitacion1 = self.listaHabitaciones[i]
                posicion_puerta = random.uniform(0, 1)
                habitacion2 = self.listaHabitaciones[random.randint(2, len(self.listaHabitaciones) - 1)]

                while (not self.colisiona_puerta(habitacion1, posicion_puerta) and
                       not self.colisiona_puerta(habitacion2, posicion_puerta)):
                    posicion_puerta = random.uniform(0, 1)
                    habitacion2 = self.listaHabitaciones[random.randint(2, len(self.listaHabitaciones) - 1)]

                self.puertas.append(Puerta(habitacion1, habitacion2, self.posicionPuerta(posicion_puerta)))



    def posicionPuerta(self, posicionPuerta):
        """
        Determina la posición de la puerta en la sala
        :param posicionPuerta: posición en probabilidad de la puerta
        :return: 0->izquierda, 1->arriba, 2->derecha, 3->abajo
        """
        if posicionPuerta < 0.25 :
            return 0
        elif posicionPuerta >= 0.25 and posicionPuerta < 0.50 :
            return 1
        elif posicionPuerta >= 0.50 and posicionPuerta < 0.75:
            return 2
        else:
            return 3

    def colisiona_puerta(self, habitacion, posicion):
        """
        Comprueba si hay puertas que colisionan
        :param habitacion: habitación de la puerta ha comprobar
        :param posicion: posición de la puerta
        :return: False si colisiona y True sui no colisiona
        """
        for i in self.puertas:
            if i.habitacion1 == habitacion:
                if posicion == i.posicionHabitacion1:
                    return False
            elif i.habitacion2 == habitacion:
                if posicion == i.posicionHabitacion1:
                    return False
        return True

    def generar_Enemigos_Tesoros(self):
        """
        Generar Enemigos y Tesoros de manera aleatoria
        :return: void
        """
        for i in range(2, len(self.listaHabitaciones)):

            """
                Aquí definirías como poner los enemigos si tienes un gráfo de enemigos etc
                mirando las puertas y poniendo enemigo o no
            """

            enemigoOTesoro = random.uniform(0, 1)
            # Probabilidad de que halla tesoro o enemigo
            if enemigoOTesoro <= 0.80:
                # Sala Enemigo
                llave = random.uniform(0, 1)
                # Probabilidad de poner llave a un enemigo
                if llave > 0.9:
                    self.enemigos.append(Enemigo(self.listaHabitaciones[i].x+self.listaHabitaciones[i].ancho/2,
                                           self.listaHabitaciones[i].y+self.listaHabitaciones[i].alto/2,
                                           7, 7, True))
                else:
                        self.enemigos.append(Enemigo( self.listaHabitaciones[i].x + self.listaHabitaciones[i].ancho/2,
                                            self.listaHabitaciones[i].y + self.listaHabitaciones[i].alto/2,
                                            7, 7, False))

            else:
                # Sala Tesoro
                self.tesoros.append(Tesoro(self.listaHabitaciones[i].x + self.listaHabitaciones[i].ancho / 2,
                                           self.listaHabitaciones[i].y + self.listaHabitaciones[i].alto / 2, 8, 8))
