from numpy import *
from math import *

fov = 37.97 * math.pi /180
aspect = 16/9
n = 1
f = 30
A = mat(([-40],[8.977],[-114.269],[1]))
B = mat(([-38.903],[5.287],[-106.719],[1]))
P = mat(([1/aspect*math.tan(fov),0,0,0],[0,1/math.tan(fov),0,0],[0,0,f/(f-n),1],[0,0,f*n/(n-f),0]))
     #     P = mat(([1/(aspect*math.tan(fov/2)),0,0,0],[0,1/math.tan(fov/2),0,0],[0,0,(f+n)/(n-f),2*f*n/(n-f)],[0,0,-1,0]))

# a represents the point after perspective transformation
# A represents the point before perspective transformation
# a & A are at the same coordinate system (eye/camera)
     
a = P*A
#A = P.I * a
b = P*B

a = a/a[3]
b = b/b[3]
     

print('a=',a)
print('b=',b)



#___________________________

g = mat(([100],[1000],[1],[1])) #g is the coordinate that you GET

G = P.I * g

r = 2.871

YG = float(G[2])
ZG = YG/math.tan(fov) - 2*r

O = mat(([0],[-0.059*math.cos(fov)],[-2*r+0.059*math.sin(fov)]))

T = mat(([0],[-0.059*math.cos(fov)+r*math.sin(fov)],[-2*r+0.059*math.sin(fov)-r*math.cos(fov)]))

