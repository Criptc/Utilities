import zlib
import shutil
from os import rename
import os
from time import sleep

#Thanks to jan0809#5705 on the python discord for help with debugging

file_types = {
    'exe': 0xFF,
    'py': 0xFE,
    'txt': 0xFD,
    'bat': 0xFC,
    'cmd': 0xFC,
    'png': 0xFB,
    'jpg': 0xFA,
    'pdf': 0xF9,
    'bin': 0xF8
 }

def compress():
    # get file to compress
    inp = input('file to compress: ')
    with open(inp, 'rb') as f:
        Bytes = f.read() # get bytes of the file
    #-----add file extention to the end of the bytes-----#
    ext = inp.split('.')[-1].lower()
    if ext in file_types:
        filetype = [file_types[ext]]
        filename = inp.replace(f'.{ext}', '.ecf')
    else:
        raise Exception('unknown file extention')
    #-----add file extention to the end of the bytes-----#
    Bytes = zlib.compress(Bytes) + bytearray(filetype) # combind the bytes compressed and the filetype bytes
    with open(filename, 'wb') as f:
        f.write(Bytes) # write the compressed bytes to the file
   

def decompress():
    inp = input('file to decompress: ')
    if not inp.endswith('.ecf'):
        raise Exception('Can\'t decompress non .ecf filetype')
    with open(inp, 'rb') as f:
        Bytes = f.read()
    filetype = int.from_bytes(Bytes[-1:], byteorder='little')
    Bytes = Bytes[:len(Bytes) - 1]
    Data = zlib.decompress(Bytes)
    if filetype in list(file_types.values()):

        filetype = f'.{list(file_types.keys())[list(file_types.values()).index(filetype)]}'
    with open(inp, 'wb') as f:
        f.write(Data)
    filename = inp.replace('.ecf', '')  + filetype
    os.rename(inp, filename)