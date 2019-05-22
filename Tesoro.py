class Tesoro:
    """
        Clase que representa un Tesoro
    """
    def __init__(self, xInicial, yInicial, alto, ancho):
        """
        Constructor del Tesoro
        :param xInicial: posición x inicial del Tesoro
        :param yFinal: posición y inicial del Tesoro
        :param width: anchura del Tesoro
        :param height: altura del Tesoro
        """
        self.x = xInicial
        self.y = yInicial
        self.alto = alto
        self.ancho = ancho