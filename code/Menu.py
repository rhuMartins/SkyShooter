#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, MENU_OPTION, COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, COLOR_BLACK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menuBG.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./assets/main-menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)

            overlay = pygame.Surface((self.rect.width, self.rect.height))
            overlay.set_alpha(40)
            overlay.fill((0, 0, 0))
            self.window.blit(overlay, (0, 0))

            self.menu_text(50, "Sky", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 65))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 95))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WINDOW_WIDTH / 2), 200 + 22 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WINDOW_WIDTH / 2), 200 + 22 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]

    # def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
    #     text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
    #     text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    #     text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    #     self.window.blit(source=text_surf, dest=text_rect)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Upheaval TT (BRK)", size=text_size)

        outline_color = COLOR_BLACK
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in offsets:
            outline_surf: Surface = text_font.render(text, True, outline_color).convert_alpha()
            outline_rect: Rect = outline_surf.get_rect(center=(text_center_pos[0] + dx, text_center_pos[1] + dy))
            self.window.blit(source=outline_surf, dest=outline_rect)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
