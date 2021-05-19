x= input("Enter sentence: ")
y=x.split()
xff=0
w=len(x.split())
for w in y:
   p= w.split()
   w= len(p[0])
   xff=xff+w
print("Total Words: "+w)
print("Total Characters: "+xff)
