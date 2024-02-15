import turtle
import random

class spirograph:

    def __init__(self, discRadius, holeRadius, radiusRatio, numberOfPens):

        # self variables
        self.discRadius = discRadius
        self.holeRadius = holeRadius
        self.radiusDrop = discRadius + holeRadius
        self.turtles = []

        #self functions
        rotationPos = self.createInnerCircle()

        #init only variables
        steps = 0
        colours  = ["red","green","blue","orange","purple","pink","yellow"]

        for i in range(numberOfPens):
            colour = random.choice(colours)
            self.turtles.append(self.createDrawer(colour))
        
        while True:
            for i in range(numberOfPens):
                self.turtles[i] = self.drawRotation(i, radiusRatio, rotationPos)
            rotationPos = self.migrateSpirographCentre(1)

            steps += 1
            # stop after 20 full rotations
            if steps >= 5200:
                break


    def createInnerCircle(self):
        # create turtle to track movement around outer circle
        self.discTracker = turtle.Turtle()
        self.discTracker.speed('fast')
        self.discTracker.up()
        self.discTracker.color('red')
        self.discTracker.goto(0, 500-self.discRadius)
        return list(self.discTracker.pos())


    def migrateSpirographCentre(self, arc):
        self.discTracker.circle(-(500-self.discRadius), arc)
        return list(self.discTracker.position())

    def createDrawer(self, colour):
        drawer = turtle.Turtle()
        drawer.color(colour)
        drawer.up()
        drawer.speed('fastest')
        drawer.goto([0, 500-self.radiusDrop])
        drawer.circle(self.holeRadius, random.randrange(360))
        penPos = list(drawer.pos())
        penDiff = [penPos[0], penPos[1] - (500 - self.radiusDrop)]
        return [drawer, penDiff]


    def drawRotation(self, i, arc, rotationPos):
        data = self.turtles[i]
        drawer, penDiff = data[0], data[1]

        rotationPos[1] = rotationPos[1] - self.holeRadius
        updatedPos = [0,0]
        updatedPos[0], updatedPos[1] = rotationPos[0] + penDiff[0], rotationPos[1] + penDiff[1]

        drawer.goto(updatedPos)
        drawer.down()
        drawer.circle(self.holeRadius, arc)
        penPos = list(drawer.pos())
        penDiff[0], penDiff[1] = penPos[0] - rotationPos[0], penPos[1] - rotationPos[1]
        return [drawer, penDiff]