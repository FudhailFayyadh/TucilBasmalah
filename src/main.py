import os
import sys
from visual import Visual
from boardreader import BoardReader
from validator import Validator
from queensolver import QueenSolver

def print_header():
    print("\n" + "="*60)
    print(" " * 15 + "QUEENS SOLVER")
    print(" " * 10 + "Brute Force Algorithm")
    print("="*60 + "\n")

def get_input_file():
    print("File yang Tersedia:")

    test_dir = "../test"
    if os.path.exists(test_dir):
        test_file = [f for f in os.listdir(test_dir) if f.endswith('.txt')]

        if test_file:
            print("\nFile yang tersedia")
            for i, file in enumerate(test_file, 1):
                print(f"{i}. {file}")
            print()
    
    while True:
        filename = input("Masukan nama file ").strip()
        if not os.path.exists(filename):
            test_path = os.path.join(test_dir, filename)
            if os.path.exists(test_path):
                filename = test_path
            else:
                print ("File tidak ditemukan.)")
                continue
    
        return filename
    
        

def main():
    try:
        print_header()

        filename = get_input_file()
        print(f"Memuat papan dari {filename}...")
        reader = BoardReader()
        board = reader.read_file(filename)
        reader.validate_board()
        validator = Validator(board)
        visual = Visual(board)
        queen_solver = QueenSolver(board)
        validator.is_region_valid()

        print("\n Papan yang dimuat:")
        visual.display_board()

        input("Tekan Enter untuk memulai pencarian solusi...")
        solution = queen_solver.solve(validator, visual)
        stats = queen_solver.get_statistics()

        if solution:
            visual.display_solution(solution, stats['time_ms'], stats['iterations'])
            save = input("Apakah Anda ingin menyimpan solusi? (y/n): ").strip().lower()
            if save == 'y':
                save_filename = input("Masukan nama file untuk menyimpan solusi: ").strip()

                if not save_filename:
                    save_filename = "solusi.txt"

                if not save_filename.endswith('.txt'):
                    save_filename += '.txt'
                
                output_dir = "../output"
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                output_path = os.path.join(output_dir, save_filename)
                queen_solver.save_solution(output_path, solution)


        else:
            visual.print_no_solution(stats['time_ms'], stats['iterations'])
        
        print("Program selesai.")

    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e) 
        sys.exit(1)

if __name__ == "__main__":
    main()   
