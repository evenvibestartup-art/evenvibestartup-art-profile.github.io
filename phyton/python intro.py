import time
import sys
import os

# --- Fungsi Dasar ---

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.06): # Jeda 0.06 detik per karakter
    """Menampilkan teks karakter demi karakter (seperti mengetik)."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() # Memastikan karakter langsung muncul
        time.sleep(delay)
    print() # Pindah baris setelah selesai mengetik

# --- Fungsi Utama ---

def tampilkan_intro():
    
    clear_screen()
    
    # Pesan 1: Intro
    typing_effect("Project Initialize...")
    time.sleep(0.5)
    
    # Pesan 2: Nama Brand
    typing_effect("Loading Brand Identity: EVENVIBE.LOCAL")
    time.sleep(1.0)
    
    # Pesan 3: Slogan (lebih cepat)
    typing_effect("Your Event, Our Vibe")
    time.sleep(1.5)
    
    # Jeda
    typing_effect("--- READY ---")
    time.sleep(2.0)
    
    # Hapus layar lagi untuk tampilan bersih (opsional)
    clear_screen()
    typing_effect("EVENVIBE.LOCAL")
    print("\n\nSelamat Datang!")


# Jalankan fungsinya
if __name__ == "__main__":
    tampilkan_intro()