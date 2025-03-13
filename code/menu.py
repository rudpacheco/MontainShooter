#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.font = pygame.font.SysFont('Arial', 36)  # Escolha uma fonte e tamanho

    def draw_text(self, text, color, x, y):
        """Função auxiliar para desenhar texto."""
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.window.blit(text_surface, text_rect)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # --- Inserção de texto ---
            self.draw_text("Mountain", (255, 128, 0), 100, 50)  # Título
            self.draw_text("Pressione ESPAÇO para começar", (255, 255, 255), 100, 150)
            self.draw_text("ESC para sair", (255, 255, 255), 100, 200)
            # --- Fim inserção de texto ---

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Aqui você colocaria a lógica para iniciar o jogo
                        print("Jogo iniciado!")
                        return  # Sai do loop do menu e retorna
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((800, 600))  # Defina o tamanho da janela
    pygame.display.set_caption("Meu Jogo")  # Defina o título da janela
    menu = Menu(window)
    menu.run()
