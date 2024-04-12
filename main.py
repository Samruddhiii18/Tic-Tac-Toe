# modules
import pygame, sys
import numpy as np

#initialiase pygame
pygame.init()

#-------------------
# Constant
#-------------------
width = 300
height = 300
line_width = 15
board_rows = 3
board_cols = 3
square_size = width // board_cols
circle_radius = square_size // 3
circle_width = 15
cross_width = 25
space = square_size // 4

# rgb: red, green, blue
red = (255, 0, 0)
bg_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(bg_color)

# board
board = np.zeros((board_rows, board_cols))
print(board)

#pygame.draw.line( screen,red,(10,10),(300,300),10)


def draw_lines():
  #1. horizontal
  pygame.draw.line(screen, line_color, (0, square_size), (width, square_size),
                   line_width)
  #2. horizontal
  pygame.draw.line(screen, line_color, (0, 2 * square_size),
                   (width, 2 * square_size), line_width)

  #1. vertical
  pygame.draw.line(screen, line_color, (square_size, 0), (square_size, height),
                   line_width)
  #2. vertical
  pygame.draw.line(screen, line_color, (2 * square_size, 0),
                   (2 * square_size, height), line_width)


def draw_figures():
  for row in range(board_rows):
    for col in range(board_cols):
      if board[row][col] == 1:
        pygame.draw.circle(screen, circle_color,
                           (int(col * square_size + square_size // 2),
                            int(row * square_size + square_size // 2)),
                           circle_radius, circle_width)
      elif board[row][col] == 2:
        pygame.draw.line(screen, cross_color,
                         (col * square_size + space,
                          row * square_size + square_size - space),
                         (col * square_size + square_size - space,
                          row * square_size + space), cross_width)
        pygame.draw.line(
            screen, cross_color,
            (col * square_size + space, row * square_size + space),
            (col * square_size + square_size - space,
             row * square_size + square_size - space), cross_width)


def mark_square(row, col, player):
  board[row][col] = player


def available_square(row, col):
  return board[row][col] == 0


def is_board_full():
  for row in range(board_rows):
    for col in range(board_cols):
      if board[row][col] == 0:
        return False

  return True


def check_win(player):
  # vertical win check
  for col in range(board_cols):
    if board[0][col] == player and board[1][col] == player and board[2][
        col] == player:
      draw_vertical_winning_line(col, player)
      return True

  # horizontal win check
  for row in range(board_rows):
    if board[row][0] == player and board[row][1] == player and board[row][
        2] == player:
      draw_horizontal_winning_line(row, player)
      return True

  # asc diagonal win check
  if board[2][0] == player and board[1][1] == player and board[0][2] == player:
    draw_asc_diagonal(player)
    return True

  # desc diagonal win check
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    draw_desc_diagonal(player)
    return True

  return False


def draw_vertical_winning_line(col, player):
  posX = col * square_size + square_size // 2

  if player == 1:
    color = circle_color
  elif player == 2:
    color = cross_color

  pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)


def draw_horizontal_winning_line(row, player):
  posY = row * square_size + square_size // 2

  if player == 1:
    color = circle_color
  elif player == 2:
    color = cross_color

  pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)


def draw_asc_diagonal(player):
  if player == 1:
    color = circle_color
  elif player == 2:
    color = cross_color

  pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)


def draw_desc_diagonal(player):
  if player == 1:
    color = circle_color
  elif player == 2:
    color = cross_color

  pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)


def restart():
  screen.fill(bg_color)
  draw_lines()
  player = 1
  for row in range(board_rows):
    for col in range(board_cols):
      board[row][col] = 0


draw_lines()

player = 1
game_over = False

# mainloop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
      mouseX = event.pos[0]  #x
      mouseY = event.pos[1]  #y

      clicked_row = int(mouseY // square_size)
      clicked_col = int(mouseX // square_size)

      if available_square(clicked_row, clicked_col):
        mark_square(clicked_row, clicked_col, player)
        if check_win(player):
          game_over = True
        player = player % 2 + 1

        draw_figures()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        restart()
        game_over = False

  pygame.display.update()
