from socket import *
import socket
import threading
import logging
import time
import sys
import json
import base64
import os

from file_protocol import FileProtocol

fp = FileProtocol()

class ProcessTheClient(threading.Thread):
    """Kelas untuk menangani setiap client yang terhubung"""
    def __init__(self, connection, address):
        super().__init__()
        self.connection = connection  # Menyimpan koneksi socket
        self.address = address       # Menyimpan alamat client

    def run(self):
        """Method yang dijalankan saat thread dimulai"""
        try:
            buffer = b''
            while True:
                chunk = self.connection.recv(4096)
                if not chunk:
                    break
                buffer += chunk
                # Cek delimiter akhir perintah (CRLF CRLF)
                if b"\r\n\r\n" in buffer:
                    break

            if not buffer:
                return

            # Pisahkan header (perintah) dan body (payload) jika ada
            # Misal: "UPLOAD filename <base64>"
            raw = buffer.decode(errors='ignore').strip()
            parts = raw.split(' ', 2)
            cmd = parts[0].lower()

            # UPLOAD
            if cmd == 'upload' and len(parts) == 3:
                filename = parts[1]
                payload_b64 = parts[2]
                try:
                    data = base64.b64decode(payload_b64)
                except Exception as e:
                    resp = {"status": "ERROR", "data": "Invalid base64 payload"}
                    self.connection.sendall((json.dumps(resp) + "\r\n\r\n").encode())
                    return

                # Pastikan direktori files ada
                os.makedirs('files', exist_ok=True)
                filepath = os.path.join('files', filename)
                with open(filepath, 'wb') as f:
                    f.write(data)

                resp = {"status": "OK", "data": f"{filename} berhasil diupload"}
                self.connection.sendall((json.dumps(resp) + "\r\n\r\n").encode())

            # DOWNLOAD atau perintah lain
            else:
                # gunakan protokol umum
                hasil = fp.proses_string(raw)
                # jika download, kirim sesuai protokol
                if isinstance(hasil, dict) and hasil.get('is_download'):
                    header = f"DOWNLOAD {hasil['data_namafile']}\r\n"
                    self.connection.sendall(header.encode())
                    # kirim file base64
                    self.connection.sendall(hasil['data_file'].encode())
                    self.connection.sendall(b"\r\n\r\n")
                else:
                    resp_text = hasil + "\r\n\r\n"
                    self.connection.sendall(resp_text.encode())

        finally:
            self.connection.close()

class Server(threading.Thread):
    """Kelas utama server yang menangani koneksi masuk"""
    def __init__(self, ipaddress='0.0.0.0', port=8889):
        super().__init__()
        self.ipinfo = (ipaddress, port)  # Menyimpan info IP dan port
        self.the_clients = []            # List untuk menyimpan client
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        """Method yang dijalankan saat thread server dimulai"""
        logging.warning(f"server berjalan di ip address {self.ipinfo}")
        self.my_socket.bind(self.ipinfo)
        self.my_socket.listen(5)
        while True:
            connection, client_address = self.my_socket.accept()
            logging.warning(f"connection from {client_address}")

            clt = ProcessTheClient(connection, client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    """Fungsi utama untuk menjalankan server"""
    svr = Server(ipaddress='0.0.0.0', port=46666)
    svr.start()
    svr.join()

# Jalankan main() jika file dijalankan langsung
if __name__ == '__main__':
    main()
