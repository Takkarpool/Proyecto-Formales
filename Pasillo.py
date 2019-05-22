class Pasillo:
    """
        Clase que representa un Pasillo
    """
    def __init__(self, xInicial, yInicial ):
        """
        Constructor del pasillo
        :param xInicial: posición x inicial
        :param yInicial: poisición y inicial
        """
        self.xInicial = xInicial
        self.yInicial = yInicial

    def __eq__(self, other):
        """
        Comparador de pasillos
        :param other: otro pasillo a comparar
        :return: True si sin iguales y false si no lo son,
        ademas de la excepción NotImplemented si other no es un pasillo
        """
        if not isinstance(other, Pasillo):
            return NotImplemented

        return self.x == other.x and self.y == other.y and self.alto == other.alto and self.ancho == other.ancho
