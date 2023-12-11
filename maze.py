import pygame
import sys

OPEN = 1
BUSH = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class maze:
    def __init__(self):
        pass

    def run_game():
        pygame.init()

        screen = pygame.display.set_mode((900,900))
        pygame.display.set_caption('Maze')   

        player = pygame.Rect((200, 200, 50, 50))

        run = True
        while run:
            screen.fill((0,0,0))
            pygame.draw.rect(screen, RED, player)

            key = pygame.key.get_pressed()
            if key[pygame.K_a] == True:
                player.move_ip(-1, 0)
            elif key[pygame.K_d] == True:
                player.move_ip(1, 0)
            elif key[pygame.K_w] == True:
                player.move_ip(0, -1)
            elif key[pygame.K_s] == True:
                player.move_ip(0, 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        
            pygame.display.update()

        pygame.quit() 






if __name__ == "__main__":
    Maze = maze()
    maze.run_game()
