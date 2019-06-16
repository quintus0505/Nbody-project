# -----------------------------------------------------------------------
# universe.py
# -----------------------------------------------------------------------

import sys
import mujoco_py   #现在看来用不上
import stdarray
import stddraw
from body import Body
from instream import InStream
from vector import Vector
from tensorboardX import SummaryWriter
import numpy as np
import math


# -----------------------------------------------------------------------
writer = SummaryWriter()
class Universe:

    # Construct a new Universe object by reading a description
    # from the file whose name is filename.

    def __init__(self, filename):
        instream = InStream(filename)
        n = instream.readInt()
        radius = instream.readFloat()
        stddraw.setXscale(-radius, +radius)
        stddraw.setYscale(-radius, +radius)
        self._bodies = stdarray.create1D(n)
        for i in range(n):
            rx = instream.readFloat()
            ry = instream.readFloat()
            vx = instream.readFloat()
            vy = instream.readFloat()
            mass = instream.readFloat()
            r = Vector([rx, ry])
            v = Vector([vx, vy])
            self._bodies[i] = Body(r, v, mass)

    # Simulate the passing of dt seconds in self.

    def increaseTime(self, dt, epoch):

        # Initialize the forces to zero.
        n = len(self._bodies)
        f = stdarray.create1D(n, Vector([0, 0]))

        # Compute the forces.

        for i in range(n):
            for j in range(n):
                if i != j:
                    bodyi = self._bodies[i]
                    bodyj = self._bodies[j]

                    f[i] = f[i] + bodyi.forceFrom(bodyj,epoch,i,j)



        # Move the bodies.
        for i in range(n):
            self._bodies[i].move(f[i], dt,epoch,i)

            # Draw self to standard draw.

    def draw(self):
        for body in self._bodies:
            body.draw()


# -----------------------------------------------------------------------

# Accept a string filename and a float dt as command-line arguments.
# Simulate the motion in the universe defined by the contents of
# the file with the given filename, increasing time at the rate
# specified by dt.

def main():

    filename ="/home/quintus0505/programming/Nbody/3body.txt" #sys.argv[1]
    #fp=open(filename,"r")
    dt = 10000 #float(sys.argv[2])
    universe = Universe(filename)
    #while True:
    for epoch in range(15000):
        universe.increaseTime(dt, epoch)

        stddraw.clear()
        universe.draw()
        stddraw.show(10)
    #fp.close

if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------

# python universe.py 2bodyTiny.txt 20000

# python universe.py 2body.txt 20000

# python universe.py 3body.txt 20000

# python universe.py 4body.txt 20000
