import os

# Struktur data untuk menyimpan soal-soal (list of dictionaries)
questions = [
    {"question": "Apa ibu kota Indonesia?", "options": ["Jakarta", "Surabaya", "Bandung"], "answer": "Jakarta"},
    {"question": "Berapa hasil 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "Apa warna langit pada siang hari?", "options": ["Merah", "Biru", "Hijau"], "answer": "Biru"},
    {"question": "Siapa presiden pertama Indonesia?", "options": ["Soekarno", "Suharto", "Habibie"], "answer": "Soekarno"},
    {"question": "Apa bahasa resmi Indonesia?", "options": ["Jawa", "Bahasa Indonesia", "Sunda"], "answer": "Bahasa Indonesia"}
]

# Fungsi untuk memuat data streak dari file
def load_streak():
    if os.path.exists("streak.txt"):
        try:
            with open("streak.txt", "r") as file:
                return int(file.read().strip())
        except ValueError:
            print("Error: File streak.txt tidak valid. Menggunakan streak 0.")
            return 0
    return 0

# Fungsi untuk menyimpan data streak ke file
def save_streak(streak):
    try:
        with open("streak.txt", "w") as file:
            file.write(str(streak))
    except IOError:
        print("Error: Gagal menyimpan streak ke file.")

# Fungsi untuk menampilkan menu utama
def display_menu():
    print("\n=== Aplikasi Belajar Mirip Duolingo ===")
    print("1. Mulai Belajar")
    print("2. Lihat Streak")
    print("3. Keluar")

# Fungsi untuk memainkan game (menjawab soal)
def play_game(current_streak):
    streak = current_streak
    for q in questions:
        print(f"\nPertanyaan: {q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input("Pilih jawaban (1-3): "))
            if 1 <= choice <= 3:
                if q['options'][choice-1] == q['answer']:
                    streak += 1
                    print("Benar! Streak bertambah 1.")
                else:
                    streak = 0
                    print("Salah! Streak hilang.")
            else:
                print("Pilihan tidak valid. Streak hilang.")
                streak = 0
        except ValueError:
            print("Input harus angka. Streak hilang.")
            streak = 0
    
    return streak

# Fungsi untuk menampilkan streak
def view_streak(current_streak):
    print(f"\nStreak saat ini: {current_streak}")

# Fungsi utama
def main():
    streak = load_streak()
    while True:
        display_menu()
        try:
            choice = int(input("Pilih menu (1-3): "))
            if choice == 1:
                streak = play_game(streak)
                save_streak(streak)
            elif choice == 2:
                view_streak(streak)
            elif choice == 3:
                print("Terima kasih telah bermain!")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input harus angka. Coba lagi.")

if __name__ == "__main__":
    main()