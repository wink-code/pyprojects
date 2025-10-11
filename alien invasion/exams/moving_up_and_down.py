import pygame
import sys
from pathlib import Path 

class updown_game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,900))
        self.bg_color = (255,255,255)
        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()
        self.bullet_allowed = 3

    def run_game(self):
        while True:
            self._get_event()
            self.ship.update()
            self._update_bullet()
            self._update_screen()
            

            
    def _get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if (len(self.bullets) < self.bullet_allowed and event.key == pygame.K_SPACE):
        # if event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_keyup_events(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    

class Bullet(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.bullet_color = (1,0,0)
        self.bullet_width = 10
        self.bullet_length = 10
        self.bullet_speed = 1

        self.rect = pygame.Rect(0,0,self.bullet_width,self.bullet_length)
        self.rect.midright = game.ship.rect.midright


    def update(self):
        self.rect.x += self.bullet_speed
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

class ship:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load(Path(__file__).parent / Path('ship.bmp'))
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1


    def blitme(self):
        self.screen.blit(self.image,self.rect)

if __name__ == '__main__':
    # print(__file__)
    game = updown_game()
    game.run_game()