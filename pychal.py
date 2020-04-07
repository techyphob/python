import re
import urllib.request, urllib.parse
import pickle
import os
import zipfile
from PIL import Image, ImageDraw
import bz2
from itertools import groupby

#with open('input.txt','r') as inf:
#    s = inf.readline()
#inf.close()

#print (''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', s)))

#for i in range(0,len(s)): 
#    ss = s[i:i+9]
#    if ss[0].islower() and ss[1:4].isupper()  and ss[4].islower() and ss[5:8].isupper() and ss[8].islower():
#        print (ss)


#u = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
#d= dict(nothing="12345")
#d = '12345'
#d = '8022'
#d = '63579'
#req = urllib.request.Request(u,data=urllib.parse.urlencode(d).encode("utf-8"))
#req = urllib.request.Request(u + d)
#f = urllib.request.urlopen(u + d).read()
#while 'next' in f.decode("utf-8") :
#    d = re.findall('[0-9]+',f.decode("utf-8"))
#    f = urllib.request.urlopen(u + ''.join(d)).read()
#    print (d)
#t=f.read()
#nd = t[-5:]
#print (t[8:12])

#with open('banner.p','rb') as f:
#    f = pickle.load(f)
#    for l in f:
#        for i in l:
#            print (i[0]*i[1],end='')
#        print ('')
#z = zipfile.ZipFile('D:\Dan\Downloads\channel.zip')
#comments = []
#d = '90052'
#lin = z.read(d+'.txt').decode('utf-8')
#while 'Next' in lin:
#    comments.append(z.getinfo(d+'.txt').comment.decode("utf-8"))  
#    d = ''.join(re.findall('[0-9]+',lin))
#    lin = z.read(d+".txt").decode("utf-8")
#print (''.join(comments))
#possible = []
#img = Image.open("oxygen.png")
#row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
#ords = [r for r,g,b,a in row[::7] if r==g==b]
#nums = re.findall('\d+',''.join(map(chr,ords)))
#print (''.join(map(chr,map(int,nums))))


#un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
#print(bz2.decompress(un))
#print(bz2.decompress(pw))

#first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,332,155,348,156,353,153,366,149,379,147,394,146,399]
#second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,158,121,157,128,156,134,157,136,156,136]
#im = Image.new('RGB', (500,500))
#draw = ImageDraw.Draw(im)
#draw.polygon(first, fill='red')
#draw.polygon(second, fill='white')
#im.show()

#def lookandsay(num):
#    return ''.join(str(len(list(g)))+k for k,g in groupby(num))
#lands = lookandsay('1')
#for i in range(2,31):
#    lands = lookandsay(lands)
#    print (str(i)+'\t'+str(len(lands)))

#im = Image.open('cave.jpg')
#(w,h) = im.size

#even = Image.new('RGB',(w//2,h//2))
#odd = Image.new('RGB',(w//2,h//2))
#for i in range(w):
#    for j in range(h):
#        p = im.getpixel((i,j))
#        if (i+j)%2 == 1:
#            odd.putpixel((i // 2, j // 2), p)
#        else:
#            even.putpixel((i // 2, j // 2), p)
#even.save('even.jpg')
#odd.save('odd.jpg')

#data = open('evil2.gfx','rb').read()
#for i in range(5):
#    open('%d.jpg' % i , 'wb').write(data[i::5])

#import xmlrpc.client
#conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
#conn.system.listMethods()
#conn.system.methodHelp('phone')
#conn.system.methodSignature('phone')
#print (conn.phone('Bert'))

im = Image.open('wire.png')
delta = [(1,0),(0,1),(-1,0),(0,-1)]
out = Image.new('RGB',[100,100])
x,y,p = -1,0,0
d = 200 
while d/2>0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y),im.getpixel((p,0)))
            p += 1
        d -= 1
out.save('level_14_result.jpg')








