'''
Non-dominated set by gift-wrapping
'''

from matplotlib import pyplot as plt
import numpy as np 

# Defines the diemsnion of the window
MIN_WIDTH = 0
MAX_WIDTH = 100
MIN_HEIGHT = 0
MAX_HEIGHT = 100


def cleardata():
    global fig, gw
    cid = fig.canvas.mpl_connect('button_press_event', onmouseclick)
    ax.cla()
    gw.points = []
    gw.stack = []
    ax.set_xlim([MIN_WIDTH, MAX_WIDTH])
    ax.set_ylim([MIN_HEIGHT, MAX_HEIGHT])
    plt.show()
        
def onmouseclick(event):
    '''Event handler for inputting the points and storing it into the global list "points" '''
    global gw
    ix, iy = event.xdata, event.ydata
    if ix and iy:
        gw.points.append((ix, iy))
        ax.plot(ix, iy, marker='o', color='black')
        plt.show()

def onkeypress(event):
    global ax, gw
    
    if event.key == ' ':
        '''Carry out the gift-wrapping stop point collection from mouse if exists '''
        gw.giftwrap(True)
    elif event.key == 'c':
        '''Clear the plot '''
        cleardata()

class Gwnondominate():
    def __init__(self):
        self.points = [] # List to store the raw points
        self.stack = [] # The stack which store the non-dominated points
        
    def readpoints(self, option, filename=None):
        global ax
        
        if option == "mouse":
            cid = fig.canvas.mpl_connect('button_press_event', onmouseclick)
        elif option == "file":
            with open(filename, 'r') as f:
                for line in f:
                    processedline = line.strip('\n\r')
                    splitted = processedline.split(',')
                    x = float(splitted[0])
                    y = float(splitted[1])
                    self.points.append((x, y))
                    ax.plot(x, y, marker='o', color='black')
            plt.show()
        elif option == "random":
            minx = int(input("Enter in the min x coordinate: "))
            maxx = int(input("Enter in the max x coordinate: "))
            miny = int(input("Enter in the min y coordinate: "))
            maxy = int(input("Enter in the max y coordinate: "))
            numpoints = int(input("Enter in the number of points to generate: "))
            
            x = np.random.randint(minx, maxx, numpoints)
            y = np.random.randint(miny, maxy, numpoints)
            self.points = [coordinate for coordinate in zip(x, y)]
            ax.scatter(x, y, marker='o', color='black')
            plt.show()
    
    def findextremepoint(self):
        '''Returns the right-most and highest Y-coordinate point'''
        rightmost = self.points[0]
        for point in self.points:
            if point[0] > rightmost[0]:
                rightmost = point
            elif point[0] == rightmost[0] and point[1] > rightmost[1]:
                rightmost = point
        
        return rightmost
        
    def giftwrap(self, trace=False):
        '''Computes a list of points which are the non-dominated set found by "gift-wrapping" and is store into stack'''
        global ax
        
        points = self.points 
        stack = self.stack
        rightmost = self.findextremepoint()
        leftover = len(points) - 1
        ax.plot(rightmost[0], rightmost[1], color='b', marker='o')
        plt.show()
        
        # Add and remove the rightmost to the stack and from the point
        stack.append(rightmost)
        points.remove(rightmost)
        
        while len(points) > 0:
            currentmax = points[0]
            lastpoint = stack[-1]
            pointI = 0
            while pointI < len(points):
                point = points[pointI]
                if trace:
                    ax.plot([lastpoint[0], point[0]], [lastpoint[1], point[1]])
                    plt.show()
                    plt.waitforbuttonpress()
                if point[1] < lastpoint[1]:
                    points.remove(point)
                    if trace:
                        ax.lines.pop()
                        plt.show()
                    continue
                if currentmax[0] < point[0]:
                    currentmax = point 
                elif currentmax[0] == point[0] and currentmax[1] < point[1]:
                    currentmax = point
                if trace:
                    ax.lines.pop()
                    plt.show()
                pointI += 1
            if currentmax[0] < stack[-1][0] and currentmax[1] > stack[-1][1]:
                stack.append(currentmax)
                points.remove(currentmax)
                ax.plot(currentmax[0], currentmax[1], color='b', marker='o')
            else:
                if currentmax in points:
                    points.remove(currentmax)


if __name__ == "__main__":
    
    # Main plot for plotting the convex hull
    fig, ax = plt.subplots(1,1)
    
    gw = Gwnondominate()

    fig.canvas.mpl_connect('key_press_event', onkeypress)
    
    # print(refinepoints(), "is the refined points")

    ax.set_xlim([MIN_WIDTH, MAX_WIDTH])
    ax.set_ylim([MIN_HEIGHT, MAX_HEIGHT])
    
    print("1. 'mouse': mouse in points")
    print("2. 'file': file inputs")
    print("3. 'random': randomly generate points")
    userchoice = input("Select which option you want to input the points: ")
    if userchoice == "mouse":
        gw.readpoints("mouse")
    elif userchoice == "file":
        filename = input("Input in the file name: ")
        gw.readpoints("file", filename)
    elif userchoice == "random":
        gw.readpoints("random")
        
    plt.show()
