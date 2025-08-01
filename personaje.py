import pygame
import constantes

class Personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect( 0, 0 , constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE) #crea rectangulo donde (coordenada x, coord y, ancho, alto)
        self.forma.center = (x, y) #Cuando creo personaje, se inicia en las coordenadas dadas
    
    def movimiento(self, delta_x, delta_y):
            #moverse en horizontal
            self.forma.x = self.forma.x + delta_x
            #moverse en vertical
            self.forma.y = self.forma.y + delta_y
            
    def dibujar(self, interfaz):
        #dibujar rectangulo en la ventanda (interfaz) con el color y la forma 
        pygame.draw.rect(interfaz,constantes.COLOR_PERSONAJE,self.forma)
        