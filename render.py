from snake import Snake
import pygame

cell_size = 30

class Render:
    def __init__(self):
        self.screen = None
        self.cell_size = 16
        self.clock = None

    def render(self, snake_body, apple_location):
        if self.screen is None:
            pygame.init()
            self.screen = pygame.display.set_mode((16 * cell_size, 15 * cell_size))
            self.clock = pygame.time.Clock()
        self.screen.fill((0, 0, 0))

        # Draw apple
        pygame.draw.rect(self.screen, (255, 0, 0), (apple_location[0] * cell_size, apple_location[1] * cell_size, cell_size, cell_size))
        # Draw snake
        for segment in snake_body:
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))
            
        pygame.display.flip()
        self.clock.tick(30)
