def f(x):
    return (x**2-2)
def df(x):
    return (2*x)
def newton_raphson(x0,tol, max_iter):
    for i in range(max_iter):
        f_x0=f(x0)
        df_x0=df(x0)
        if df_x0==0:
           print("Zero Derivative")
           return None
        x1=x0-f_x0/df_x0
        if abs(x1-x0)<tol:
           return x1
        x0=x1
    print("Exceeded maximum iteration")
    return None
x0=1
tol=0.000001
max_iter=20
root=newton_raphson(x0,tol, max_iter)
if root is not None:
   print(f"Approximate root:{root}")
