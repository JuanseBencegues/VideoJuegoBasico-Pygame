import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        #Invertir horizontalmente al jugador
        self.flip = False

        self.animaciones = animaciones
        #Figura de la animacion mostrandose actualmente
        self.frame_index = 0
        #guarda los milisegundos desde que se inicia el juego
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        #Forma [HITBOX] del jugador
        self.forma = self.image.get_rect() #crea rectangulo donde (coordenada x, coord y, ancho, alto)
        #Posicion del jugador en la forma [HITBOX]
        self.forma.center = (x, y) #Cuando creo personaje, se inicia en las coordenadas dadas
    
    def movimiento(self, delta_x, delta_y):
        #Determina cuando el personaje se invierte
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False
        #moverse en horizontal
        self.forma.x = self.forma.x + delta_x
        #moverse en vertical
        self.forma.y = self.forma.y + delta_y

    def update(self):
        #tiempo antes de cambiar frame de animacion (en miliseg)
        cooldown_animacion = 75
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            #tiempo actual - tiempo desde que se inicio el juego >= ...
            #Avanza al siguiente frame de animacion
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0


    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, flip_y=False)
        #Dibuja imagen del personaje
        interfaz.blit(imagen_flip, self.forma)
        #dibujar rectangulo en la ventanda (interfaz) con el color y la forma [HITBOX]
        #pygame.draw.rect(interfaz,constantes.COLOR_PERSONAJE,self.forma,width=1)
        