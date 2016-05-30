import math, colorsys
# needs Python Image Library (PIL)
import Image, ImageDraw

# angle to radian factor
ang2rad = math.pi/180.0

# experiment with number of iterations (try 4 to 16) ###iteration 8 is start of leaves..color green?
iter = 18
# experiment with trunk length (try 100)
t = 120
# experiment with factor to contract the trunk each iteration (try 0.65)
r = 0.65
# starting orientation (initial 90 deg)
theta = 90.0 * ang2rad
# experiment with angle of the branch (try 60 deg)
dtheta = 10.0 * ang2rad
# center of top
#origin = (200, 0)
# center of bottom
origin = (200, 0)

width = 400
height = 600

#(r, g, b) = colorsys.hsv_to_rgb(float(height * 0.9) / iter, 1.0, 1.0)
#R, G, B = int(255 * r), int(255 * g), int(255 * b)

lines = fractal_tree(iter, origin, t, r, theta, dtheta)

image1 = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image1)
















lines = fractal_tree(iter, origin, t, r, theta, dtheta)

# change width and height as needed ...
width = 400
height = 600
image1 = draw_lines(lines, width, height)
