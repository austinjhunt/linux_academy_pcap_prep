#!/usr/bin/env python3.7
# r = read
# w = write (overwrite.)
# r+ = read and write
# r+t = read, gives you text back
# r+b = read, gives you binary (when to use? reading raw bytes from disk)
# w+ = truncate, read and write
# x = create
# + = if you're writing, gives you reading. if you're reading, gives you rwiritng.
# a = append

# What happens if you use open(file,'r').write("Hello")?
# io.UnsupportedOperation: not writable

# What happens if you use open(file,'r+').write("Hello")?
# 5 ???? what is that

f1 = open('xmen.txt','w+')
f1.write("Beast\n")
f1.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n'
])
# pass a list of lines to writelines. if you don't pass \n as nweline char to open() then you should include \n in all lines written.
# Always close when done.
print("f1.read() => {}".format(f1.read()))
print("returns nothing because cursor from open('w+') is at very end of file, and read() starts reading from cursor. Use seek to move cursor to specific position.")
print("f1.seek(0) => move cursor to beginning.")
f1.seek(0)
f1.write("Morph")
f1.seek(0)
print("f1.read() => \n{}".format(f1.read()))
f1.close()

f1 = open('xmen.txt','r')
print(f1.read())
f1.close()



f2 = open('xmen2.txt','w+',newline="\n")
f2.write("Beast")
f2.writelines([
    'Cyclops',
    'Bishop',
    'Nightcrawler'
])
f2.close()



with open('testfile.txt','w+') as f:
    f.write('file will close after this context.')
# same as
f = open('testfile.txt','w+')
with f:
    f.write('file will close after this context.')


with open('xmen.txt') as f:
    for line in f.readlines():
        print(line)