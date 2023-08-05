import os
import marshal
import zlib
import base64

try:
    lokasi_file = input("Masukkan lokasi file: ")
except KeyboardInterrupt:
    print("Proses kompilasi dibatalkan.")
    exit()

try:
    nama_file_keluaran = input("Masukkan nama file keluaran: ")
except KeyboardInterrupt:
    print("Proses kompilasi dibatalkan.")
    exit()

if not nama_file_keluaran.endswith(".py"):
    nama_file_keluaran += ".py"

try:
    with open(lokasi_file, "r") as file_sumber:
        kode_sumber = file_sumber.read()

    kode_terkompilasi = compile(kode_sumber, "", "exec")

    for i in range(14):
        try:
            data_marshal = marshal.dumps(kode_terkompilasi)
            data_terkompresi = zlib.compress(data_marshal)
            data_terenkripsi = base64.b64encode(data_terkompresi)
            kode_terkompilasi = marshal.loads(zlib.decompress(base64.b64decode(data_terenkripsi)))
        except KeyboardInterrupt:
            print("Proses kompilasi dibatalkan.")
            exit()

    if os.path.exists(nama_file_keluaran):
        try:
            pilihan = input(f"File {nama_file_keluaran} sudah ada. Apakah Anda ingin menimpanya? (y/n): ")
            if pilihan.lower() != "y":
                print("Proses kompilasi dibatalkan.")
                exit()
        except KeyboardInterrupt:
            print("Proses kompilasi dibatalkan.")
            exit()

    with open(nama_file_keluaran, "w") as file_keluaran:
        file_keluaran.write(
            f"#-------------------------------------------------\n"
            f"#!/usr/bin/env python\n"
            f"# Dikompilasi oleh FII14\n"
            f"# https://github.com/FII14/PSP\n"
            f"#-------------------------------------------------\n\n"
            f"import base64, zlib, marshal\n"
            f"exec(marshal.loads(zlib.decompress(base64.b64decode({repr(data_terenkripsi)}))))\n"
        )

    print(f"File berhasil dikompilasi: {nama_file_keluaran}\n")

except FileNotFoundError:
    print(f"File tidak ditemukan: {lokasi_file}. Pastikan Anda memasukkan lokasi file yang benar.")

except Exception as e:
    print(f"Terjadi kesalahan: {str(e)}")

try:
    input("Tekan Enter untuk keluar...")
except KeyboardInterrupt:
    print("Proses kompilasi dibatalkan.")
