import os
import datetime

# Struktur data untuk menyimpan soal-soal berdasarkan hari (dictionary of lists of dictionaries)
questions_by_day = {
    "Senin": [
        {"question": "Berapa hasil 5 + 3?", "options": ["7", "8", "9"], "answer": "8"},
        {"question": "Berapa hasil 10 - 4?", "options": ["5", "6", "7"], "answer": "6"},
        {"question": "Berapa hasil 2 * 6?", "options": ["10", "12", "14"], "answer": "12"}
    ],
    "Selasa": [
        {"question": "Apa nama planet terdekat dari Matahari?", "options": ["Venus", "Merkurius", "Bumi"], "answer": "Merkurius"},
        {"question": "Apa fungsi daun pada tumbuhan?", "options": ["Bernapas", "Fotosintesis", "Makan"], "answer": "Fotosintesis"},
        {"question": "Apa nama gas yang kita hirup?", "options": ["Oksigen", "Nitrogen", "Karbon dioksida"], "answer": "Oksigen"}
    ],
    "Rabu": [
        {"question": "Apa ibu kota Indonesia?", "options": ["Jakarta", "Surabaya", "Bandung"], "answer": "Jakarta"},
        {"question": "Siapa presiden pertama Indonesia?", "options": ["Soekarno", "Suharto", "Habibie"], "answer": "Soekarno"},
        {"question": "Apa bahasa resmi Indonesia?", "options": ["Jawa", "Bahasa Indonesia", "Sunda"], "answer": "Bahasa Indonesia"}
    ],
    "Kamis": [
        {"question": "Berapa hasil 7 + 2?", "options": ["8", "9", "10"], "answer": "9"},
        {"question": "Berapa hasil 15 / 3?", "options": ["4", "5", "6"], "answer": "5"},
        {"question": "Berapa hasil 4^2?", "options": ["16", "18", "20"], "answer": "16"}
    ],
    "Jumat": [
        {"question": "Apa nama organ tubuh yang memompa darah?", "options": ["Hati", "Jantung", "Paru-paru"], "answer": "Jantung"},
        {"question": "Apa proses perubahan air menjadi uap?", "options": ["Penguapan", "Pembekuan", "Pencairan"], "answer": "Penguapan"},
        {"question": "Apa nama unsur kimia dengan simbol O?", "options": ["Oksigen", "Osmium", "Oganesson"], "answer": "Oksigen"}
    ],
    "Sabtu": [
        {"question": "Apa warna langit pada siang hari?", "options": ["Merah", "Biru", "Hijau"], "answer": "Biru"},
        {"question": "Berapa hasil 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
        {"question": "Apa nama hewan tercepat di dunia?", "options": ["Singa", "Cheetah", "Harimau"], "answer": "Cheetah"}
    ],
    "Minggu": [
        {"question": "Apa nama sungai terpanjang di dunia?", "options": ["Nil", "Amazon", "Yangtze"], "answer": "Nil"},
        {"question": "Siapa penemu lampu pijar?", "options": ["Einstein", "Edison", "Tesla"], "answer": "Edison"},
        {"question": "Apa nama benua terbesar?", "options": ["Asia", "Afrika", "Amerika"], "answer": "Asia"}
    ]
}

# Fungsi untuk mendapatkan hari saat ini dalam bahasa Indonesia
def get_current_day():
    days = {
        0: "Senin",
        1: "Selasa",
        2: "Rabu",
        3: "Kamis",
        4: "Jumat",
        5: "Sabtu",
        6: "Minggu"
    }
    today = datetime.datetime.now().weekday()
    return days[today]

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
    print("1. Mulai Belajar (Soal Umum)")
    print("2. Lihat Streak")
    print("3. Pengingat Belajar (Berdasarkan Hari)")
    print("4. Keluar")

# Fungsi untuk memainkan game dengan soal umum
def play_game(current_streak):
    streak = current_streak
    questions = [
        {"question": "Apa ibu kota Indonesia?", "options": ["Jakarta", "Surabaya", "Bandung"], "answer": "Jakarta"},
        {"question": "Berapa hasil 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
        {"question": "Apa warna langit pada siang hari?", "options": ["Merah", "Biru", "Hijau"], "answer": "Biru"}
    ]
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

# Fungsi untuk memainkan game berdasarkan hari (pengingat)
def play_reminder_game(current_streak, day):
    streak = current_streak
    if day in questions_by_day:
        questions = questions_by_day[day]
        print(f"\nHari ini {day}, materi belajar: {'Matematika' if day == 'Kamis' else 'IPA' if day == 'Jumat' else 'Umum'}")
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
    else:
        print("Tidak ada soal untuk hari ini.")
    
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
            choice = int(input("Pilih menu (1-4): "))
            if choice == 1:
                streak = play_game(streak)
                save_streak(streak)
            elif choice == 2:
                view_streak(streak)
            elif choice == 3:
                day = get_current_day()
                streak = play_reminder_game(streak, day)
                save_streak(streak)
            elif choice == 4:
                print("Terima kasih telah bermain!")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input harus angka. Coba lagi.")

if __name__ == "__main__":
    main()