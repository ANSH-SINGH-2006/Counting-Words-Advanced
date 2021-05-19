x= input("Enter sentence: ")
y=x.split()
xff=0

for w in y:
   p= w.split()
   w= len(p[0])
   xff=xff+w

print("Total Words: ")
w=len(x.split())
print(w)
print("Total Characters: ")
print(xff) 
