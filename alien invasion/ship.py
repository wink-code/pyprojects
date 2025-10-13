import pygame


class Ship(pygame.sprite.Sprite):
    """ class that manage the ships """
    def __init__(self, ai_game):
        """ initialize the ship and set its location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # loading the picture of the ship and get its outer rectangle
        self.image = pygame.image.load(r'images/ship.bmp')
        self.rect = self.image.get_rect()

        # put every ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # put the float data in the attribute 'x' in ship
        self.x = float(self.rect.x)


        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ move the location of the ship according to the moving flag"""
        # update the ship instead of the rect.x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            # self.rect.x -= 1
            self.x -= self.settings.ship_speed  
        
        self.rect.x = self.x

    def blitme(self):
        """ draw the ship at the location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ put the ship at the bottom center of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)