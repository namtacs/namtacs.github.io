from PIL import Image
#char range - cp-1251   33-151
WIDTH = 100
MAX_VALUE = 151-35
ENC_START = 35
import sys
im = Image.open(sys.argv[1])
print(im.format, im.size, im.mode)
height = int(im.size[1]/im.size[0]*WIDTH)
im = im.resize((WIDTH, height),Image.Resampling.LANCZOS).convert("1")
print(im.size)
im.show()
data = im.getdata()
out = []
num=0
prev=True
def write_num(num):
    global out
    if num > MAX_VALUE:
        while (num:=num-MAX_VALUE) > 0:
            out.append(MAX_VALUE)
            out.append(0)
        out.append(num+MAX_VALUE)
    else:
        out.append(num)
for p in data:
    p=p>=127
    if prev!=p:
        write_num(num)
        prev = p
        num = 1
        continue
    num+=1
write_num(num)
out=bytes([i+ENC_START for i in out]).decode("cp1251")
print(len(out))
print(out)

