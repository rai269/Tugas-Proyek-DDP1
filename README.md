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
   ![image](https://github.com/user-attachments/assets/59c99c43-0704-4e26-b727-ceb87e0897a2)

   pada kode saya, pertama saya menggunakan login dengan username dan password yang sudah saya tentukan sebelumnya
   kode saya menggunakan percabaangan berguna untuk mendapatkan nilai tambah pada mata kuliah dasar pemrograman ini

   ![image](https://github.com/user-attachments/assets/16ba4eac-2c32-4b65-a017-25a27deeec5e)
   
   ini merupakan username dan password yang sudah saya tentukan sebelumnya
  
![image](https://github.com/user-attachments/assets/f13bc8c0-8f39-48ec-80fb-087fc0551f5b)

  pada kode di atas ini merupakan kode untuk input username dan password

![image](https://github.com/user-attachments/assets/8474561b-dd86-4b59-bb92-b41f29b35ea1)

ini merupakan proses percabangan untuk menentukan apakah password yang diinputkan user sudah benar atau tidak, jika tidak benar, maka user akan mengulang dari halaman login

![image](https://github.com/user-attachments/assets/1e15bf8b-cede-4d1f-989f-e1295f0d2bde)

pada kode ini saya sengaja memberikannya untuk menyambut user, seperti yang ada di web SIPLO

![image](https://github.com/user-attachments/assets/24061ae8-e160-4bbd-a9a5-2c220fdeae71)

pada input ini digunakan untuk memasukkan gaji dan jam kerja dari user

![image](https://github.com/user-attachments/assets/d9cfa5de-f5c7-403c-bc08-2585ee1f5d42)

pada percabangan ini saya menggunakan 0.10 untuk memberi bonus dari user, karena nilainya sama dengan 10%
di percabangan ini akan ada 3 output pertama dari output jam kerja > 160 akan ada output bonus yang didapatkan dan jumlah Gaji yang telah ditambahkan oleh bonus
pada output else atau Gaji < 160, hanya akan ada output Anda tidak mendapatkan bonus

![image](https://github.com/user-attachments/assets/153d9fee-3e64-4b6b-8999-c200e2b27155)

pada bagian ini user akan mendapatkan pilihan, apakah ingin menghitung gaji ulang apa tidak, jika ya maka user akan kembali ke halaman login
jika tidak, maka user akan mendapatkan output terimakasih, dan keluar dari program, tambahan saya menggunakan lower() agar input user menjadi kecil semua
sebagai contoh, jika user ngetik Ya/YA/yA, maka inputnya akan menjadi ya, berfungsi untuk if else pada program selanjutnya (program itu sangat rawan, typo dikit aja eror)

![image](https://github.com/user-attachments/assets/f52aa691-0fb2-4735-8afd-f9aef50835a4)

ada program ini untuk memproses input user, jika ya maaka user memilih untuk menghitung gaji ulang, jika tidak maka user memilih tidak ingin menghitung ulang gaji dan program selesai.

3. output/hasil program
![image](https://github.com/user-attachments/assets/3cc6c9bd-320a-4ca2-98b7-58aa42891704)
hasil program jika password benar dan user memilih untuk tidak menghitung ulang Gaji

![image](https://github.com/user-attachments/assets/43493622-7192-4df1-875f-9b94e80d8c0d)
hasil jika username dan password/username atau password salah

![image](https://github.com/user-attachments/assets/f6411f7e-430e-44cb-ae46-91db1707dd1f)
hasil jika username dan password benar dan user memilih untuk menghitung ulang gaji



sekian program saya, terimakasih!!
