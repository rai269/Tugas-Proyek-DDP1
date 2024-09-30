while True:
 
 #username dan password yang digunakan untuk login
 Nama = "Raihan"
 passwordKuatBanget = "2409116083"

#output yang akan ditampilkan saat akan login
 print("Selamat datang di program hitung gaji, silahkan login")
 username = input("Masukkan username anda: ")
 password = input("Masukkan password anti kebobolan: ")

#proses untuk login, apakah password benar atau salah
 if username == Nama and password == passwordKuatBanget:
    print("Login berhasil! Selamat datang!")
 else:
    print("Login gagal! Username atau password salah.")
    continue
 
 #saat sudah masuk maka akan ada output seperti ini
 print(f"Halo {Nama}, Selamat datang!!")

#input yang digunakan untuk memasukkan Gaji dan Jam Kerja
 Gaji= float(input("Silahkan Masukkan Gaji anda: "))
 Jam = float(input("Silahkan Masukkan Jumlah Jam kerja anda: "))

#percabangan, kalau Jam Kerja lebih dari 160 jam maka akan mendapatkan bonus
 if Jam > 160:
    bonus = 0.10 * Gaji
    Gaji += bonus
    print(f"Anda Mendapatkan Bonus 10% Rp. {bonus}")
    print(f"Gaji yang anda terima adalah Rp. {Gaji}")
 else:
    print("Anda tidak mendapatkan bonus")

#input untuk user, apakah ingin menghitung ulang gaji apa tidak
 Ulang = input("Apakah anda ingin menghitung ulang gaji anda? ya/tidak ").lower()

#jika user memilih tidak, maka akan keluar dari program
 if Ulang == "tidak":
      print("Terimakasih, selamat membayar cicilan")
      break