import os
import marshal
import zlib
import base64

def compile_file():
    try:
        file_location = input('Enter your file location: ')
    except KeyboardInterrupt:
        print('Compilation process canceled.')
        return

    try:
        output_file_name = input('Enter the output file name: ')
    except KeyboardInterrupt:
        print('Compilation process canceled.')
        return

    if not output_file_name.endswith('.py'):
        output_file_name += '.py'

    try:
        with open(file_location, 'r') as source_file:
            source_code = source_file.read()

        compiled_code = compile(source_code, '', 'exec')

        for i in range(14):
            try:
                data_marshal = marshal.dumps(compiled_code)
                compressed_data = zlib.compress(data_marshal)
                encoded_data = base64.b64encode(compressed_data)
                compiled_code = marshal.loads(zlib.decompress(base64.b64decode(encoded_data)))
            except KeyboardInterrupt:
                print('Compilation process canceled.')
                return

        if os.path.exists(output_file_name):
            try:
                choice = input(f'File {output_file_name} already exists. Do you want to overwrite it? (y/n): ')
                if choice.lower() != 'y':
                    print('Compilation process canceled.')
                    return
            except KeyboardInterrupt:
                print('Compilation process canceled.')
                return

        with open(output_file_name, 'w') as output_file:
            output_file.write(
                f"#-------------------------------------------------\n"
                f"#!/usr/bin/env python\n"
                f"# Compiled by FII14\n"
                f"# https://github.com/FII14/PSP\n"
                f"#-------------------------------------------------\n\n"
                f"import base64, zlib, marshal\n"
                f"exec(marshal.loads(zlib.decompress(base64.b64decode({repr(encoded_data)}))))\n"
            )

        print(f'File successfully compiled: {output_file_name}\n')

    except FileNotFoundError:
        print(f'File not found: {file_location}. Please make sure you enter the correct file location.')

    except Exception as e:
        print(f'An error occurred: {str(e)}')

try:
    compile_file()
except KeyboardInterrupt:
    print('Compilation process canceled.')
