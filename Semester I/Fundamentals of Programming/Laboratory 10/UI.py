import numpy as ny
import pygame
import sys
import math
import random
from Exception.Exception import RepoError


class Presentation:
    def __init__(self, service):
        self.__service = service
    def menu(self):
        print("1.GUI")
        print("2.UI")
    def __board(self, row, column):
        return self.__service.create_board(row, column)

    def __print_board(self, board):
        print(ny.flip(board, 0))

    def __get_row(self, board, table_row, column):
        return self.__service.row(board, table_row, column)

    def __move(self, board, row, column, player):
        return self.__service.move(board, row, column, player)

    def __verify_win(self, board, row, column, table_row, table_column):
        return self.__service.win(board, row, column, table_row, table_column)

    def __block(self, board, table_row, table_column, x):
        return self.__service.block(board, table_row, table_column, x)

    def draw_board(self, board, row, column, screen, square, radius, blue, black, red, yellow, height):
        for i in range(column):
            for j in range(row):
                pygame.draw.rect(screen, blue, (i * square, j * square + square, square, square))
                pygame.draw.circle(screen, black,
                                   (int(i * square + square / 2), int(j * square + square + square / 2)), radius)
        for i in range(column):
            for j in range(row):
                if board[j][i] == 1:
                    pygame.draw.circle(screen, red,
                                       (int(i * square + square / 2), height - int(j * square + square / 2)), radius)
                elif board[j][i] == 2:
                    pygame.draw.circle(screen, yellow,
                                       (int(i * square + square / 2), height - int(j * square + square / 2)), radius)
        pygame.display.update()

    def full_table(self, board, table_row, table_column):
        return self.__service.full_table(board, table_row, table_column)

    def start(self):
      self.menu()
      m=int(input("x="))
      if m==1:
        table_row = 6
        table_column = 7
        board = self.__board(table_row, table_column)
        game_over = False
        turn = random.randint(0, 1)
        pygame.init()
        square = 90
        width = 630
        height = 630
        radius = int(square / 2 - 5)
        size = (width, height)
        screen = pygame.display.set_mode(size)
        blue = (0, 0, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        white = (255, 255, 255)
        g = False
        self.__print_board(board)
        self.draw_board(board, table_row, table_column, screen, square, radius, blue, black, red, yellow, height)
        pygame.display.update()
        if turn == 1:
            pygame.draw.rect(screen, black, (0, 0, width, square))
            column = random.randint(0, 6)
            row = self.__get_row(board, table_row, column)
            self.__move(board, row, column, 2)
            turn += 1
            pygame.time.wait(2000)
            self.__print_board(board)
            self.draw_board(board, table_row, table_column, screen, square, radius, blue, black, red, yellow, height)
        while game_over == False and g == False:
            for event in pygame.event.get():
                g = self.full_table(board, table_row, table_column)
                if g == True and game_over == False:
                    myfont = pygame.font.SysFont("monospace", 75)
                    label = myfont.render("    Draw", 1, white)
                    screen.blit(label, (30, 10))
                    self.__print_board(board)
                    self.draw_board(board, table_row, table_column, screen, square, radius, blue, black, red, yellow,
                                    height)
                    pygame.time.wait(2000)
                else:
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEMOTION:
                        pygame.draw.rect(screen, black, (0, 0, width, square))
                        position_of_x = event.pos[0]
                        if turn % 2 == 0:
                            pygame.draw.circle(screen, red, (position_of_x, int(square / 2)), radius)
                    pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN and turn % 2 == 0:
                        pygame.draw.rect(screen, black, (0, 0, width, square))
                        position_of_x = event.pos[0]
                        column = int(math.floor(position_of_x / square))
                        try:
                            row = self.__get_row(board, table_row, column)
                            self.__move(board, row, column, 1)
                            game_over = self.__verify_win(board, row, column, table_row, table_column)
                            if game_over == True:
                                myfont = pygame.font.SysFont("monospace", 75)
                                label = myfont.render(" Player wins", 1, red)
                                screen.blit(label, (30, 10))
                            else:
                                turn += 1
                        except RepoError as re:
                            myfont = pygame.font.SysFont("monospace", 35)
                            label = myfont.render(str(re), 1, red)
                            screen.blit(label, (30, 10))
                        self.__print_board(board)
                        self.draw_board(board, table_row, table_column, screen, square, radius, blue, black, red,
                                        yellow,
                                        height)
                    elif turn % 2 != 0:
                        x = -1
                        x = self.__block(board, table_row, table_column, x)
                        if x != -1:
                            column = x
                        else:
                            pygame.draw.rect(screen, black, (0, 0, width, square))
                            column = random.randint(0, 6)
                        try:
                            row = self.__get_row(board, table_row, column)
                            self.__move(board, row, column, 2)
                            game_over = self.__verify_win(board, row, column, table_row, table_column)
                            if game_over == True:
                                myfont = pygame.font.SysFont("monospace", 75)
                                label = myfont.render("  PC wins", 1, yellow)
                                screen.blit(label, (30, 10))
                            else:
                                turn += 1
                        except RepoError as re:
                            myfont = pygame.font.SysFont("monospace", 35)
                            label = myfont.render(str(re), 1, yellow)
                            screen.blit(label, (30, 10))
                        self.__print_board(board)
                        self.draw_board(board, table_row, table_column, screen, square, radius, blue, black, red,
                                        yellow,
                                        height)
                if game_over == True or g == True:
                    pygame.time.wait(3000)
      else:
          table_row = 6
          table_column = 7
          board = self.__board(table_row, table_column)
          game_over = False
          turn = random.randint(0, 1)
          g = False
          self.__print_board(board)
          turn=0
          while game_over == False and g == False:
              g = self.full_table(board, table_row, table_column)
              if g == True and game_over == False:
                 self.__print_board(board)
                 print("Draw")
                 return
              else:
                  if turn%2==0:
                      print("Player move:")
                      column = int(input("move="))
                      try:
                          row = self.__get_row(board, table_row, column)
                          self.__move(board, row, column, 1)
                          game_over = self.__verify_win(board, row, column, table_row, table_column)
                          if game_over == True:
                              print("Player 1 won")
                              self.__print_board(board)
                              return
                          else:
                               turn += 1
                      except RepoError as re:
                          print("RepoError!")
                      self.__print_board(board)
                  else:
                      x = -1
                      x = self.__block(board, table_row, table_column, x)
                      if x != -1:
                          column = x
                      else:
                          column = random.randint(0, 6)
                      try:
                          row = self.__get_row(board, table_row, column)
                          self.__move(board, row, column, 2)
                          game_over = self.__verify_win(board, row, column, table_row, table_column)
                          if game_over == True:
                              print("Pc wins")
                              self.__print_board(board)
                              return
                          else:
                              turn += 1
                      except RepoError as re:
                          print("RepoError")
                      self.__print_board(board)