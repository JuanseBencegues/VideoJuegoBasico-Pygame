import pygame
import constantes
import math

class Weapon():
    def __init__(self, image):
        self.image_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.image_original, self.angulo)
        self.forma = self.imagen.get_rect()

    def update(self, personaje):
        #Centra el arma en el personaje
        self.forma.center = personaje.forma.center
        #posiciona el arma en el eje y
        self.forma.y = self.forma.y - personaje.forma.width / 4

        #Rotar arma
        if personaje.flip == False:
            self.forma.x = self.forma.x + personaje.forma.width / 2
            self.rotar_arma(False)
        if personaje.flip == True:
            self.forma.x = self.forma.x - personaje.forma.width / 2
            self.rotar_arma(True)
        
        #Mover arma con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))
        #Rango base (cuando mira a la derecha)
        min_angulo = constantes.MIN_ANGULO  
        max_angulo = constantes.MAX_ANGULO  
        #Si el personaje está mirando a la izquierda, reflejamos el cono
        if personaje.flip:
            # Reflejamos el ángulo: 180 - ángulo original
            self.angulo = 180 - self.angulo

            # También reflejamos el rango permitido
            min_angulo, max_angulo = 180 - max_angulo, 180 - min_angulo 

        # Aplico el límite
        if self.angulo < min_angulo:
            self.angulo = min_angulo
        elif self.angulo > max_angulo:
            self.angulo = max_angulo
        

    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.forma)
        #pygame.draw.rect(interfaz,constantes.COLOR_ARMA,self.forma,width=1)

    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.image_original, flip_x=True,flip_y=False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.image_original, flip_x=False, flip_y=False)   
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)