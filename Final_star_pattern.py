#Final star pattern program:
a=int(input("enter no of rows of the triangle in the star pattern:"))
for i in range(1,a+1):
    print((' '*((3*a)-i-1))+('*'*((2*i)-1)))
for i in range(a+1,1,-1):
    print((' '*(a-i+1))+('*'*((2*i)-3))+(' '*((4*a)+1-(2*i)))+('*'*((2*i)-3))+(' '*(a-i)))
for i in range(2,a+1):
    print(' '*(a-i)+('*'*((2*i)-1))+(' '*((4*a)-1-(2*i)))+('*'*((2*i)-1))+' '*(a-i-1))
for i in range(a+1,1,-1):
    print((' '*((3*a)-i))+('*'*((2*i)-3)))
