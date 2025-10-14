import pygame

class GameStats:
    """ follow the statistic infos in games"""
    def __init__(self,ai_game):
        """initialize the statistic"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        with open(self.settings.high_score_path) as f:
            self.high_score = int(f.read())

    def reset_stats(self):
        """initialize the statistic that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
