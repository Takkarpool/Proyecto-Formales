class Habitacion:
    """
    Clase que representa una habitación
    """
    def __init__(self, xInicial, yInicial ,ancho, alto, numero):
        """
        Constructor de una habitacion
        :param xInicial: posición x inicial del Habitación
        :param yFinal: posición y inicial del Habitación
        :param width: anchura del Habitación
        :param height: altura del Habitación
        :param numero: número de la habitación
        """
        self.x = xInicial
        self.y = yInicial
        self.alto = alto
        self.ancho = ancho
        self.numero = numero

    def __eq__(self, other):
        """
        Comparador de Habitaciones
        :param other: otra habitación
        :return: True si sin iguales y false si no lo son,
        ademas de la excepción NotImplemented si other no es una habitación
        """
        if not isinstance(other, Habitacion):
            return NotImplemented

        return self.x == other.x and self.y == other.y and self.alto == other.alto and self.ancho == other.ancho
