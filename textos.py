import pygame.sprite
import constantes

class DmgText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, font, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(damage), True, color).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.tiempo_inicio = pygame.time.get_ticks()
        self.duracion = constantes.DURACION_TEXTO_HIT 

    def update(self):
        self.rect.y -= 1  # velocidad fija
        tiempo_actual = pygame.time.get_ticks() - self.tiempo_inicio
        alpha = max(255 - int((tiempo_actual / self.duracion) * 255), 0)
        self.image.set_alpha(alpha)

        if tiempo_actual > self.duracion:
            self.kill()