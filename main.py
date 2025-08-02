import pygame
import constantes
from personaje import Personaje
from weapons import Weapon


pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)) #Inicia ventana
#nombre de la ventana
pygame.display.set_caption("Juego")

def escalar_img(image, scale):
    """ Dada una imagen y valor, la imagen se escala al valor dado """
    w = image.get_width()
    h = image.get_height()
    n_image = pygame.transform.scale(image, (w*scale, h*scale))
    return n_image


#Importar imagenes
#Personaje
animaciones = []
for i in range (10):
    img = pygame.image.load(f"assets/images/characters/player/run_{i}.png")
    img = escalar_img(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)
#Arma
imagen_ballesta = pygame.image.load("assets/images/weapons/crossbow.png")
imagen_ballesta = escalar_img(imagen_ballesta, constantes.ESCALA_ARMA)
#Flechas
imagen_balas = pygame.image.load("assets/images/weapons/arrow.png")
imagen_balas = escalar_img(imagen_balas, constantes.ESCALA_ARMA)

#Crear un jugador de la clase personaje
jugador  = Personaje(50,50,animaciones)
#Crear un arma de la clase weapon
ballesta = Weapon(imagen_ballesta, imagen_balas)

#Crear grupo de sprites
grupo_balas = pygame.sprite.Group()

#definir variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

#Controlar frame-rate
reloj = pygame.time.Clock()

run = True
while run:
    #determinar fps
    reloj.tick(constantes.FPS)
    #Fondo de la ventana
    ventana.fill(constantes.COLOR_FONDO)

    #Calcular movimiento jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #mover al jugador
    jugador.movimiento(delta_x, delta_y)

    #Actualiza estado del jugador
    jugador.update( )

    #Actualiza estado del arma
    bala = ballesta.update(jugador)
    if bala: 
        #Si hay una bala se agrega al grupo
        grupo_balas.add(bala)
    for bala in grupo_balas:
        bala.update()


   # print(grupo_balas)

    #Dibujar al jugador
    jugador.dibujar(ventana)
    #Dibujar el arma
    ballesta.dibujar(ventana)
    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)

    print(grupo_balas)


    #recorre los posibles distintos eventos que se ejecuten 
    for event in pygame.event.get(): #event.get entrega la lista de todos los eventos que pueden ocurrir
        if event.type == pygame.QUIT: 
            #event.type muestra que tipo de evento es 
            #pygame.QUIT accion de cerrar ventana (ej. click en la cruz)
            run = False
        #Cuando se precione una tecla
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: #Se presionó 'a'
                mover_izquierda = True
            if event.key == pygame.K_d: #Se presionó 'd'
                mover_derecha = True
            if event.key == pygame.K_w: #Se presionó 'w'
                mover_arriba = True
            if event.key == pygame.K_s: #Se presionó 's'
                mover_abajo = True
        #Cuando se suelte una tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: 
                mover_izquierda = False
            if event.key == pygame.K_d: 
                mover_derecha = False
            if event.key == pygame.K_w: 
                mover_arriba = False
            if event.key == pygame.K_s: 
                mover_abajo = False

    pygame.display.update() #refleja cambios

pygame.quit()