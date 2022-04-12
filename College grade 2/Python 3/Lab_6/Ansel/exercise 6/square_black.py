import Image
black_color = "#000000"
white_color = "#FFFFFF"
width, height = 344, 473
image = Image.Image(width, height, "square_black.img")
for x in range(width):
    for y in range(height):
        if (x%86 < 43 and y%86<43) or (x%86 > 43 and y%86>43):
            image[x, y] = black_color
        elif (x%86 < 43 and y%86>43) or (x%86 > 43 and y%86<43) :
            image[x, y] = white_color
image.save()
image.export("square_black.xpm")
