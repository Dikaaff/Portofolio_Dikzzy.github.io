# Tugas pertemuan 3 algoritma pemrograman (praktik)
# Nama : Dika Afif Indrawan (23.01.5029)
# Tugas menuliskan kode program untuk menghitung umur

Tanggal = 22
Bulan = 6
Tahun = 2005
print("Tanggal : ", Tanggal)
print("Bulan : ", Bulan)
print("Tahun : ", Tahun)


jumlah_hari = int(input("Masukkan jumalah hari: "))
jumlah_tahun = int(jumlah_hari / 365)
jumlah_minggu = int(jumlah_hari % 365 / 7)
sisa_jumlah_hari = int(jumlah_hari % 365 % 7)
print(f"Tahun = {jumlah_tahun}, Minggu = {jumlah_minggu}, Hari = {sisa_jumlah_hari}")