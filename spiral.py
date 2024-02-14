import turtle

class spirograph:

    def __init__(self, discRadius, holeRadius):
        self.discRadius = discRadius
        self.holeRadius = holeRadius
        self.radiusDrop = discRadius + holeRadius
        self.posDiff = [0, 0]
        self.createInnerCircle()
        self.createDrawer()
        rotationPos = [0, 500-self.discRadius]
        penPos = [0, 500-self.radiusDrop]
        endPos = [0, 500-self.radiusDrop]

        while True:
            penPos = self.drawRotation(1, rotationPos)
            rotationPos = self.migrateSpirographCentre(1)
            
            if rotationPos == endPos:
                break


    def createInnerCircle(self):
        # create turtle to track movement around outer circle
        self.discTracker = turtle.Turtle()
        self.discTracker.speed('fast')
        self.discTracker.up()
        self.discTracker.color('red')
        self.discTracker.goto(0, 500-self.discRadius)


    def migrateSpirographCentre(self, arc):
        self.discTracker.circle(-(500-self.discRadius), arc)
        return list(self.discTracker.position())

    def createDrawer(self):
        self.drawer = turtle.Turtle()
        self.drawer.up()
        self.drawer.speed('fastest')
    
    def drawRotation(self, arc, rotationPos):
        rotationPos[1] = rotationPos[1] - self.holeRadius
        updatedPos = [0,0]
        updatedPos[0], updatedPos[1] = rotationPos[0] + self.posDiff[0], rotationPos[1] + self.posDiff[1]
        self.drawer.goto(updatedPos)
        self.drawer.down()
        self.drawer.circle(self.holeRadius, arc)
        penPos = list(self.drawer.pos())
        self.posDiff[0], self.posDiff[1] = penPos[0] - rotationPos[0], penPos[1] - rotationPos[1]
        return penPos