import os
import marshal

def kompilasi_file():
    # Meminta lokasi file dan nama file keluaran dari pengguna
    lokasi_file = input('Masukkan lokasi file Anda: ')
    nama_file_keluaran = input('Masukkan nama file keluaran: ')

    # Memastikan ekstensi file keluaran adalah .py
    if not nama_file_keluaran.endswith('.py'):
        nama_file_keluaran += '.py'

    try:
        # Membaca isi file sumber
        with open(lokasi_file, 'r') as file_sumber:
            kode_sumber = file_sumber.read()

        # Melakukan kompilasi kode sumber menjadi objek kode kompilasi
        kode_kompilasi = compile(kode_sumber, '', 'exec')

        # Melakukan marshal (serialisasi) terhadap objek kode kompilasi
        data_marshal = marshal.dumps(kode_kompilasi)

        # Memeriksa apakah file keluaran sudah ada
        if os.path.exists(nama_file_keluaran):
            pilihan = input(f'File {nama_file_keluaran} sudah ada. Apakah Anda ingin menimpanya? (y/n): ')
            if pilihan.lower() != 'y':
                print('Proses kompilasi dibatalkan.')
                return

        # Menulis kode keluaran ke dalam file keluaran
        with open(nama_file_keluaran, 'w') as file_keluaran:
            file_keluaran.write('# Dikompilasi oleh FII14\n')
            file_keluaran.write('# https://github.com/FII14/kompilasi-marshal\n\n')
            file_keluaran.write('import marshal\n')
            file_keluaran.write(f'exec(marshal.loads({repr(data_marshal)}))\n')

        # Menampilkan pesan berhasil jika proses kompilasi selesai
        print(f'File berhasil dikompilasi: {nama_file_keluaran}\n')

    except FileNotFoundError:
        # Menangani kesalahan jika file sumber tidak ditemukan
        print('File tidak ditemukan. Pastikan lokasi file yang Anda masukkan benar.')

    except Exception as e:
        # Menangani kesalahan umum dan menampilkan pesan kesalahan
        print(f'Terjadi kesalahan: {str(e)}')

# Memanggil fungsi kompilasi_file untuk menjalankan proses kompilasi
kompilasi_file()
