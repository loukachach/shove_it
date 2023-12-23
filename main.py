import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 50
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shove it")

def draw_game_board(game_board):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
 
def read_game_board(file_path):
    game_board = []
    try:
        with open(file_path, 'r') as file:
            # Alternatively, read line by line
            print("\nReading Line by Line:")
            file.seek(0)  # Reset file pointer to the beginning
            for line in file:
                print(line,)  # strip() removes leading and trailing whitespaces
                game_board.append(list(line))
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(game_board)
    return game_board



##################
######  MAIN #####
##################

board = read_game_board('./level_1')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the board
    draw_game_board(board)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
