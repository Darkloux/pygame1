import pygame

# Colores
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
LINE_WIDTH = 15
CIRCLE_RADIUS = 100
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

def draw_lines():
    for row in range(1, 3):
        pygame.draw.line(pygame.display.get_surface(), LINE_COLOR, (0, row * 200), (600, row * 200), LINE_WIDTH)
    for col in range(1, 3):
        pygame.draw.line(pygame.display.get_surface(), LINE_COLOR, (col * 200, 0), (col * 200, 600), LINE_WIDTH)

def draw_figures(screen, board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (col * 200 + 100, row * 200 + 100), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * 200 + SPACE, row * 200 + SPACE), 
                                 (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), 
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * 200 + SPACE, row * 200 + 200 - SPACE), 
                                 (col * 200 + 200 - SPACE, row * 200 + SPACE), 
                                 CROSS_WIDTH)

def display_winner(screen, winner):
    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 80)
    if winner == "Tie":
        text = font.render("¡Empate!", True, LINE_COLOR)
    else:
        text = font.render(f"Jugador {winner} gana!", True, LINE_COLOR)
    text_rect = text.get_rect(center=(300, 250))
    screen.blit(text, text_rect)

    font_small = pygame.font.Font(None, 50)
    retry_text = font_small.render("Presiona R para revancha", True, LINE_COLOR)
    retry_rect = retry_text.get_rect(center=(300, 350))
    screen.blit(retry_text, retry_rect)

    quit_text = font_small.render("Presiona Q para salir", True, LINE_COLOR)
    quit_rect = quit_text.get_rect(center=(300, 400))
    screen.blit(quit_text, quit_rect)

    pygame.display.update()
