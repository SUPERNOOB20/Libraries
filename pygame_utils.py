# Library with tools for pygame-ce.

import pygame
import adaptive_screensize_utils

pygame.init()

if (getattr(pygame, "IS_CE", False) != True):
    raise Warning("Your version of Pygame isn't CE. Please install pygame-ce with \033[92mpip install pygame-ce\033[00m\033[95m.\033[00m")


# Input: dict {handle: filename}
#
# anchor to set anchor
# image_size to set size
def creates_images(handle, image_size):
    
    created_images: dict = {}

    for key, value in args:

        # Matches user's screen resolution by default.
        if len(value) == 1:

            key_surf = pygame.image.load(value).convert_alpha()
            key_scaled_surf = pygame.transform.scale(surface = key_surf, size = (user_screen_width, user_screen_height))
            created_images[key] = key_scaled_surf


        else:

            key_surf = pygame.image.load(handle).convert_alpha()
            key_scaled_surf = pygame.transform.scale(surface = key_surf, size = (image_size[0], image_size[1]))
            created_images[key] = key_scaled_surf


    return created_images



# Input: dict {handle: filename}
# or
# Input: dict {handle: [filename, anchor, x, y]}
#
# anchor to set anchor
# image_size to set size
def creates_images_and_rects(*args, anchor, image_size):
    
    return



# Raises an exception if the input dict has len() == 0.
# Otherwise, calls "creates_images_and_rects()" (for _ in [])
# Returns a GroupSingle if the input dict has len() == 1.
# Returns a Group if the input dict has len() > 1
def creates_sprites(*args, **kwargs):
    class MySprite(pygame.sprite.Sprite):
        def __init__

    match len(args):
        case 0:
            raise Exception("Please provide an image for the sprite!")
        case 1:
            sprite_instance = pygame.sprite.GroupSingle()
        case 2:
            sprite_instance = pygame.sprite.Group()
    return sprite_instance