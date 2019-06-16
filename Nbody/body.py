#-----------------------------------------------------------------------
# body.py
#-----------------------------------------------------------------------

import stddraw
from tensorboardX import SummaryWriter
import numpy as np
import math

writer = SummaryWriter()
class Body:

    # Construct a new Body object whose position is specified by
    # Vector object r, whose velocity is specified by Vector object
    # v, and whose mass is specified by float mass.

    def __init__(self, r, v, mass):
        self._r = r        # Position
        self._v = v        # Velocity
        self._mass = mass  # Mass

    # Move self by applying the force specified by Vector object
    # f for the number of seconds specified by float dt.

    def move(self, f, dt,epoch,i):
        a = f.scale(1 / self._mass)

        self._v = self._v + (a.scale(dt))
        self._r = self._r + self._v.scale(dt)
        print(self._v)
        total1=0
        total2 = 0
        total0 = 0
        total3=0
        tv1 = 0
        tv2 = 0
        tv0 = 0
        tv3=0
        if i == 1:
            for vs in self._v:
                total1 = total1+vs*vs

            tv1 = math.sqrt(total1)

        if i == 2:
            for vs in self._v:
                total2 = total2 + vs * vs

            tv2 = math.sqrt(total2)
        if i == 0:
            for vs in self._v:
                total0 = total0 + vs * vs

            tv0 = math.sqrt(total0)

        if i == 3:
            for vs in self._v:
                total3 = total3 + vs * vs

            tv3 = math.sqrt(total3)


        writer.add_scalars('scalar/test', {'body2': tv1, 'body3': tv2, 'body1': tv0,'body4': tv3}, epoch)
        print(epoch)



    # Return the force between Body objects self and other.

    def forceFrom(self, other, epoch,i,j):
        G = 6.67e-11
        delta = other._r - self._r
        dist = abs(delta)
        magnitude = (G * self._mass * other._mass) / (dist * dist)


        return delta.direction().scale(magnitude)

    # Draw self to standard draw.

    def draw(self):
        stddraw.setPenRadius(0.0125)
        stddraw.point(self._r[0], self._r[1])


