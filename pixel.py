from PIL import Image
img = Image.open("joconde_1024.png")

import time

img.show()
img.size

def echange2pix(image, ij0, ij1):
    couleurs0 = image.getpixel(ij0)
    couleurs1 = image.getpixel(ij1)
    image.putpixel(ij0, couleurs1)
    image.putpixel(ij1, couleurs0)

def tourne4pix(image, ij0, ij1, ij2, ij3):
    echange2pix(image, ij0, ij1)
    echange2pix(image, ij1, ij2)
    echange2pix(image, ij2, ij3)

def tourne(image):
    assert(image.size[0] == image.size[1])
    n = image.size[0]
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            ri = (n - 1) - i
            rj = (n - 1) - j
            tourne4pix(image, (i, j), (rj, i), (ri, rj), (j, ri))

temps_origine = time.time()
tourne(img)
print(time.time() - temps_origine)
img.show()


