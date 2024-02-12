    # Introduction

    A spirograph is a mathematical method of drawing geometric patterns. A large, hollow circle houses a smaller cirle, allowing it to rotate as it travels the inside edge of the circumference. A pen or other marker is placed at a point inside the smaller circle to draw as it rotates. This produces the geometric pattern we all love.  

    # Scope

    I want to use the Turtle and Math libraries to create a programe which will replicate a spirograph. The target outcomes are:
     - save the output as an image file
     - take arguments for inner and outer radius
     - take argument for where the marker shoul be along inner radius
     - colour argument 

    ## nice to have
     - ability to specify other inner shapes

# Maths theory

In effect this project is calculating continuous relationships between the lengths of arcs, the angle of travel and radius lengths. 

Four circles need to be considered for the case of a circle in circle spirograph. 

1. The outer circle containing the graph.  
2. The inner circle, spinning to create the pattern we see.  
3. The circle which the centre point of the inner circle makes as it travels around the outer circle. 
4. Point k (pen) rotating around the center of the inner circle with it's shorter radius.  

The inner circle spins around the outer circle, and the arc length that has been in contact on the inner and outer is equal. (Imagine converting the circumferneces into flat lines, one rotation = the length of this line)  

The arc length here is equal, but the angle of rotation will be different. e.g. if the outer circle is 8πcm and the inner is 4πcm, then the angle travelled by a full roation of the inner circle (2π) will be a half cirlce on the outer circle (π)

So, if we define one arbritary circumfrance unit, we can can calculate the angle of movement along the outer circle, and the new position of the inner circle's centre point can be found from that. (imagine a pizza slice shape, the crust is the outer circle and the centre point of the inner circle has moved from one slice edge to the other ((not the same movement as the length of crust)))

IF we consier this movement in infentisimaly small steps, we can say that the inner circle rotates aroun its centre point, for the same arc length as our original step. BUT, with a new angle. The rotation of this circle is relative to it's centre point, which we can upate in small steps to create an appearance of a smooth line. 

The same proccess of thought can be use to etermine the movement of point k (spirograph pen) along it's rotation.