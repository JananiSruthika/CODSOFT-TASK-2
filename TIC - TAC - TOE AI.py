#!/usr/bin/env python
# coding: utf-8

# In[1]:


# IMPORTING REQUIRED LIBRARY
import random


# In[2]:


# CREATING A CLASS FOR TIC-TAC-TOE
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.human_player = 'X'
        self.ai_player = 'O'

    def print_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-----")

    def is_winner(self, player):
    # CHECK ROWS, COLUMNS AND DIAGONALS FOR A WIN
        for i in range(0, 9, 3):
            if all(self.board[j] == player for j in range(i, i + 3)) or               all(self.board[j] == player for j in range(i // 3, i // 3 + 3)):
                return True
        if all(self.board[i] == player for i in range(0, 9, 4)) or            all(self.board[i] == player for i in range(2, 7, 2)):
            return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner(self.human_player) or                self.is_winner(self.ai_player) or                self.is_board_full()

    def get_empty_cells(self):
        return [i for i, cell in enumerate(self.board) if cell == ' ']

    # USING MINIMAX ALGORITHM
    def minimax(self, depth, maximizing_player):
        if self.is_winner(self.human_player):
            return -1
        elif self.is_winner(self.ai_player):
            return 1
        elif self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for empty_cell in self.get_empty_cells():
                self.board[empty_cell] = self.ai_player
                eval = self.minimax(depth + 1, False)
                self.board[empty_cell] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for empty_cell in self.get_empty_cells():
                self.board[empty_cell] = self.human_player
                eval = self.minimax(depth + 1, True)
                self.board[empty_cell] = ' '
                min_eval = min(min_eval, eval)
            return min_eval       
        
    def best_move(self):
        best_val = float('-inf')
        best_move = -1

        for empty_cell in self.get_empty_cells():
            self.board[empty_cell] = self.ai_player
            move_val = self.minimax(0, False)
            self.board[empty_cell] = ' '

            if move_val > best_val:
                best_move = empty_cell
                best_val = move_val

        return best_move

    # FUNCTION FOR PLAYING THE GAME
    def play(self):
        while not self.is_game_over():
            self.print_board()

            if self.is_board_full():
                print("It's a tie!")
                break

            human_move = int(input("Enter your move (1-9): ")) - 1

            if self.board[human_move] != ' ' or human_move < 0 or human_move > 8:
                print("Invalid move. Try again.")
                continue

            self.board[human_move] = self.human_player

            if self.is_winner(self.human_player):
                self.print_board()
                print("Congratulations! You win!")
                break

            if self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

            ai_move = self.best_move()
            print(f"AI plays at position {ai_move + 1}")
            self.board[ai_move] = self.ai_player

            if self.is_winner(self.ai_player):
                self.print_board()
                print("AI wins! Better luck next time.")
                break

# MAIN FUNCTION
if __name__ == "__main__":
    game = TicTacToe()
    game.play()


# In[ ]:




