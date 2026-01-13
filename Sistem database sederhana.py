import csv

FILE_NAME =  'Database.csv'

def tambah_data(nama, umur, tanggal_lahir):
    with open(FILE_NAME, mode='a',  newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, umur, tanggal_lahir])
        print("Data berhasil ditambahkan.")

def lihat_data():
    try:
        with open(FILE_NAME, mode= 'r') as file:
            reader = csv.reader(file)
            print("Data dalam database:")
            for row in reader:
                print(f"nama: {row[0]}, umur: {row[1]}, tanggal lahir: {row[2]}")
    except FileNotFoundError:
        print("Database tidak ditemukan.")
def main():
    while True:
        print("\nmenu:")
        print("1. Tambah data")
        print("2. Lihat data")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3):")
        if pilihan == '1':
            nama = input("Masukkan nama:")
            umur = input("Masukkan umur:")
            tanggal_lahir = input("Masukkan tanggal lahir (DD-MM-YYYY):")
            tambah_data(nama, umur, tanggal_lahir)
        elif pilihan == '2':
            lihat_data()
        elif pilihan == '3':
            print("Keluar dari program.")
            break


if __name__ == "__main__":
    main()