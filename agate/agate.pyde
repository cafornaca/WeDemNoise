def setup():
    size(500, 500)
    xoff = 0.0
    background(204)
    for i in range(1000):
        xoff = xoff + .01
    n = noise(xoff) * width
    line(n, 0, n, height)

noiseScale = 0.02
myScale = 5
i = 0

def makeAgate(movement):
    if movement == True:
        global i
        i = i+.01
    for x in range(0, width, myScale):
        if movement == True:
            noiseVal = noise(x+i)
        else:             
            noiseVal = noise(x)
        fill(noiseVal * 255)
        noStroke()
        ellipse(height/2 , width/2, height-x, width-x)
            

def draw():
    background(0)
    makeAgate(False)
    
