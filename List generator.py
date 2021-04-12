import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.image as mpimg
from PIL import Image, ImageDraw
from matplotlib.animation import FuncAnimation, PillowWriter
import math




	
def interp(x0, y0, x1, y1):
    """Uses Xiaolin Wu's line algorithm to interpolate all of the pixels along a
    straight line, given two points (x0, y0) and (x1, y1)

    """
    pixels = []
    steep = abs(y1 - y0) > abs(x1 - x0)


    if steep:
        t = x0
        x0 = y0
        y0 = t

        t = x1
        x1 = y1
        y1 = t

    if x0 > x1:
        t = x0
        x0 = x1
        x1 = t

        t = y0
        y0 = y1
        y1 = t

    dx = x1 - x0
    dy = y1 - y0
    gradiente = dy / dx  # gradiente


    x_end = round(x0)
    y_end = y0 + (gradiente * (x_end - x0))
    xpxl0 = x_end
    ypxl0 = round(y_end)
    if steep:
        pixels.extend([(ypxl0, xpxl0), (ypxl0 + 1, xpxl0)])
    else:
        pixels.extend([(xpxl0, ypxl0), (xpxl0, ypxl0 + 1)])

    interpolated_y = y_end + gradiente


    x_end = round(x1)
    y_end = y1 + (gradiente * (x_end - x1))
    xpxl1 = x_end
    ypxl1 = round(y_end)


    for x in range(xpxl0 + 1, xpxl1):
        if steep:
            pixels.extend([(math.floor(interpolated_y), x), (math.floor(interpolated_y) + 1, x)])

        else:
            pixels.extend([(x, math.floor(interpolated_y)), (x, math.floor(interpolated_y) + 1)])

        interpolated_y += gradiente


    if steep:
        pixels.extend([(ypxl1, xpxl1), (ypxl1 + 1, xpxl1)])
    else:
        pixels.extend([(xpxl1, ypxl1), (xpxl1, ypxl1 + 1)])

    return pixels





def numeros_no_posibles(a):
	lista_numeros=[]
	b=int(np.floor(n*0.1))
	if b%2==0: 
		b=b+1

	for i in range(int(b)):
		lista_numeros.append(((a-i)%(n)+int((b-1)/2))%n)

	return lista_numeros




def linea(a,b):
	plt.plot([x[a],x[b]],[y[a],y[b]],"k",linewidth=0.2)

def linea2(a):
	plt.plot([x[lista[a]],x[lista[a+1]]],[y[lista[a]],y[lista[a+1]]],"k",linewidth=0.2)	

def linea3(a):
	draw.line(((x[a]+rad,-y[a]+rad), (x[lista[a+1]]+rad,-y[lista[a+1]]+rad)), 
		fill=(255,255),width=1)

def promedio(cosita):
	total = 0
	for i in range(0, 412):
	    for j in range(0, 412):
	        total += cosita.getpixel((i,j))[0]

	mean = total / (412 * 412)
	return mean

def buscador(a,im):

	img=np.array(im)
	promedios=[]
	for i in range(n):
		base=img
		imagen_prueba=Image.fromarray(img)
		dibujar = ImageDraw.Draw(imagen_prueba) 
		if i in numeros_no_posibles(a) or i==lista[-2]:
			promedios.append(255)
		else:
			suma=0
			for j in interp(x[a],y[a],x[i],y[i]):
				c,b=j

				suma+=imagen_prueba.getpixel((int(c+rad),int(-b+rad)))[0]

			promedio=suma/len(interp(x[a],y[a],x[i],y[i]))
			promedios.append(promedio)
			


	return promedios.index(min(promedios))

def buscador2(a,im):

	img=np.array(im)
	promedios=[]
	for i in range(n):
		base=img
		imagen_prueba=Image.fromarray(img)
		dibujar = ImageDraw.Draw(imagen_prueba) 
		if i in numeros_no_posibles(a):
			promedios.append(255)

		else:
			suma=0
			for j in interp(x[a],y[a],x[i],y[i]):
				c,b=j

				suma+=imagen_prueba.getpixel((int(c+rad),int(-b+rad)))[0]

			promedio=suma/len(interp(x[a],y[a],x[i],y[i]))
			promedios.append(promedio)
			

	print(lista[-1])
	print(promedios.index(min(promedios)))



def linea_foto(a,b):
	draw.line(((x[a]+rad,-y[a]+rad), (x[b]+rad,-y[b]+rad)), 
		fill=(255,255,255),width=1)




n=int(input("inserte numero de puntos: "))
num_lineas=int(input("inserte el numero de lineas: "))
lista=[0,0,]
rad = 412*2/2-2
cx = 0
cy = 0
actual=0
angulo = np.linspace(0, 2*np.pi, n+1)
x = rad * np.cos(angulo) + cx
y = rad * np.sin(angulo) + cy



actual=0

plt.plot(x, y, 'ro',markersize=1)
plt.gca().set_aspect('equal')

ima= Image.open("imagen.png") 

ima=ima.resize((412*3,412*3))
ima=ima.convert('LA')
ima=ima.crop((412*3/6,412*3/6,5*412*3/6,5*412*3/6))

ima.save("grande_gris.png")

img=Image.open("grande_gris.png").convert("RGB")

npImage=np.array(img)


h,w=img.size

# Create same size alpha layer with circle
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0,0,h,w],0,360,fill=255)

# Convert alpha Image to numpy array
npAlpha=np.array(alpha)

# Add alpha layer to RGB
npImage=np.dstack((npImage,npAlpha))

# Save with alpha
Image.fromarray(npImage).save('result.png')


img2=Image.open('result.png') 
draw=ImageDraw.Draw(img2)

for i in range(num_lineas):



	b=buscador(actual,img2)
	linea_foto(actual,b)
	lista.append(b)
	linea(actual,b)
	"""
	if len(lista)>150:
		buscador2(actual,img2)
	"""


	actual=b


plt.axis("off")
with open("lista de puntos.txt","w") as new_file:
	j=1
	for i in lista:
		if j%20==0:
			new_file.write(str(i)+", "+"\n")
			j+=1

		else:
			new_file.write(str(i)+", ")
			j+=1







"""

actual=0
for j in range(len(lista)-1):

	draw.line(((x[actual]+rad,-y[actual]+rad), (x[lista[j+1]]+rad,-y[lista[j+1]]+rad)), 
		fill=(255,255),width=1)
	actual=lista[j+1]
	promedio()

im.show()

"""

"""

fig, ax = plt.subplots()

plt.plot(x, y, 'ro',markersize=1)
plt.gca().set_aspect('equal')
ani = FuncAnimation(fig,func=linea2,frames=len(lista)-1,
                    interval=10)

ani.save("cosa9.gif", writer=PillowWriter(fps=24))

"""
"""
#animacion de la imagen quitando lineas

im = mpimg.imread("imagen.png") 
draw = ImageDraw.Draw(im) 
figu, ax = plt.subplots()
anim = FuncAnimation(figu,func=linea3,frames=len(lista)-1,
                    interval=10)

im.show()
"""