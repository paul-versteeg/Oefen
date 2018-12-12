from PIL import Image
from PIL import ImageDraw
from datetime import *
import colorsys

dimensions=(800,800)
scale=1.0/(dimensions[0]/3)
center=(2.2,1.5) # Dit verschuift het plaatje naar links recht onder en boven. Met 2,2 en 1,5 lijkt hij in het midden te staan
iterate_max=100  # Aantal loops in fractal berekening. 101 is max
colors_max=100  # Hoe groter aantal kleuren hoe meer diepte in plaatje

img=Image.new("RGB",dimensions)
d=ImageDraw.Draw(img)

# De Mandelbrot fractal berekening
palette=[0]*colors_max
for i in range(colors_max):
    f=1-abs((float(i)/colors_max-1)**15)
    r,g,b=colorsys.hsv_to_rgb(.66+f/3,1-f/2,f)
    palette[i]=(int(r*255),int(g*255),int(b*255))

def iterate_mandelbrot(c,z=0):
    for n in range(iterate_max+1):
        z=z*z+c
        if abs(z)>2:
            return n
    return None

for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        c=complex(x*scale-center[0],y*scale-center[1])
        n=iterate_mandelbrot(c)
        if n is None:
            v=1
        else:
            v=n/100.0
            d.point((x,y),fill=palette[int(v*(colors_max-1))])
del d

#het plaatje opslaan met de tijd in de file naam
vandaag=datetime.today()
FileNaam='Resultaat-'

for attr in \
    ['minute','second','microsecond']:
    FileNaam=FileNaam+str(getattr(vandaag,attr))
FileNaam=FileNaam+".png"
img.save(FileNaam)