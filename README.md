# Tugas 3 Pemrograman Jaringan

# Daftar Isi
Langkah - Langkah Pengerjaan
1. [Edit File file_server.py]()
2. [Edit File file_protocol.py]()
3. [Edit File file_interface.py]()
4. [Install Netcat]()
5. [Lakukan Client Implementation]()

Penjelasan Program File Baru
1. [file_Server.py]()
2. [file_protocol.py]()
3. [file_interface.py]()

Langkah - Langkah Pengerjaan 
## 1. Edit File file_server.py di Mesin 1
Ganti port dari 6666 menjadi port 46666. <br>
Dan ubah `data = self.connection.recv(32)` menjadi `data = self.connection.recv(4096)` <br>
Gunakan command 
```
vim file_server.py
```
![Screenshot 2025-05-22 181013](https://github.com/user-attachments/assets/59cd8a9d-8fd4-4a36-9cd0-b51326701245)

## 2. Edit File file_protocol.py di Mesin 1
Ubah `c = shlex.split(string_datamasuk.lower())` menjadi `c = shlex.split(string_datamasuk)` <br>
Gunakan command 
```
vim file_protocol.py
```
![Screenshot 2025-05-22 181425](https://github.com/user-attachments/assets/766d89ff-b725-47b4-9ef7-5a9fd4d15c32)

## 3. Edit File file_interface.py di Mesin 1
Ganti file asli menjadi file modifikasi yang sudah ada fungsi untuk menghaspu dan mengupload file.<br>
Gunakan command 
```
vim file_interface.py
```
![Screenshot 2025-05-21 215653](https://github.com/user-attachments/assets/cefc5ccc-6282-46c4-b705-f7e009c9f805)
## 4. Install Netcat
Gunakan command
```
sudo apt install netcat
```
## 5. Lakukan Client Implementation dari operasi tambahan tersebut
Pada terminal 1 : Jalankan command `python3 file_server.py` <br>
Pada terminal 2 : Jalankan command `nc -vvv 127.16.16.101 46666` <br>
### 🌴 : LIST
Tujuan : menampilkan list file yang terdapat pada direktori /files <br>
Command : ```list```<br>
Hasil : <br>
![List](https://github.com/user-attachments/assets/97bb8921-7873-41b3-ab27-765fe2795d12)
### 🌴 : GET 
Tujuan : mengunduh file berupa encode base64<br>
Command : ```get [nama_file.tipe_file]```<br>
Hasil : <br>
![Get](https://github.com/user-attachments/assets/136228ea-9cca-48a3-ae02-645af8f38e60)
### 🌴 : DELETE
Tujuan : menghapus file yang ada di direktori /files <br>
Command : ```delete [nama_file.tipe_file]```<br>
Hasil : <br>
![Delete](https://github.com/user-attachments/assets/2c0887bf-3e8a-44d5-8ad5-5bdecbb3de68)
### 🌴 : UPLOAD
Tujuan : mengunggah/mengupload file ke direktori /files<br>
Command : ```upload [namafile.tipefile] [encodebase64 dari isi file yang inign diupload]``` <br>
Hasil : <br>
![Upload](https://github.com/user-attachments/assets/9369f351-9a13-4525-8fad-0fe4f38e6f06)


