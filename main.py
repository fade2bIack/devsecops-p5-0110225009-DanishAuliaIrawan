from operasi import tambah_data
from validasi import cek_input

def jalankan_aplikasi():
    print("Aplikasi berjalan...")
    data = "Data Rahasia"
    if cek_input(data):
        tambah_data(data)

if __name__ == "__main__":
    jalankan_aplikasi()