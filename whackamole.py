import random

import pygame
from pygame import MOUSEBUTTONDOWN


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")

        screen = pygame.display.set_mode((640, 512))

        clock = pygame.time.Clock()

        running = True
        mole_col = 0
        mole_row = 0

        screen.fill("light green")
        for vert in range(1, 21):
            pygame.draw.line(screen, "black", (vert * 32, 0), (vert * 32, 512))
        for horizontal in range(1, 17):
            pygame.draw.line(screen, "black", (0, horizontal * 32), (640, horizontal * 32))

        #screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos

                    row = y//32
                    col = x//32
                    print(col,row)
                    if row == mole_row and col == mole_col:
                        mole_col = random.randrange(0,640)//32
                        mole_row = random.randrange(0,512)//32
                        print(mole_col, " " , mole_row)
            screen.fill("light green")
            for vert in range(1, 21):
                pygame.draw.line(screen, "black", (vert * 32, 0), (vert * 32, 512))
            for horizontal in range(1, 17):
                pygame.draw.line(screen, "black", (0, horizontal * 32), (640, horizontal * 32))
            screen.blit(mole_image,mole_image.get_rect(topleft = (mole_col*32,mole_row*32)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
