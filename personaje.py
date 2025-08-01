import pygame
import constantes

class Personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect( 0, 0 , constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE) #crea rectangulo donde (coordenada x, coord y, ancho, alto)
        self.forma.center = (x, y) #Cuando creo personaje, se inicia en las coordenadas dadas
    
    def dibujar(self, interfaz):
        #dibujar rectangulo en la ventanda (interfaz) con el color y la forma 
        pygame.draw.rect(interfaz,constantes.COLOR_PERSONAJE,self.forma)
        