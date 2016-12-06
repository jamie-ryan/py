# draw a fractal tree using PIL, code adopted from:
# http://www.math.union.edu/research/fractaltrees/
# Python Image Library (PIL) free from:
# http://www.pythonware.com/products/pil/index.htm
# tested with Python24 and PIL115    vegaseat   25jun2006
#import os
import math
# needs Python Image Library (PIL)
import Image, ImageDraw
def fractal_tree(iter, origin, t, r, theta, dtheta):
    """
    returns a list of line begin/end

     when iter == 0
    origin:   x,y coordinates of the start of this branch
    t:        current trunk length
    r:        factor to contract the trunk each iteration
    theta:    starting orientation
    dtheta:   angle of the branch
    """
    if iter == 0:
        return []
    x0, y0 = origin
    x, y = x0 + t * math.cos(theta), y0 + t * math.sin(theta)
    lines = [((x0,y0), (x,y))]
    # recursive calls
    lines.extend(fractal_tree(iter-1, (x,y), t * r, r, theta + dtheta, dtheta))
    lines.extend(fractal_tree(iter-1, (x,y), t * r, r, theta - dtheta, dtheta))
    return lines
def draw_lines(lines, width=320, height=250):
    """draw and return the fractal tree image"""
    # create empty white image to draw on
    image1 = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image1)

#    brown = (102, 51, 0)
#    green = (0, 153, 0)

    min_branch_length = abs(lines[8][0][0] - lines[8][1][0])
    for line in lines:
        dx = abs(line[0][0] - line[1][0])
        dy = abs(line[0][1] - line[1][1])
        dz = math.sqrt((dx**2)+(dy**2))
        if dz > min_branch_length:
        #brown
            col = (102, 51, 0)
        else:
        #green
            col = (0, 153, 0)
        draw.line(line, col)
    return image1
# test the functions ...
if __name__ == '__main__':
    # angle to radian factor
    ang2rad = math.pi/180.0

    # experiment with number of iterations (try 4 to 16) ###iteration 8 is start of leaves..color green?
    iter = 18
    niter = 18
    # experiment with trunk length (try 100)
    t = 150
    # experiment with factor to contract the trunk each iteration (try 0.65)
    r = 0.75
    # starting orientation (initial 90 deg)
    thetadegrees = 90.0
    theta = thetadegrees * ang2rad
    # experiment with angle of the branch (try 60 deg)
    dthetadegrees = 60.0
    dtheta = dthetadegrees * ang2rad
    # center of top
    #origin = (200, 0)
    # center of bottom
    origin = (500, 0)

    lines = fractal_tree(iter, origin, t, r, theta, dtheta)

    # change width and height as needed ...
    width = 1000
    height = 1000
    # use PIL's show, internally saves a temporary bitmap file, then calls the default viewer
    # (the problem: these bitmap files are large and accumulate in one of the temp directories)
    #imgage1.show()

    # or ...
    # save as .png .jpg .gif or .bmp file
    # (the .png format gives the smallest file size)
    image1 = draw_lines(lines, width, height)
    iterst = str(iter)
    tst = str(t)
    rst = str(r)
    thetast = str(thetadegrees)
    dthetast = str(dthetadegrees)

    filename = "fractal-tree-iter-"+iterst+"-t-"+tst+"-r-"+rst+"-theta-"+thetast+"-dtheta-"+dthetast+".jpg"
    image1.save(filename)
    image1.show()
    # ... and view the saved file, works with Windows only
    # behaves like double-clicking on the saved file
    #os.startfile(filename)
    
    
    #"""
    # another way to activate the default viewer associated with the image
    # might work on more platforms
    #import webbrowser
    #webbrowser.open(filename)
    #"""


