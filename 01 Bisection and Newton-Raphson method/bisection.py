def f(x):
    return (x**2-3)
def bisection(a, b, tol):
  if f(a)*f(b)>=0:
     print("Bisection method fails")
     return None
  while (b-a/2.0>tol):
      c=(a+b)/2.0
      if f(c)==0:
         return c
      elif f(a)*f(c)<0:
         b=c
      else:
         a=c
      return(a+b)/2.0
a=1
b=2
tol=0.000001
root=bisection(a, b, tol)
if root is not None:
   print(f"Approximate root:{root}")