avg=int(input())
a1,a2=0,1
print(a2,end=" ")
for i in range(1,avg):
  a3=a1+a2
  print(a3,end=" ")
  a1,a2=a2,a3
  
