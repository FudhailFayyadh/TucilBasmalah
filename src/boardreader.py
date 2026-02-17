class BoardReader:
    def __init__(self):
        self.board = []
        self.n = 0

    def read_file(self, filename):
        try:
            with open (filename, 'r') as f:
                lines = f.readlines()
            
            self.board = []
            for line in lines:
                line = line.strip()
                if line :
                    self.board.append(list(line))
            
            if not self.board:
                raise ValueError("File Tidak Valid")

            self.n = len(self.board)

            return self.board  
        
        except FileNotFoundError:
            raise FileNotFoundError(f"file'{filename}' tidak ditemukan")
        except Exception as e:
            raise e
        

    def validate_board(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if not cell.isalpha():
                    raise ValueError(
                        f"Karakter '{cell}' pada posisi ({i},{j}) tidak valid "
                        f"Karakter harus berupa alphabet"
                    )
                
        row_lengths = [len(row) for row in self.board]
        if len(set(row_lengths)) != 1:
            raise ValueError("Panjang baris tidak konsisten")
        
        if row_lengths[0] != self.n:
            raise ValueError("Panjang baris tidak sesuai dengan ukuran papan")
        
        print("board valid")
    
    def get_board(self):
        return self.board
    
    def get_size(self):
        return self.n