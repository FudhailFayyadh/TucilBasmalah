import time
import math

class QueenSolver:
    def __init__(self, board):
        self.board = board
        self.n = len(board)
        self.iteration_count = 0
        self.solution = None
        self.time_taken = 0

    def permutations(self, arr):
        arr = list(arr)
        n = len (arr)
        c = [0] * n

        yield tuple(arr)

        i = 0
        while i < n:
            if c[i] < i:
                if i % 2 == 0:
                    arr[0], arr[i] = arr[i], arr[0]
                else:
                    arr[c[i]], arr[i] = arr[i], arr[c[i]]
                yield tuple(arr)
                c[i] += 1
                i = 0
            else:
                c[i] = 0
                i += 1

    def solve(self, validator, visualizer=None): 
        print("Mencari solusi...")

        start_time = time.time()

        if self.n <= 4:
            interval = 1
        elif self.n <= 7:
            interval = 10
        else:
            interval = 10000

        total_permutations = math.factorial(self.n)
        initial = list(range(self.n))

        for permutation in self.permutations(initial):
            self.iteration_count += 1

            if visualizer and self.iteration_count % interval == 0:
                visualizer.animate_progress(permutation, self.iteration_count, total_permutations)
            
            if validator.is_valid(permutation):
                end_time = time.time()
                self.time_taken = (end_time - start_time) * 1000
                self.solution = permutation
                return permutation
            
        end_time = time.time()
        self.time_taken = (end_time - start_time) * 1000
        print()
        return None
    
    def get_statistics(self):
        return {
            'time_ms': self.time_taken,
            'iterations': self.iteration_count,
            'solution': self.solution 
        }
    

    def save_solution(self, filename, permutation):
        try:
            with open (filename, 'w') as f:
                for row in range (self.n):
                    col = permutation[row]
                    line = ""
                    for c in range (self.n):
                        if c == col:
                            line += "#"
                        else:
                            line += self.board[row][c]
                    f.write(line + "\n")
            
            print(f"Solusi disimpan ke {filename}")
            return True

        except Exception as e:
            print(f"Gagal menyimpan solusi ke {e}")
            return False
                    
