import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import shapes.conic_sections as conic
import shapes as sh



mpl.rc('axes',labelsize=24)
mpl.rc('font',size=24)




print('This is the test directory')

#C1 = sh.conic_sections.circle(3,(5,-2.5))
C1 = conic.circle(3,(5,-2.5))

E1 = sh.conic_sections.ellipse((1,2),(5,5))
E2 = conic.ellipse((2,1),(-5,-5))

print('Circumference = %1.2f ; Area = %1.2f' %(C1.perimeter, C1.area))


fig1 = plt.figure('Test-shapes-pkg')
ax1_f1 = fig1.add_subplot(111)
ax1_f1.plot(C1.x,C1.y,linewidth=2)
ax1_f1.plot(E1.x,E1.y,linewidth=2)
ax1_f1.plot(E2.x,E2.y,linewidth=2)


ax1_f1.grid(1)
ax1_f1.set_xlim([-10,10])
ax1_f1.set_ylim([-10,10])

plt.show()
