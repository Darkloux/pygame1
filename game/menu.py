import pygame
import sys
from game.tic_tac_toe import main

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 600, 600
BG_COLOR = (28, 170, 156)
TEXT_COLOR = (23, 145, 135)

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe - Menú')
screen.fill(BG_COLOR)

# Mostrar menú
def display_menu():
    font = pygame.font.Font(None, 80)
    title_text = font.render("Tic Tac Toe", True, TEXT_COLOR)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title_text, title_rect)

    font_small = pygame.font.Font(None, 50)
    play_text = font_small.render("Presiona ENTER para jugar", True, TEXT_COLOR)
    play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(play_text, play_rect)

    pygame.display.update()

# Bucle principal del menú
def menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                main()  # Llamar al juego principal

        screen.fill(BG_COLOR)
        display_menu()

if __name__ == '__main__':
    menu()
