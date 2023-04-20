from csv import reader
from .settings import tile_size
from os import walk
import pygame
import json

def import_character(path):
    surface_list = []
    for _, __, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf, (64, 54))
            surface_list.append(image_surf)

    return surface_list


def import_folder(path):
    surface_list = []
    for _, __, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list


def import_csv_layout(path):
    terrain_map = []
    with open(path) as dic:
        level = reader(dic, delimiter=',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * 64
            y = row * 64
            new_surf = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surf)

    return cut_tiles



def read_data():
    f = open('./data.json')
    data = json.load(f)
    f.close()
    return data


def write_data(val_type,value):
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data[val_type] = value
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


# def import_background(level):


