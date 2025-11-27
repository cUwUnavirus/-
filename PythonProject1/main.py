import pygame

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
size = [600, 800]
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
MARGIN = 1
COUNT = 20

screen = pygame.display.set_mode(size)
pygame.display.set_caption("zmey")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    for row in range(COUNT):
        for column in range(COUNT):
            if (row+column)%2==0:
                color = BLUE
            else:
                color = WHITE

            pygame.draw.rect(screen,color, [10+column*SIZE_BLOCK+MARGIN*(column+1),20+row*SIZE_BLOCK+MARGIN*(row+1) ,SIZE_BLOCK,SIZE_BLOCK])

    pygame.display.flip()
