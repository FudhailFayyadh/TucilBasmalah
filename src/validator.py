class Validator:
    def __init__(self, board):
        self.board = board
        self.n = len(board)
        self.color_regions = self.build_color_map()
    
    def build_color_map(self):
        color_map = {}

        for i in range(self.n):
            for j in range (self.n):
                color = self.board[i][j]
                if color not in color_map:
                    color_map[color] = []
                color_map[color].append((i,j))

        return color_map 

    def is_region_valid(self):
        num_colors = len(self.color_regions)
        if num_colors != self.n:
            raise ValueError(f"Jumlah warna tidak sams dengan ukuran papan, \nPapan = {self.n}) \nWarna = {num_colors}")
        
    def is_valid(self, permutation):   
        if not self.check_color_cinstraints(permutation):
            return False
            
        if not self.check_neighbor(permutation):
            return False
            
        return True
    
    def check_color_cinstraints(self, permutation):
        color_used ={}

        for row in range (self.n):
            col = permutation[row]
            color = self.board[row][col]

            if color in color_used:
                return False
            
            color_used[color] = True

        return True
    
    def check_neighbor(self, permutation):
        queens_positions = [(row, permutation[row]) for row in range(self.n)]

        for i in range(len(queens_positions)):
            for j in range(i + 1, len(queens_positions)):
                r1, c1 = queens_positions[i]
                r2, c2 = queens_positions[j]
                if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1:
                    return False

        return True
            