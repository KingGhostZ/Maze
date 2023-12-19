import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        # Sprite setup
        self.create_map()

    def create_map(self):
        for indexy, row in enumerate(gameBoard):
            for indexx, column in enumerate(row):
                x = indexx * tileSize
                y = indexy * tileSize
                if column == "X":
                    Tile((x,y), [self.visible_sprites, self.obstacle_sprites])
                if column == "P":
                    self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)


    def run(self):
        # Update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group): # Camera movement
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)

    def custom_draw(self, player):

        # Getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)