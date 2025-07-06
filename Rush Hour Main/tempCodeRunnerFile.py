import os
import pygame
# Load map buttons images
map_buttons_dir = "./assets/MapButtons"
map_button_default_imgs = []
map_button_selected_imgs = []

for fname in os.listdir(map_buttons_dir):
    if "(A)" in fname and fname.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = pygame.image.load(os.path.join(map_buttons_dir, fname))
        map_button_default_imgs.append(img)
    if "(B)" in fname and fname.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = pygame.image.load(os.path.join(map_buttons_dir, fname))
        map_button_selected_imgs.append(img)
print (map_button_default_imgs)
print (map_button_selected_imgs)