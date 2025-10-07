import math
x=[0,1,2,3,4,5]
y=[0,1,8,27,64,125]
h=x[1]-x[0]
def forward_difference_table(x,y):
  n=len(y)
  diff_table=[y.copy()]
  for i in range (1,n):
    row=[]
    for j in range (n-i):
      delta=diff_table[i-1][j+1]-diff_table[i-1][j]
      row.append(delta)
    diff_table.append(row)
  return diff_table
print("forward difference table:")
diff_table=forward_difference_table(x,y)
for row in diff_table:
   print(row)
x_test=1.5
p=(x_test-x[0])/h
dy=(1/h)*(diff_table[1][0]+((2*p-1)/math.factorial(2))*diff_table[2][0]+((3*p**2-6*p+2)/math.factorial(3))*diff_table[3][0])
d2y=(1/h**2)*(diff_table[2][0]+(p-1)*diff_table[3][0])
print(f"At x={x_test}:")
print(f"First derivative(dy/dx)≈{dy}")
print(f"Second derivative (d²y/dx²)≈{d2y}")





