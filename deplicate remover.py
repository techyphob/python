#!/usr/bin/env python

import hashlib
import os
import glob
import shutil

def hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
    for block in bytesiter:
        hasher.update(block)
    return hasher.hexdigest() if ashexstr else hasher.digest()

def file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)

#file_path = "D:/Dan/Pictures/Mixed photos/"
file_path = "D:/Dan/Pictures/School/test/"
out_path = file_path+"duplicates/"
if os.path.exists(out_path):
    shutil.rmtree(out_path)
file_list  = glob.iglob(file_path+"*")

hashes = [(hash_bytestr_iter(file_as_blockiter(open(fname, 'rb')), hashlib.md5(),True),fname) for fname in file_list]

os.mkdir(out_path)

duplicates = {}
for i in range (0,len(hashes)):
    for j in range (i+1, len(hashes)):
        if hashes[i][0] == hashes[j][0]:
            if hashes[i][0] in duplicates:
                duplicates[hashes[i][0]].add(hashes[j][1])
            else:
                duplicates[hashes[i][0]] = {hashes[i][1],hashes[j][1]}
outf =  open(out_path+'duplicates.txt','w')
for k in duplicates:
    outf.write(k+":\t")
    if len(duplicates[k]) > 1:
        a = duplicates[k].pop()
        outf.write(a+"\t")
    for f in duplicates[k]:
        outf.write(f+"\t")
        o = f.replace(file_path[:-1]+"\\",out_path)
        shutil.move(f,o)
    outf.write("\n")
outf.close()
file_list = None
hashes = None
