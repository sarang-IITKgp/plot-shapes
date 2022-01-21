import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#import shapes.conic_sections as conic
import plotshapes as sh





mpl.rc('axes',labelsize=24)
mpl.rc('font',size=24)




print('This is the test directory')

#C1 = sh.conic_sections.circle(3,(5,-2.5))
C1 = sh.conic_sections.circle(1,(-2,3))

E1 = sh.conic_sections.ellipse((0.25,1),(5,0))
#E1.rotate(-70)
E2 = sh.conic_sections.ellipse((3,1),(-5,-5))

R1 = sh.quadrilateral.rectangle((4,0.5),(0,3))


#R1.rotate_about_center(135)




print('Circumference = %1.2f ; Area = %1.2f' %(C1.perimeter, C1.area))


fig1 = plt.figure('Test-shapes-pkg')
ax1_f1 = fig1.add_subplot(111)
#ax1_f1.plot(C1.x,C1.y,linewidth=2)
#ax1_f1.plot(E1.x,E1.y,linewidth=2)
#ax1_f1.plot(E2.x,E2.y,linewidth=2)
#ax1_f1.plot(R1.x,R1.y,linewidth=2)
#ax1_f1.plot(R2.x,R2.y,linewidth=2)
N = 8
for count in range(N):
	R1.plot(ax1_f1,text_tag = str(count*360/N))
	R1.rotate_about_center(360/N)
	E1.plot(ax1_f1,text_tag = str(count*360/N))
	E1.rotate_about_center(360/N)
	
C2 = sh.conic_sections.circle()
C2.plot(ax1_f1)

ax1_f1.axis('equal')
#ax1_f1.legend()

ax1_f1.grid(1)
ax1_f1.set_xlim([-10,10])
ax1_f1.set_ylim([-10,10])




plt.show()
