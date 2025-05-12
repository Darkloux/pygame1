import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colores
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Dibujar las líneas del tablero
def draw_lines():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Dibujar figuras (círculos y cruces)
def draw_figures(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                                 CROSS_WIDTH)

# Verificar victoria
def check_win(player):
    # Verificar filas
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Verificar columnas
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            return True
    # Verificar diagonales
    if all([board[i][i] == player for i in range(BOARD_ROWS)]):
        return True
    if all([board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)]):
        return True
    return False

# Verificar empate
def check_tie():
    for row in board:
        if '' in row:
            return False
    return True

# Mostrar pantalla de triunfo
def display_winner(winner):
    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 80)
    if winner == "Tie":
        text = font.render("¡Empate!", True, LINE_COLOR)
    else:
        text = font.render(f"Jugador {winner} gana!", True, LINE_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    font_small = pygame.font.Font(None, 50)
    retry_text = font_small.render("Presiona R para revancha", True, LINE_COLOR)
    retry_rect = retry_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(retry_text, retry_rect)

    quit_text = font_small.render("Presiona Q para salir", True, LINE_COLOR)
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(quit_text, quit_rect)

    pygame.display.update()

# Reiniciar el tablero
def reset_game():
    global board
    board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    screen.fill(BG_COLOR)
    draw_lines()

# Inicializar el tablero vacío
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Bucle principal del juego
def main():
    draw_lines()
    player = 'X'
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Revancha
                        reset_game()
                        player = 'X'
                        game_over = False
                    elif event.key == pygame.K_q:  # Salir
                        running = False
            if not game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] == '':
                    board[clicked_row][clicked_col] = player
                    if check_win(player):
                        display_winner(player)
                        game_over = True
                    elif check_tie():
                        display_winner("Tie")
                        game_over = True
                    player = 'O' if player == 'X' else 'X'

        if not game_over:
            screen.fill(BG_COLOR)
            draw_lines()
            draw_figures(board)
            pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
