import turtleWindow as tw
import outerCricle as oc
import spiral as sp

def main():
    drawingDisc = getSpiralRadius()
    spiralRadius = getSpirographHole(drawingDisc)

    screen = tw.Window()
    base = oc.outerCircle()
    spiralGraph = sp.spirograph(drawingDisc, spiralRadius)
    spiralGraph.main()


def getSpiralRadius():
    print("What size do you want the spiral to be?")
    try:
        radius = float(input("Please specify a number 0-500. "))
    except ValueError:
        print("Please choose a number between 0 and 500. ")
        getSpiralRadius()
    if radius > 500 or radius < 0:
        print("Please choose a number between 0 and 500. ")
        getSpiralRadius()
    return radius

def getSpirographHole(radius):
    choice = input("Please choose a length to draw from: \
        A) The full radius. \
        B) Three quarters of the radius. \
        C) Half the radius. \
        D) One quarter of the radius. \ ")

    match choice:
        case 'A':
            return radius
        case 'B':
            return radius * 0.75
        case 'C':
            return radius * 0.5
        case 'D':
            return radius * 0.25
        case other:
            print("Please choose a valid option. ")
            getSpirographHole()

if __name__ == "__main__":
    main()