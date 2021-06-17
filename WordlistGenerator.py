#coding:utf-8
import itertools
import argparse
import string
import time
import sys

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description='Python Wordlist Generator')
parser.add_argument('-chr', '--chars',default=None, help='kullanilacak karakterler')
parser.add_argument('-min', '--min', type=int,default=1, help='minimum karakter uzunlugu')
parser.add_argument('-max', '--max', type=int,default=5, help='maximum karakter uzunlugu')
parser.add_argument('-out', '--output',default='wordlist.txt', help='kayitlanacak dosya yolu.')
data = parser.parse_args()

if data.chars is None:
   data.chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
   
if data.min > data.max:
      exit(u"[!] minimum değer maximum değerden küçük olmalıdır!")

output = open(data.output, 'w')

for n in range(data.min, data.max + 1):
    for xxx in itertools.product(data.chars, repeat=n):
            chars = ''.join(xxx)
            output.write(chars+"\n")
            sys.stdout.write('\r[+] kelime: '+chars)
            sys.stdout.flush()

print(u'\n[i] Bitiş Tarihi: '+time.strftime('%H:%M:%S'))