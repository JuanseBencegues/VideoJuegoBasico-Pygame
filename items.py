import pygame.sprite
import constantes

""" La clase importada sprite YA TIENE SU PROPIO UPDATE """
class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type, animation_list):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type # 0 = monedas, 1 = pociones
        self.animation_list = animation_list
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self, personaje):
        #Comprobar colision
        if self.rect.colliderect(personaje.forma):
            #monedas
            if self.item_type == 0:
                personaje.score += 1
            elif self.item_type == 1: 
                personaje.energia += constantes.CURACION_POCION
                if personaje.energia > 100:
                    personaje.energia = 100
            self.kill()

        cooldown_animacion = 100
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0
