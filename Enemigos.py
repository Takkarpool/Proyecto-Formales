class Enemigo:
    """
        Clase que representa un enemigo del juego
    """
    def __init__(self, xInicial, yInicial, alto, ancho, llave):
        """
        Constructor del Enemigo
        :param xInicial: posición x inicial del Enemigo
        :param yFinal: posición y inicial del Enemig
        :param width: anchura del Enemigo
        :param height: altura del Enemigo
        :param llave: si el enemigo tiene llave o no
        """
        self.x = xInicial
        self.y = yInicial
        self.alto = alto
        self.ancho = ancho
        self.llave = llave