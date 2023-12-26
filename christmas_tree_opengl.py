import sys
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

a = 0.1
b = 0.5
turns = 40
points_per_turn = 1000
angle = 0.0
rotation_speed = 1.0  

def draw_spiral():
    z = 3
    glPointSize(4.0)
    glColor3f(0.0, 0.5, 0.1)
    glBegin(GL_POINTS)
    
    for i in range(int(turns * points_per_turn)):
        t = i / points_per_turn
        x = a * t * math.cos(t)
        y = a * t * math.sin(t)
        glVertex3f(x, y, z)
        z -= 0.000175
    glEnd()

    points = list(range(4000,15000,1400))
    points += list(range(15000,25000,800))
    points += list(range(25000,int(turns * points_per_turn),400))
    
    for i in points:
        t = i / points_per_turn
        x = a * t * math.cos(t)
        y = a * t * math.sin(t)
        
        glColor3f(0.8, 0.0, 0.0)
        glPushMatrix()
        glTranslatef(x, y, 3 - (i * 0.000175))
        glutSolidSphere(0.2, 10, 10)  
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()    
    
    glColor3f(1.0, 0.85, 0.2)  
    glPushMatrix()
    glTranslatef(0, 0, 3)
    glutSolidSphere(0.2, 10, 10)
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()
        
    points = list(range(2600,14600,700))
    points += list(range(14600,24800,400))
    points += list(range(24800,int(turns * points_per_turn),200))

    N = 3
    idx = [random.randint(0,N-1) for k in range(int(turns * points_per_turn))]

    for i in range(len(points)):
        t = points[i] / points_per_turn
        x = a * t * math.cos(t)
        y = a * t * math.sin(t)        
        z = 3 - (points[i]  * 0.000175)

        if(idx[i] == 0):
            glPointSize(2.0)
            glBegin(GL_POINTS)
            glVertex3f(x, y, z-0.1)
            glEnd()

        if(idx[i] == 1):
            glPointSize(3.0)
            glBegin(GL_POINTS)
            glVertex3f(x, y, z-0.2)
            glEnd()

        if(idx[i] == 2):
            glPointSize(4.0)
            glBegin(GL_POINTS)
            glVertex3f(x, y, z-0.3)
            glEnd()

        idx[i] = (idx[i] + 1) % N
  
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(10, 10, 4, 0, 0, 0, 0, 0, 1)
    glRotatef(angle,0.0,0.0,1.0)
    draw_spiral()
    glutSwapBuffers()    

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def update(frame):
    global angle
    angle += rotation_speed
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Christmas tree")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(16, update, 0)  
    glutMainLoop()

if __name__ == "__main__":
    main()
    
    


