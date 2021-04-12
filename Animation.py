import numpy as np
from matplotlib import pyplot as plt


from matplotlib.animation import FuncAnimation, PillowWriter



def linea2(a):
	plt.plot([x[lista[a]],x[lista[a+1]]],[y[lista[a]],y[lista[a+1]]],"k",linewidth=0.1)	


with open("lista de puntos.txt","r") as file:
	content=file.readlines()

content = [x.strip() for x in content] 

for i in range(len(content)):
	content[i]=content[i]+" "

content[0:len(content)]= [''.join(content[0:len(content)])]


string=content[0].split(", ")
string=string[:len(string)-1]
for j in range(len(string)):
	string[j]=int(string[j])

lista=string

n=306
num_lineas=2500
rad = 250*3
cx = 0
cy = 0
actual=0
angulo = np.linspace(0, 2*np.pi, n+1)
x = rad * np.cos(angulo) + cx
y = rad * np.sin(angulo) + cy

lista=lista

fig, ax = plt.subplots()

plt.plot(x, y, 'ro',markersize=1)

plt.gca().set_aspect('equal')

ani = FuncAnimation(fig,func=linea2,frames=len(lista)-1,
                    interval=1)

ani.save("animation.gif", writer=PillowWriter(fps=30))