import pygame
from itertools import product


def start_screen():


    background_image = pygame.image.load('data/fon.jpg')
    background_image = pygame.transform.scale(background_image, size)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        screen.fill('black')
        screen.blit(background_image, (0, 0))
        pygame.display.flip()


Tile_size = 50


class Tile(pygame.sprite.Sprite):
    type2image = {'.': pygame.transform.scale(pygame.image.load('data/grass.png'), (Tile_size, Tile_size)),
                  '#': pygame.transform.scale(pygame.image.load('data/box.png'), (Tile_size, Tile_size))}

    def __init__(self, pos, type, *groups):
        super().__init__(*groups)
        self.image = Tile.type2image[type]
        self.rect = self.image.get_rect().move(pos)


def load_map(path):
    with open(path, mode='r') as file:
        return [list(row.rstrip('\n')) for row in file]


def generate(map):
    tile_group = pygame.sprite.Group()
    for i, j in product(range(len(map)), range(len(map[0]))):
        if map[i][j] == '@':
            Tile((j * Tile_size, i * Tile_size), '.', tile_group)
        else:
            Tile((j * Tile_size, i * Tile_size), map[i][j], tile_group)
    return tile_group


pygame.init()
size = (800, 600)
running = True
screen = pygame.display.set_mode(size)

start_screen()
text_level = generate(load_map('data/map.txt'))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')
    text_level.draw(screen)
    pygame.display.flip()
