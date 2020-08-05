#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define ROWS 480
#define COLS 640

void header( int row, int col, unsigned char head[32] );
void clear(unsigned char image[ROWS][COLS]);
int main( int argc, char **argv )
{
	int		i, j, k;
	double Vx, Vy, Vz, Sx, Sy, Sz, Hx, Hy, Hz, Nx, Ny, Nz;
	double Ll, Ls, L;
	double x, y, p, q, r, a, m, alpha;
	unsigned char	image[ROWS][COLS], head[32];
	FILE		*fp;
	char filename[9][50];

	header(ROWS, COLS, head);

	strcpy(filename[0], "image_a");
	strcpy(filename[1], "image_b");
	strcpy(filename[2], "image_c");
	strcpy(filename[3], "image_d");
	strcpy(filename[4], "image_e");
	strcpy(filename[5], "image_f");
	strcpy(filename[6], "image_g");
	strcpy(filename[7], "image_h");
	strcpy(filename[8], "image_i");

	// if ( argc != 2 )
	// {
	//   fprintf( stderr, "usage: %s output-file\n", argv[0] );
	//   exit( 1 );
	// }
	
	Vx = 0;	Vy = 0;	Vz = 1;
	for(k = 0; k < 9; k++){
		if(k == 0){
			//Image 1
			Sx = 0;	Sy = 0;	Sz = 1;
			r = 50;
			a = 0.5;
			m = 1;
		}
		if(k == 1){
			//Image 2
			Sx = 1/sqrt(3);	Sy = 1/sqrt(3);	Sz = 1/sqrt(3);
			r = 50;
			a = 0.5;
			m = 1;
		}
		if(k == 2){
			//Image 3
			Sx = 1;	Sy = 0;	Sz = 0;
			r = 50;
			a = 0.5;
			m = 1;
		}
		if(k == 3){
			//Image 4
			Sx = 0;	Sy = 0;	Sz = 1;
			r = 10;
			a = 0.5;
			m = 1;
		}
		if(k == 4){
			//Image 5
			Sx = 0;	Sy = 0;	Sz = 1;
			r = 100;
			a = 0.5;
			m = 1;
		}
		if(k == 5){
			//Image 6
			Sx = 0;	Sy = 0;	Sz = 1;
			r = 50;
			a = 0.1;
			m = 1;
		}
		if(k == 6){
			//Image 7
			Sx = 0;	Sy = 0;	Sz = 1;
			r = 50;
			a = 1;
			m = 1;
		}
		if(k == 7){
			//Image 8
			Sx = 0;	Sy = 0;	Sz = 1;
			r = 50;
			a = 0.5;
			m = 0.1;
		}
		if(k == 8){
			//Image 9
			Sx = 0;	Sy = 0;	Sz = 1;
			r = 50;
			a = 0.5;
			m = 10000;
		}

		Hx = (Vx+Sx)/sqrt(pow((Vx+Sx),2) + pow((Vy+Sy),2) + pow((Vz+Sz),2));
		Hy = (Vy+Sy)/sqrt(pow((Vx+Sx),2) + pow((Vy+Sy),2) + pow((Vz+Sz),2));
		Hz = (Vz+Sz)/sqrt(pow((Vx+Sx),2) + pow((Vy+Sy),2) + pow((Vz+Sz),2));

		for(i = 0; i < ROWS; i++){
			for(j = 0; j < COLS; j++){
				x = j - ROWS/2;
				y = COLS/2 - i;

				p = (-x) / sqrt(pow(r,2) - (pow(x,2)+pow(y,2)));
				q = (-y) / sqrt(pow(r,2) - (pow(x,2)+pow(y,2)));

				Nx = (-p) / sqrt(pow(p,2) + pow(q,2) + 1);
				Ny = (-q) / sqrt(pow(p,2) + pow(q,2) + 1);
				Nz = 1 / sqrt(pow(p,2) + pow(q,2) + 1);
				// Nx = -(-i/sqrt(pow(r,2)-(pow(i-ROWS/2,2)+pow(j-COLS/2,2)))) / sqrt((pow(i-ROWS/2,2)/(pow(r,2)-(pow(i-ROWS/2,2)+pow(j-COLS/2,2)))) + (pow(j-COLS/2,2)/(pow(r,2)-(pow(i-ROWS/2,2)+pow(j-COLS/2,2)))) + 1);
				// Ny = -(-j/sqrt(pow(r,2)-(pow(i-ROWS/2,2)+pow(j-COLS/2,2)))) / sqrt((pow(i-ROWS/2,2)/(pow(r,2)-(pow(i-ROWS/2,2)+pow(j-COLS/2,2)))) + (pow(j-COLS/2,2)/(pow(r,2)-(pow(i-ROWS/2,2)+pow(j-COLS/2,2)))) + 1);
				// Nz = 1 / sqrt((pow(i-ROWS/2,2)/(pow(r,2)-(pow(i-ROWS/2,2)+pow(j-COLS/2,2)))) + (pow(j-COLS/2,2)/(pow(r,2)-(pow(i-ROWS/2,2)+pow(j-COLS/2,2)))) + 1);
				Ll = Sx*Nx + Sy*Ny + Sz*Nz;
				if(Ll < 0)	continue;
				alpha = acos(Hx*Nx + Hy*Ny + Hz*Nz);
				Ls = exp(-pow((alpha/m),2));
				L = a*Ll + (1-a)*Ls;
				image[i][j] = (int)(L*255);
			}
		}

		if (!(fp = fopen(strcat(filename[k], ".ras"), "wb")))
		{
			fprintf(stderr, "error: could not open %s\n", filename[k]);
			exit(1);
		}
		fwrite(head, 4, 8, fp);
		for (i = 0; i < ROWS; i++)
			fwrite(image[i], sizeof(char), COLS, fp);
		fclose(fp);
		clear(image);
	}

	return 0;
}
void clear(unsigned char image[ROWS][COLS])
{
	int	i, j;
	for (i = 0; i < ROWS; i++)
		for (j = 0; j < COLS; j++) image[i][j] = 0;
}
void header( int row, int col, unsigned char head[32] )
{
	int *p = (int *)head;
	char *ch;
	int num = row * col;

	/* Choose little-endian or big-endian header depending on the machine. Don't modify this */
	/* Little-endian for PC */
	
	*p = 0x956aa659;
	*(p + 3) = 0x08000000;
	*(p + 5) = 0x01000000;
	*(p + 6) = 0x0;
	*(p + 7) = 0xf8000000;

	ch = (char*)&col;
	head[7] = *ch;
	ch ++; 
	head[6] = *ch;
	ch ++;
	head[5] = *ch;
	ch ++;
	head[4] = *ch;

	ch = (char*)&row;
	head[11] = *ch;
	ch ++; 
	head[10] = *ch;
	ch ++;
	head[9] = *ch;
	ch ++;
	head[8] = *ch;
	
	ch = (char*)&num;
	head[19] = *ch;
	ch ++; 
	head[18] = *ch;
	ch ++;
	head[17] = *ch;
	ch ++;
	head[16] = *ch;
	

	/* Big-endian for unix */
	/*
	*p = 0x59a66a95;
	*(p + 1) = col;
	*(p + 2) = row;
	*(p + 3) = 0x8;
	*(p + 4) = num;
	*(p + 5) = 0x1;
	*(p + 6) = 0x0;
	*(p + 7) = 0xf8;
*/
}