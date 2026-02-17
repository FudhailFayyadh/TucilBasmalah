# Queens Solver - Brute Force Algorithm

Program untuk menyelesaikan masalah N-Queens dengan constraint warna menggunakan algoritma Brute Force.

## Deskripsi

Program ini menyelesaikan varian dari masalah N-Queens klasik dengan constraint tambahan:
1. **Color Constraint**: Setiap queen harus ditempatkan pada warna/region yang berbeda
2. **Neighbor Constraint**: Tidak ada dua queen yang boleh bertetangga (termasuk diagonal)

Program menggunakan pendekatan Brute Force dengan mengiterasi semua kemungkinan permutasi posisi queen hingga menemukan solusi yang valid.

## Fitur

- 🎯 Menyelesaikan masalah N-Queens dengan constraint warna
- 🔄 Visualisasi progress pencarian secara real-time
- 📊 Menampilkan statistik pencarian (waktu dan jumlah iterasi)
- 💾 Menyimpan solusi ke file output
- ✅ Validasi papan input secara otomatis

## Struktur Direktori

```
TucilAiTipis/
├── src/
│   ├── main.py              # Entry point program
│   ├── boardreader.py       # Membaca dan memvalidasi file board
│   ├── validator.py         # Validasi constraint dan solusi
│   ├── queensolver.py       # Algoritma brute force solver
│   └── visual.py            # Visualisasi board dan progress
├── test/
│   ├── test4x4.txt         # Test case board 4x4
│   ├── test6x6.txt         # Test case board 6x6
│   └── test9x9.txt         # Test case board 9x9
├── output/                  # Folder untuk menyimpan solusi
└── bin/
```

## Cara Menggunakan

### Prerequisites

- Python 3.x

### Menjalankan Program

1. Navigasi ke direktori `src`:
```bash
cd src
```

2. Jalankan program:
```bash
python main.py
```

3. Ikuti instruksi yang muncul:
   - Masukkan nama file input (misalnya: `test4x4.txt` atau path lengkap)
   - Tekan Enter untuk memulai pencarian
   - Tunggu hingga solusi ditemukan
   - Pilih apakah ingin menyimpan solusi (y/n)

### Format File Input

File input berisi papan N×N dengan karakter alphabet yang merepresentasikan warna/region:

**Contoh (4x4):**
```
AABB
ACDB
CDDB
CCDD
```

**Aturan:**
- Setiap baris harus memiliki panjang yang sama
- Hanya menggunakan karakter alphabet (A-Z)
- Jumlah warna/region unik harus sama dengan ukuran papan (N)

### Format File Output

File output menampilkan solusi dengan simbol `#` untuk posisi queen:

**Contoh:**
```
A#BB
AC#B
C#DB
CCDD
```

## Cara Kerja Algoritma

1. **Inisialisasi**: Membaca board dan memvalidasi input
2. **Generate Permutasi**: Menghasilkan semua permutasi posisi kolom untuk setiap baris (N!)
3. **Validasi**: Untuk setiap permutasi, cek:
   - Apakah setiap queen berada di warna/region yang berbeda
   - Apakah tidak ada queen yang bertetangga
4. **Solusi**: Jika permutasi valid ditemukan, simpan sebagai solusi
5. **Output**: Tampilkan hasil dan statistik pencarian

## Kompleksitas

- **Time Complexity**: O(N! × N²)
  - N! untuk mengiterasi semua permutasi
  - N² untuk validasi setiap permutasi
- **Space Complexity**: O(N²)

## Contoh Penggunaan

```
============================================================
               QUEENS SOLVER
          Brute Force Algorithm
============================================================

File yang Tersedia:

File yang tersedia
1. test4x4.txt
2. test6x6.txt
3. test9x9.txt

Masukan nama file test4x4.txt
Memuat papan dari ../test/test4x4.txt...
board valid

 Papan yang dimuat:
========================================
A A B B 
A C D B 
C D D B 
C C D D 
========================================

Tekan Enter untuk memulai pencarian solusi...
Mencari solusi...

Solusi Ditemukan

========================================
A # B B 
A C # B 
# D D B 
C C D D 
========================================

Waktu pencarian: 0.50 ms
Iterasi: 3

Apakah Anda ingin menyimpan solusi? (y/n): y
Masukan nama file untuk menyimpan solusi: solution.txt
Solusi disimpan ke ../output/solution.txt
Program selesai.
```

## Modul

### 1. BoardReader
Bertanggung jawab untuk membaca dan memvalidasi file input.

**Methods:**
- `read_file(filename)`: Membaca board dari file
- `validate_board()`: Memvalidasi format board
- `get_board()`: Mengembalikan board
- `get_size()`: Mengembalikan ukuran board

### 2. Validator
Memvalidasi constraint dan solusi.

**Methods:**
- `build_color_map()`: Membuat peta region warna
- `is_region_valid()`: Validasi jumlah region
- `is_valid(permutation)`: Cek apakah permutasi valid
- `check_color_cinstraints(permutation)`: Cek constraint warna
- `check_neighbor(permutation)`: Cek constraint tetangga

### 3. QueenSolver
Implementasi algoritma brute force.

**Methods:**
- `permutations(arr)`: Generate permutasi (Heap's algorithm)
- `solve(validator, visualizer)`: Mencari solusi
- `get_statistics()`: Mendapatkan statistik pencarian
- `save_solution(filename, permutation)`: Menyimpan solusi

### 4. Visual
Visualisasi board dan progress.

**Methods:**
- `display_board(permutation, clear)`: Tampilkan board
- `display_solution(permutation, time_ms, iteration)`: Tampilkan solusi
- `animate_progress(permutation, iteration, total)`: Animasi progress
- `print_no_solution(time_ms, iteration)`: Pesan jika tidak ada solusi

## Pembuat

Program ini dibuat untuk memenuhi Tugas Kecil Strategi Algoritma.

## Lisensi

Program ini dibuat untuk keperluan akademik.
