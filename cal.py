from numpy import *
from math import *

fov = 45 * math.pi /180
aspect = 16/9
n = 66.61
f = 160
A = mat(([-40],[8.977],[-114.269],[1]))
B = mat(([-38.903],[5.287],[-106.719],[1]))
P = mat(([1/aspect*math.tan(fov),0,0,0],[0,1/math.tan(fov),0,0],[0,0,f/(f-n),1],[0,0,f*n/(n-f),0]))
     #     P = mat(([1/(aspect*math.tan(fov/2)),0,0,0],[0,1/math.tan(fov/2),0,0],[0,0,(f+n)/(n-f),2*f*n/(n-f)],[0,0,-1,0]))

# a represents the point after perspective transformation
# A represents the point before perspective transformation
     
a = P*A
#A = P.I * a
b = P*B

a = a/a[3]
b = b/b[3]
     

print('a=',a)
print('b=',b)

