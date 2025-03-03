import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

  running = True
  while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    pygame.display.flip()

  pygame.quit()

if __name__ == "__main__":
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  main()