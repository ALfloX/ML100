# Linear s o l v e r
import numpy as np
def my_linfit( x , y ) :
    N=len(x)
    X=np.sum(x)
    Y=np.sum(y)
    XY=np.sum(x*y)
    XX=np.sum(x*x)
    a = (N*XY-X*Y)/(N*XX-X**2)
    b = (Y-a*X)/N
    return a , b
# Main
if __name__ == "__main__" :
    import matplotlib.pyplot as plt
    import numpy as np
    plt.title("Click to add points (press enter to finish, right to delete last point)")
    pts = plt.ginput(n=-1, timeout=0)
    pts = np.array(pts)
    if len(pts) < 2:
        print("Need 2 points")
    else:
        x = pts[:,0]
        y = pts[:,1]
    a , b = mylinfit( x , y )
    plt.plot( x , y , "kx" )
    xp = np.arange( -2 , 5 , 0.1 )
    plt.plot( xp , a*xp+b , "r-" )
    print(f"Myfit : a={a} and b={b}")
    plt.show( )