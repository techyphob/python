import urllib.request, urllib.parse

u = 'https://mediaroomlive.blob.core.windows.net/15-09-2018-9b5dc08ab9/PIC0'
for i in range(1,143):
    d = '{0:0>3}'.format(str(i))
    print(d)
    f = urllib.request.urlopen(u+d+'.JPG').read()
    with open('./skydive/pic0'+d+'.jpg','wb') as o:
        o.write(f)
    o.close()
    

