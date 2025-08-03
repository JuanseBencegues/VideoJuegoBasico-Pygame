import pygame
import constantes
from personaje import Personaje
from weapons import Weapon
from textos import DmgText
from items import Item
import os

#---------------- Funciones ----------------
def escalar_img(image, scale):
    """ Dada una imagen y valor, la imagen se escala al valor dado """
    w = image.get_width()
    h = image.get_height()
    n_image = pygame.transform.scale(image, (w*scale, h*scale))
    return n_image

def contar_elementos(directorio):
    """ Entrega la cantidad de elementos en el directorio dado"""
    return len(os.listdir(directorio))

def nombres_carpetas(directorio):
    """ Retorna una lista con el nombre de las carpertas en el directorio dado """
    return os.listdir(directorio)

def vida_jugador():
    c_mitad_dibujado = False
    for i in range(constantes.CANTIDAD_CORAZONES):
        if jugador.energia >=((i+1)*100 / constantes.CANTIDAD_CORAZONES):
            ventana.blit(corazon_lleno, (5+i*50,5))
        elif jugador.energia % 25 > 0 and not c_mitad_dibujado:
            ventana.blit(corazon_mitad, (5+i*50,5))
            c_mitad_dibujado = True
        else:
            ventana.blit(corazon_vacio,(5+i*50,5))

#---------------- Pantalla ----------------
#Inicia pygame
pygame.init()
#Inicia ventana
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)) 
#nombre de la ventana
pygame.display.set_caption("Juego")

#Fuente
font = pygame.font.Font("assets/fonts/m6x11.ttf",constantes.TAM_FUNTE)

#---------------- Animaciones ----------------
#Personaje
animaciones = []
for i in range (10):
    img = pygame.image.load(f"assets/images/characters/player/run_{i}.png")
    img = escalar_img(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)
#Salud
corazon_vacio = pygame.image.load("assets/images/items/hearts/heart_empty.png")
corazon_vacio = escalar_img(corazon_vacio, constantes.ESCALA_CORAZONES)

corazon_mitad = pygame.image.load("assets/images/items/hearts/heart_half.png")
corazon_mitad = escalar_img(corazon_mitad, constantes.ESCALA_CORAZONES)

corazon_lleno = pygame.image.load("assets/images/items/hearts/heart_full.png")
corazon_lleno = escalar_img(corazon_lleno, constantes.ESCALA_CORAZONES)

#Enemigos
directorio_enemigos = "assets/images/characters/enemies"
tipo_enemigos = nombres_carpetas(directorio_enemigos)
animaciones_enemigos = []
for eni in tipo_enemigos:
    lista_temp = []
    ruta_temp = f"assets/images/characters/enemies/{eni}"
    num_animaciones = contar_elementos(ruta_temp)
    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}/{eni}_{i+1}.png")
        if eni == "blood-demon":
            img_enemigo = escalar_img(img_enemigo, constantes.ESCALA_ENEMIGO)
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)

#Arma
imagen_ballesta = pygame.image.load("assets/images/weapons/crossbow.png")
imagen_ballesta = escalar_img(imagen_ballesta, constantes.ESCALA_ARMA)
#Flechas
imagen_balas = pygame.image.load("assets/images/weapons/arrow.png")
imagen_balas = escalar_img(imagen_balas, constantes.ESCALA_ARMA)

#Items
#Pocion
directorio_pociones = "assets/images/items/potions"
animaciones_pocion = []
for i in range(contar_elementos(directorio_pociones)):
    img_pocion = pygame.image.load(f"assets/images/items/potions/potion_{i+1}.png")
    img_pocion= escalar_img(img_pocion, constantes.ESCALA_POCION)
    animaciones_pocion.append(img_pocion)
#Monedas
directorio_monedas = "assets/images/items/coin"
animaciones_monedas = []
for i in range(contar_elementos(directorio_monedas)):
    img_moneda = pygame.image.load(f"assets/images/items/coin/coin_{i+1}.png")
    img_moneda = escalar_img(img_moneda, constantes.ESCALA_MONEDA)
    animaciones_monedas.append(img_moneda)


#---------------- Personajes ----------------

#Crear un jugador de la clase personaje
jugador  = Personaje(50,70,animaciones, 100)
#definir variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

#Crear un enemigo de la clase personaje
blood_demon = Personaje(400,400,animaciones_enemigos[0],100)
blood_demon_2 = Personaje(150,500,animaciones_enemigos[0],100)
flying_demon = Personaje(200,200, animaciones_enemigos[1],100)
flying_demon_2 = Personaje(300,80, animaciones_enemigos[1],100)
#Crear lista de enemigos
lista_enemigos = []
lista_enemigos.append(blood_demon)
lista_enemigos.append(blood_demon_2)
lista_enemigos.append(flying_demon)
lista_enemigos.append(flying_demon_2)

#---------------- Armas ----------------
#Crear un arma de la clase weapon
ballesta = Weapon(imagen_ballesta, imagen_balas)
#Critico
critico = False

#---------------- Items ----------------
moneda = Item(350, 25, 0, animaciones_monedas)
pocion = Item(450, 230, 1, animaciones_pocion)


#---------------- Grupos ----------------
#grupos de sprites
""" Utilizo estos grupos para los objetos de la misma clase 
    de los cuales podria haber mas de uno en pantalla """
grupo_balas = pygame.sprite.Group()
grupo_damage_text = pygame.sprite.Group()
grupo_items = pygame.sprite.Group()

grupo_items.add(moneda)
grupo_items.add(pocion)


#Controlar frame-rate
reloj = pygame.time.Clock()

run = True
#---------------- BUCLE DE JUEGO ----------------
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
    jugador.update()
    #Actualiza estado enemigos
    for ene in lista_enemigos:
        ene.update()
        #print(ene.energia)

    #Actualiza estado del arma
    bala = ballesta.update(jugador)
    if bala: 
        #Si hay una bala se agrega al grupo
        grupo_balas.add(bala)
    for bala in grupo_balas:
        damage, pos_damage, critico = bala.update(lista_enemigos)
        if damage:
            color = constantes.COLOR_GOLPE_CRITICO if critico else constantes.COLOR_GOLPE
            damage_text = DmgText(pos_damage.centerx, pos_damage.centery, int(damage), font, color)
            grupo_damage_text.add(damage_text) 
    #Actualiza daño
    grupo_damage_text.update()

    #Actualiza items
    grupo_items.update()

    #---------------- Dibujar ----------------
    # al jugador
    jugador.dibujar(ventana)
    # el arma
    ballesta.dibujar(ventana)
    # enemigos
    for ene in lista_enemigos:
        ene.dibujar(ventana)
    # balas
    for bala in grupo_balas:
        bala.dibujar(ventana)
    # corazones
    vida_jugador()
    # textos
    grupo_damage_text.draw(ventana)
    # items
    grupo_items.draw(ventana)

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