import Image
back_color = "#B22222"
pot_color = "#DCDCDC"
width, height = 688, 946
image = Image.Image(width, height, "dot.img")
for x in range(width):
    for y in range(height):
        if ((x+21)%43==0 or (x+21)%43==1) and ((y+21)%43==0 or (y+21)%43==1):
            image[x, y] = pot_color
        else :
            image[x, y] = back_color
image.save()
image.export("dot.xpm")
