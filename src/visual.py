import os
import sys

class Visual:
    def __init__(self, board):
        self.board = board
        self.n = len(board)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self, permutation = None, clear = None):
        if clear:
            self.clear_screen()
        print ("\n" + "="*40)

        for row in range (self.n):
            line = ""
            for col in range (self.n):
                has_queen = False
                if permutation:
                    has_queen = (permutation[row] == col)
                if has_queen:
                    line += "# "
                else:
                    line += self.board[row][col] + " "
            print(line)

        print("="*40 + "\n")


        
    def display_solution(self, permutation, time_ms, iteration):
        print("\nSolusi Ditemukan\n")

        self.display_board(permutation)

        print(f"Waktu pencarian: {time_ms:.2f} ms")
        print(f"Iterasi: {iteration}")

    def print_no_solution(self, time_ms, iteration):
        print("Tidak ada solusi yang ditemukan")
        print(f"Waktu pencarian: {time_ms:.2f} ms")
        print(f"Iterasi: {iteration}")

    def animate_progress(self, permutation, iteration, total):
        sys.stdout.write(f"\riterasi: {iteration}/{total}") 
        sys.stdout.flush()

        print("\n" + "="*40)
        for row in range (self.n):
            line = ""
            for col in range (self.n):
                has_queen = (permutation[row] == col)
                if has_queen:
                    line += "# "
                else:
                    line += self.board[row][col] + " "
            print(line)
        print("="*40 + "\n")
        