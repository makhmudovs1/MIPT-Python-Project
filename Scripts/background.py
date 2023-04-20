import pygame
from settings import vertical_tile_number, tile_size, screen_width,screen_height



class background:
    def __init__(self, horizon, style='level'):
        self.top = pygame.image.load('./graphics/bg/1.png').convert()
        self.bottom = pygame.image.load('./graphics/bg/2.png').convert()
        self.middle = pygame.image.load('./graphics/bg/3.png').convert()
        self.horizon = horizon

        # self.style = style
        # if self.style == 'overworld':
        #     palm_surfaces = import_folder('../graphics/overworld/palms')
        #     self.palms = []
        #
        #     for surface in [choice(palm_surfaces) for image in range(10)]:
        #         x = randint(0, screen_width)
        #         y = (self.horizon * tile_size) + randint(50, 100)
        #         rect = surface.get_rect(midbottom=(x, y))
        #         self.palms.append((surface, rect))
        #
        #     cloud_surfaces = import_folder('../graphics/overworld/clouds')
        #     self.clouds = []
        #
        #     for surface in [choice(cloud_surfaces) for image in range(10)]:
        #         x = randint(0, screen_width)
        #         y = randint(0, (self.horizon * tile_size) - 100)
        #         rect = surface.get_rect(midbottom=(x, y))
        #         self.clouds.append((surface, rect))

    def draw(self, surface):
        for row in range(vertical_tile_number):
            y = row * tile_size
            if row < self.horizon:
                surface.blit(self.top, (0, y))
            elif row == self.horizon:
                surface.blit(self.middle, (0, y))
            else:
                surface.blit(self.bottom, (0, y))