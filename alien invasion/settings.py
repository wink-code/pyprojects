class Settings:
    """ restore all the setting class in the games """
    def __init__(self):
        """initialize the setting of the game"""
        # creen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # the speed of the ship
        self.ship_speed = 1.5
        # bullet setting
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        