CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = u"Hello World\n"
bytes_out = hello_out.encode(CODEC)
f=open(FILE,"wb")
f.write(bytes_out)
f.close()

f=open(FILE,"rb")
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print(hello_in)
