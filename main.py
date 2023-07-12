import os, marshal, zlib, base64

def kompilasi_file():
    try:
        lokasi_file = input('Masukkan lokasi file Anda: ')
    except KeyboardInterrupt:
        print('Proses kompilasi dibatalkan.')
        return

    try:
        nama_file_keluaran = input('Masukkan nama file keluaran: ')
    except KeyboardInterrupt:
        print('Proses kompilasi dibatalkan.')
        return

    if not nama_file_keluaran.endswith('.py'):
        nama_file_keluaran += '.py'

    try:
        with open(lokasi_file, 'r') as file_sumber:
            kode_sumber = file_sumber.read()

        kode_kompilasi = compile(kode_sumber, '', 'exec')

        for i in range(14):
            try:
                data_marshal = marshal.dumps(kode_kompilasi)
                data_kompresi = zlib.compress(data_marshal)
                data_base64 = base64.b64encode(data_kompresi)
                kode_kompilasi = marshal.loads(zlib.decompress(base64.b64decode(data_base64)))
            except KeyboardInterrupt:
                print('Proses kompilasi dibatalkan.')
                return

        if os.path.exists(nama_file_keluaran):
            try:
                pilihan = input(f'File {nama_file_keluaran} sudah ada. Apakah Anda ingin menimpanya? (y/n): ')
                if pilihan.lower() != 'y':
                    print('Proses kompilasi dibatalkan.')
                    return
            except KeyboardInterrupt:
                print('Proses kompilasi dibatalkan.')
                return

        with open(nama_file_keluaran, 'w') as file_keluaran:
            file_keluaran.write(f"# Dikompilasi oleh FII14\n# https://github.com/FII14/kompilasi-marshal\n\nimport base64, zlib, marshal;exec(marshal.loads(zlib.decompress(base64.b64decode({repr(data_base64)}))))\n")

        print(f'File berhasil dikompilasi: {nama_file_keluaran}\n')

    except FileNotFoundError:
        print(f'File tidak ditemukan: {lokasi_file}. Pastikan lokasi file yang Anda masukkan benar.')

    except Exception as e:
        print(f'Terjadi kesalahan: {str(e)}')

try:
    kompilasi_file()
except KeyboardInterrupt:
    print('Proses kompilasi dibatalkan.')
    
