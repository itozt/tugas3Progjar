# Tugas 3 Pemrograman Jaringan
Langkah - Langkah Pengerjaan 
## 1. Edit File file_server.py di Mesin 1
Ganti dari port 6666 menjadi port 46666. <br>
Dan ubah `data = self.connection.recv(32)` menjadi `data = self.connection.recv(4096)` <br>
```
vim file_server.py
```
![Screenshot 2025-05-22 181013](https://github.com/user-attachments/assets/59cd8a9d-8fd4-4a36-9cd0-b51326701245)

## 2. Edit File file_interface.py
Ganti file asli menjadi file modifikasi yang sudah ada fungsi untuk menghaspu dan mengupload file.<br>
Gunakan command 
```
vim file_interface.py
```
![Screenshot 2025-05-21 215653](https://github.com/user-attachments/assets/cefc5ccc-6282-46c4-b705-f7e009c9f805)
## 3. Install Netcat
Gunakan command
```
sudo apt install netcat
```
## 4. Lakukan Client Implementation dari operasi tambahan tersebut
### 🌴 : LIST
Tujuan : menampilkan list file yang terdapat pada direktori /files <br>
Command : ```LIST```
![Screenshot 2025-05-21 222928](https://github.com/user-attachments/assets/d961a913-d1c3-4af6-a97e-4fbc215df341)
### 🌴 : GET 
Tujuan : mengunduh file berupa encode base64<br>
Command : ```GET [nama_file.tipe_file]```
![Screenshot 2025-05-21 223416](https://github.com/user-attachments/assets/3e95e5fc-3523-4e43-96ab-cf58fe224d71)
### 🌴 : DELETE
Tujuan : menghapus file yang ada di direktori /files <br>
Command : ```DELETE [nama_file.tipe_file]```
![Screenshot 2025-05-21 223636](https://github.com/user-attachments/assets/156aefe4-e0f3-48dc-95c4-e23021274abd)
### 🌴 : UPLOAD
Tujuan : mengunggah/mengupload file ke direktori /files<br>
Command : ``` ```


