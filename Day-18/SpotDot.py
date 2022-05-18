import colorgram as c

colors_full = []
colors = c.extract("./hello.png", 10)
for i in range(0, 10):
    color = colors[i]
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    my_tuple = (r, g, b)
    colors_full.append(my_tuple)

print(colors_full)
