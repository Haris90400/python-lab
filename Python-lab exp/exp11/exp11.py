import os

f=open("demofile.txt","w")
msg = input("Enter a line: ")

f.write(msg +"\n")
f.close()
f=open("demofile.txt","r")
f1=open("writefile.txt","w")

for l in f.read():
    f1.write(l)
f1.close()

f1=open("writefile.txt","a")
msg="append line"
f1.write(msg)
f1.close()

f1=open("writefile.txt","r")
wc,lc,cc=0,0,0

for l in f1:
    lc = lc+1
wc=wc+len(l.split())
cc=cc+len(l)
print(lc,wc,cc)
print(lc,"::", wc,"::", cc)
f.close()
f1.close()

for p,d,f in os.walk("."):
    print(f)