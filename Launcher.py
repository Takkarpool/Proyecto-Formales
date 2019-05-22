import pygame as g
from GeneracionMapa import *
from Jugador import *

def inicializar():
    """
    Inicializa el mundo en 2D
    """

    #Escoger tamaño de la pantalla
    alto = 500
    ancho = 500

    #Iniciar el display
    g.init()
    pantalla: g.Surface = g.display.set_mode((alto, ancho))
    g.display.set_caption("Formales")

    #Sprite para posible juego
    jugador_sprite = g.sprite.Group()
    listade_todoslos_sprites = g.sprite.Group()

    # Velocidad del jugador
    vel = 5
    # Juego en Acción
    run = True
    #Generación del Mundo
    gen = GeneracionMapa(alto, ancho, 8)

    #Dibujar los elementos del Mapa
    jugador = dibujar(gen, pantalla, True)

    # Sprite del Jugador (en deusos)
    jugador_sprite.add(jugador)


    #Recargar la pantalla
    while run:
        # FPS
        g.time.delay(50)

        # Quitar el juego
        for event in g.event.get():
            if event.type == g.QUIT:
                run = False

        # Movimiento del Jugador
        keys = g.key.get_pressed()

        if keys[g.K_LEFT]:
            jugador.control(-vel, 0)

        if keys[g.K_RIGHT]:
            jugador.control(+vel, 0)

        if keys[g.K_UP]:
            jugador.control(0, -vel)

        if keys[g.K_DOWN]:
            jugador.control(0, +vel)

        # Dibujar los elementos del Mapa
        dibujar(gen, pantalla, False)

        #Recargar la Pnatalla
        g.display.update()

        #Gestión del Jugador
        jugador.update()
        jugador_sprite.update()
        jugador_sprite.draw(pantalla)

        g.display.flip()

    g.quit()

def dibujar(gen, pantalla, personaje):
    """
    Dibuja todos los elementos del mapa
    :param gen: generación del mapa con los elementos de este
    :param pantalla: pantalla donde puntar los elementos
    :return: void
    """
    dibujar_mapa(gen, pantalla)
    dibujarPuertas(gen, pantalla)
    dibujar_Tesoros(gen, pantalla)
    dibujar_Enemigos(gen, pantalla)
    if personaje:
        return dibujarPersonaje(gen)



def dibujar_mapa(gen, pantalla):
    """
    Dibuja las Habitaciones
    :param gen: generación del mapa con los elementos de este
    :param pantalla: pantalla donde puntar los elementos
    :return: Jugador
    """
    pantalla.fill((0, 0, 0))
    for i in gen.listaHabitaciones:
        g.draw.rect(pantalla, (255, 255, 0), (i.x, i.y, i.ancho, i.alto))


def dibujarPersonaje(gen):
    """
    Dibuja los Personajes
    :param gen: generación del mapa con los elementos de este
    :param pantalla: pantalla donde puntar los elementos
    :return: el personaje
    """

    return Jugador((gen.salaInicial.x+gen.salaInicial.ancho/2), (gen.salaInicial.y+gen.salaInicial.alto/2), 7, 7)

def dibujarPuertas(gen, pantalla):
    """
    Dibuja las Puertas del Mapa
    :param gen: generación del mapa con los elementos de este
    :param pantalla: pantalla donde puntar los elementos
    :return: void
    """

    for i in gen.puertas:
        if i.posicionHabitacion1 == 0:
            g.draw.rect(pantalla, (255, 0, 255), (i.habitacion1.x, i.habitacion1.y+i.habitacion1.alto/2, 10, 10))
            g.draw.rect(pantalla, (255, 0, 255), (i.habitacion2.x + i.habitacion2.ancho-1, i.habitacion2.y
                                                 + i.habitacion2.alto/2, -10, -10))
        elif i.posicionHabitacion1 == 1:
            g.draw.rect(pantalla, (255, 0, 255), (i.habitacion1.x + i.habitacion1.ancho/2, i.habitacion1.y, 10, 10))
            g.draw.rect(pantalla, (255, 0, 255), (i.habitacion2.x + i.habitacion2.ancho/2, i.habitacion2.y
                                                + i.habitacion2.alto, -10, -10))
        elif i.posicionHabitacion1 == 2:
            g.draw.rect(pantalla, (255, 0, 255), (i.habitacion1.x + i.habitacion1.ancho, i.habitacion1.y +
                                                i.habitacion1.alto/2, -10, -10))
            g.draw.rect(pantalla, (255, 0, 255), (i.habitacion2.x, i.habitacion2.y+i.habitacion2.alto/2, 10, 10))

        else:
            g.draw.rect(pantalla, (255, 0, 255), (i.habitacion2.x + i.habitacion2.ancho/2, i.habitacion2.y, 10, 10))
            g.draw.rect(pantalla, (255, 0, 255), (i.habitacion1.x + i.habitacion1.ancho/2, i.habitacion1.y
                                                + i.habitacion1.alto, -10, -10))


def dibujar_Enemigos(gen, pantalla):
    """
    Dibuja los enemigos
    :param gen: generación del mapa con los elementos de este
    :param pantalla: pantalla donde puntar los elementos
    :return: void
    """
    for i in gen.enemigos:
        if i.llave:
            g.draw.rect(pantalla, (100, 100, 255), (i.x, i.y, i.ancho, i.alto))
        else:
            g.draw.rect(pantalla, (255, 0, 0), (i.x, i.y, i.ancho, i.alto))

    g.draw.rect(pantalla, (100, 100, 255), (gen.listaHabitaciones[1].x + gen.listaHabitaciones[1].ancho/2-7,
                gen.listaHabitaciones[1].y + gen.listaHabitaciones[1].alto/2-7, 14, 14))


def dibujar_Tesoros(gen, pantalla):
    """
    Dibuja los Tesoros
    :param gen: generación del mapa con los elementos de este
    :param pantalla: pantalla donde puntar los elementos
    :return: void
    """

    for i in gen.tesoros:
        g.draw.rect(pantalla, (255, 100, 100), (i.x, i.y, i.ancho, i.alto))


if __name__ == "__main__":
    inicializar()
