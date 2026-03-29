#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_YELLOW, MENU_OPTION, C_WHITE, C_BLACK, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)

        while True:
            # Draw background
            self.window.blit(source=self.surf, dest=self.rect)

            # Game Title with shadow effect
            self.menu_text(50, "Don't Pass", C_BLACK, ((WIN_WIDTH / 2), 195))
            self.menu_text(50, "Don't Pass", C_WHITE, ((WIN_WIDTH / 2), 185))
            self.menu_text(50, "Me By", C_BLACK, ((WIN_WIDTH / 2), 245))
            self.menu_text(50, "Me By", C_WHITE, ((WIN_WIDTH / 2), 235))

            # Instructions
            self.menu_text(14, "USE W, D, S, A TO FLY", C_WHITE, (WIN_WIDTH - 90, WIN_HEIGHT - 20))
            self.menu_text(14, "PRESS SPACE TO SHOOT", C_WHITE, (90, WIN_HEIGHT - 20))

            # Menu options
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, f" {MENU_OPTION[i]} ", C_YELLOW, ((WIN_WIDTH / 2), 360 + 35 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 360 + 35 * i))

            self.menu_text(15, "Press ESC to quit", C_WHITE, ((WIN_WIDTH / 7), WIN_HEIGHT - 835))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)