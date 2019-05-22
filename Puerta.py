class Puerta:
    """
        Clase que representa una Puerta
    """
    def __init__(self, habitacion1, habitacion2, posicionHabitacion1):
        """
        Constructor de la puerta
        :param habitacion1: primera habitación involucrada
        :param habitacion2: segunda habitación involucrada
        :param posicionHabitacion1: posición de la puerta en la primera habitación: 0-> izquierda,
                                    1-> arriba, 2-> derecha, 3->abajo
        """
        self.habitacion1 = habitacion1
        self.habitacion2 = habitacion2
        self.posicionHabitacion1 = posicionHabitacion1