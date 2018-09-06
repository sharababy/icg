// gcc -o line line.c -L/System/Library/Frameworks -framework GLUT -framework OpenGL

#include <GLUT/glut.h>
#include <stdio.h>

int x1, y1, x2, y2;


void myDisplay() {
	//draw_line(x1, x2, y1, y2);
	glFlush();
}

int main(int argc, char **argv) {

	printf( "Enter (x1, y1, x2, y2)\n");
	scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

	// glutInit(&argc, argv);
	// glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
	// glutInitWindowSize(500, 500);
	// glutInitWindowPosition(0, 0);
	// glutCreateWindow("Bresenham's Line Drawing");
	// myInit();
	// glutDisplayFunc(myDisplay);
	// glutMainLoop();

	return 0;
}