# Tugas-Proyek-DDP1

Nama : Raihan Fariz Novanto
NIM : 2409116083

1. FLowchart
   dibawah ini adalah flowchart yang saya buat untuk membuat program perhitungan gaji karyawan, bisa dilihat juga dari file txt yang sudah saya berikan
   ![image](https://github.com/user-attachments/assets/9836414e-0871-428d-9794-0d9cf4cf441a)
 pada flowchart diatas saya memulai dengan simbol START dengan bentuk Oval, lalu user akan ke halaman login untuk input username dan password
username dan password yang digunakan adalah
username : Raihan
password : 2409116083
jika password salah, maka akan mengulang hingga password benar
jika password sudah benar maka akan loanjut ke progran perhitungan gaji
setelah masuk, maka user akan disambut dan langsung disuruh untuk menginput Gaji dan Jam Kerja
Jika jam kerja kurang dari 160 jam, Maka user tidak akan mendapatkan bonus 10% dari Gaji
Jiika Jam Kerja lebih dari 160 jam, Maka program akan mengarahkan pada program/proses perhitungan bonus 10%
setelah selesai, user akan memilih, apakah ingin mengulang perhitungan apa tidak
jika ingin melakukan perhitungan ulang, maka user akan kembali ke halaman login
jika tidak, maka user akan keluar dari program
jika sudah selesai, maka program akan selesai juga

3. Kode
   dibawah ini merupakan kodingan saya, bisa dilihat juga dari file yang sudah saya berikan
      ![image](https://github.com/user-attachments/assets/96c785db-4fb0-4d9b-9483-16666fc3d369)

   pada kode saya, pertama saya menggunakan login dengan username dan password yang sudah saya tentukan sebelumnya
   kode saya menggunakan percabaangan berguna untuk mendapatkan nilai tambah pada mata kuliah dasar pemrograman ini

   ![Uploading Screenshot 2024-09-30 104339.png…]()   
   ini merupakan username dan password yang sudah saya tentukan sebelumnya
  
#output yang akan ditampilkan saat akan login
  pada kode di atas ini merupakan kode untuk input username dan password

#proses untuk login, apakah password benar atau salah
ini merupakan proses percabangan untuk menentukan apakah password yang diinputkan user sudah benar atau tidak, jika tidak benar, maka user akan mengulang dari halaman login

#saat sudah masuk maka akan ada output seperti ini
pada kode ini saya sengaja memberikannya untuk menyambut user, seperti yang ada di web SIPLO

#input yang digunakan untuk memasukkan Gaji dan Jam Kerja
pada input ini digunakan untuk memasukkan gaji dan jam kerja dari user

#percabangan, kalau Jam Kerja lebih dari 160 jam maka akan mendapatkan bonus
pada percabangan ini saya menggunakan 0.10 untuk memberi bonus dari user, karena nilainya sama dengan 10%
di percabangan ini akan ada 3 output pertama dari output jam kerja > 160 akan ada output bonus yang didapatkan dan jumlah Gaji yang telah ditambahkan oleh bonus
pada output else atau Gaji < 160, hanya akan ada output Anda tidak mendapatkan bonus

#input untuk user, apakah ingin menghitung ulang gaji apa tidak
pada bagian ini user akan mendapatkan pilihan, apakah ingin menghitung gaji ulang apa tidak, jika ya maka user akan kembali ke halaman login
jika tidak, maka user akan mendapatkan output terimakasih, dan keluar dari program, tambahan saya menggunakan lower() agar input user menjadi kecil semua
sebagai contoh, jika user ngetik Ya/YA/yA, maka inputnya akan menjadi ya, berfungsi untuk if else pada program selanjutnya (program itu sangat rawan, typo dikit aja eror)

#jika user memilih tidak, maka akan keluar dari program
ada program ini untuk memproses input user, jika ya maaka user memilih untuk menghitung gaji ulang, jika tidak maka user memilih tidak ingin menghitung ulang gaji dan program selesai.

sekian program saya, terimakasih
