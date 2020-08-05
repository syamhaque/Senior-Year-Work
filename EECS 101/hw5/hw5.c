#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define ROWS	480
#define COLS	640
#define PI 3.14159265358979323846

#define sqr(x)	((x)*(x))
#define THETA   360
#define RHO 	1600



void clear( unsigned char image[][COLS] );
void header( int row, int col, unsigned char head[32] );

int main( int argc, char** argv )
{
	int				i,j, sgmmax;
	// localmax: number in the three bucket of voting array corrsponding to three local maxima
	// index[3][2]: used for store rho and theta
	int				dedx, dedy, sgm, localmax[3] = {0, 0, 0}, index[3][2] = { 0, 0, 0, 0, 0, 0 }, ma;
	// voting; voting array
	int				sgm_threshold, hough_threshold, voting[THETA][RHO], voting_max[3];
	FILE*			fp;
	unsigned char	image[ROWS][COLS], simage[ROWS][COLS], sgmimage[ROWS][COLS], bimage[ROWS][COLS], head[32];
	char			filename[50], ifilename[50], ch;
	float           theta, rho;
	
	clear(simage);
	strcpy ( filename, "image.raw");
	memset ( voting, 0, sizeof(int) * 180 * 400 );
	header(ROWS, COLS, head);
	

	/* Read in the image */
	if (!( fp = fopen(filename, "rb" ) ))
	{
		fprintf( stderr, "error: couldn't open %s\n", argv[1]);
		exit(1);
	}

	for ( i = 0 ; i < ROWS ; i++ )
		if (!( COLS == fread( image[i], sizeof(char), COLS, fp ) ))
		{
			fprintf( stderr, "error: couldn't read %s\n", argv[1] );
			exit(1);
		}
	fclose(fp);

    /* Compute SGM */
	for (i = 1; i < ROWS - 1; i++) {
		for (j = 1; j < COLS - 1; j++) {
			dedx = image[i - 1][j + 1] + 2 * image[i][j + 1] + image[i + 1][j + 1] - image[i - 1][j - 1] - 2 * image[i][j - 1] - image[i + 1][j - 1];
			dedy = image[i - 1][j - 1] + 2 * image[i - 1][j] + image[i - 1][j + 1] - image[i + 1][j - 1] - 2 * image[i + 1][j] - image[i + 1][j + 1];
			simage[i][j] = sqrt(sqr(abs(dedx)) + sqr(abs(dedy)));
		}
	}
	sgmmax = 0;
	sgm_threshold = 115;
	for (i = 0; i < ROWS - 1; i++) {
		for (j = 0; j < COLS - 1; j++) {
			sgm = simage[i][j];
			sgmmax = sgm > sgmmax ? sgm : sgmmax;
		}
	}

	// clear(sgmimage);
	for (i = 0; i < ROWS - 1; i++) {
		for (j = 0; j < COLS - 1; j++) {
			sgmimage[i][j] = (int)(simage[i][j] * 255.0) / sgmmax;
		}
	}
	
	/* build up voting array */
	for (theta = 0; theta < THETA; theta+=0.5) {
		for (rho = 0; rho < RHO; rho++) {
			voting[(int)theta][(int)rho] = 0;
		}
	}

	/* Save SGM to an image */
	strcpy(filename, "image");
	if (!(fp = fopen(strcat(filename, "-sgm.ras"), "wb")))
	{
		fprintf(stderr, "error: could not open %s\n", filename);
		exit(1);
	}
	fwrite(head, 4, 8, fp);
	for (i = 0; i < ROWS; i++)
		fwrite(sgmimage[i], sizeof(char), COLS, fp);
	fclose(fp);


	/* Compute the binary image */
	clear(simage);
	for (i = 0; i < ROWS; i++) {
		for (j = 0; j < COLS; j++) {
			if (sgmimage[i][j] > sgm_threshold) {
				simage[i][j] = 255;
			}
			else {
				simage[i][j] = 0;
			}
		}
	}

	/* Save the thresholded SGM to an image */
	strcpy(filename, "image");
	if (!(fp = fopen(strcat(filename, "-binary.ras"), "wb")))
	{
		fprintf(stderr, "error: could not open %s\n", filename);
		exit(1);
	}
	fwrite(head, 4, 8, fp);
	for (i = 0; i < ROWS; i++)
		fwrite(simage[i], sizeof(char), COLS, fp);
	fclose(fp);

	for (i = 0; i < ROWS - 1; i++) {
		for (j = 0; j < COLS - 1; j++) {
			if (simage[i][j] == 255) {
				for (theta = 0; theta < THETA; theta+=0.5) {
					rho = j * cos((theta * (PI / 180))) - i * sin((theta * (PI / 180)));
					voting[(int)theta][(int)rho]++;
				}
			}
		}
	}

	/* Save original voting array to an image */
	strcpy(filename, "image");
	header(THETA, RHO, head);
	if (!(fp = fopen(strcat(filename, "-voting_array.ras"), "wb")))
	{
		fprintf(stderr, "error: could not open %s\n", filename);
		exit(1);
	}
	fwrite(head, 4, 8, fp);

	for (i = 0; i < THETA; i++)
		fwrite(voting[i], sizeof(char), RHO, fp);
	fclose(fp);

	///* Threshold the voting array */

	hough_threshold = 30;
	for(theta = 0; theta < THETA; theta+=0.5){
		for(rho = 0; rho < RHO; rho++){
			if(voting[(int)theta][(int)rho] < hough_threshold){
				voting[(int)theta][(int)rho] = 0;
			}
		}
	}

	///* Write the thresholded voting array to a new image */
	strcpy(filename, "image");
	header(THETA, RHO, head);
	if (!(fp = fopen(strcat(filename, "-voting_array.ras"), "wb")))
	{
		fprintf(stderr, "error: could not open %s\n", filename);
		exit(1);
	}
	fwrite(head, 4, 8, fp);

	for (i = 0; i < THETA; i++)
		fwrite(voting[i], sizeof(char), RHO, fp);
	fclose(fp);

	voting_max[0] = 0;
	voting_max[1] = 0;
	voting_max[2] = 0;

	for (i = 0; i < 200; i++) {
		for (j = 0; j < RHO; j++) {
			if (voting_max[0] < voting[i][j]) {
				voting_max[0] = voting[i][j];
				index[0][0] = i;
				index[0][1] = j;
			}
		}
	}
	for (i = 240; i < 300; i++) {
		for (j = 0; j < RHO; j++) {
			if (voting_max[1] < voting[i][j]) {
				voting_max[1] = voting[i][j];
				index[1][0] = i;
				index[1][1] = j;
			}
		}
	}
	for (i = 300; i < 360; i++) {
		for (j = 0; j < RHO; j++) {
			if (voting_max[2] < voting[i][j]) {
				voting_max[2] = voting[i][j];
				index[2][0] = i;
				index[2][1] = j;
			}
		}
	}
	// int k = 0, s = 0, ii = 0, jj = 0;
	// for (i = 0; i < THETA; i++) {
	// 	for (j = 0; j < RHO; j++) {
	// 		if (voting[i][j] > 0) {
	// 			voting_max[0] = voting[i][j];
	// 			index[0][0] = i;
	// 			index[0][1] = j;
	// 			ii = i; jj = j;
	// 			for(k = i+1; k < i+30; k++){
	// 				for(s = j+1; s < j+30; s++){
	// 					if(voting[k][s] > 0){
	// 						i = k;
	// 						j = s;
	// 					}
	// 					if(voting_max[0] < voting[k][s]){
	// 						voting_max[0] = voting[k][s];
	// 						index[0][0] = k;
	// 						index[0][1] = s;
	// 					}
	// 				}
	// 			}
	// 			for(ii; ii < k; ii++){
	// 				for(jj; jj < s; jj++){
	// 					voting[ii][jj] = 0;
	// 				}
	// 			}
	// 		}
	// 		break;
	// 	}
	// 	break;
	// }

	// for (i = 0; i < THETA; i++) {
	// 	for (j = 0; j < RHO; j++) {
	// 		if (voting[i][j] > 0) {
	// 			voting_max[1] = voting[i][j];
	// 			index[1][0] = i;
	// 			index[1][1] = j;
	// 			ii = i; jj = j;
	// 			for(k = i+1; k < i+30; k++){
	// 				for(s = j+1; s < j+30; s++){
	// 					if(voting[k][s] > 0){
	// 						i = k;
	// 						j = s;
	// 					}
	// 					if(voting_max[1] < voting[k][s]){
	// 						voting_max[1] = voting[k][s];
	// 						index[1][0] = k;
	// 						index[1][1] = s;
	// 					}
	// 				}
	// 			}
	// 			for(ii; ii < k; ii++){
	// 				for(jj; jj < s; jj++){
	// 					voting[ii][jj] = 0;
	// 				}
	// 			}
	// 		}
	// 		break;
	// 	}
	// 	break;
	// }

	// for (i = 0; i < THETA; i++) {
	// 	for (j = 0; j < RHO; j++) {
	// 		if (voting[i][j] > 0) {
	// 			voting_max[2] = voting[i][j];
	// 			index[2][0] = i;
	// 			index[2][1] = j;
	// 			ii = i; jj = j;
	// 			for(k = i+1; k < i+30; k++){
	// 				for(s = j+1; s < j+30; s++){
	// 					if(voting[k][s] > 0){
	// 						i = k;
	// 						j = s;
	// 					}
	// 					if(voting_max[2] < voting[k][s]){
	// 						voting_max[2] = voting[k][s];
	// 						index[2][0] = k;
	// 						index[2][1] = s;
	// 					}
	// 				}
	// 			}
	// 			for(ii; ii < k; ii++){
	// 				for(jj; jj < s; jj++){
	// 					voting[ii][jj] = 0;
	// 				}
	// 			}
	// 		}
	// 		break;
	// 	}
	// 	break;
	// }

	printf("Hough threshold: %d\n", hough_threshold);
	printf("%d %d %d\n%d %d %d\n%d %d %d\n", index[0][0], index[0][1], voting_max[0],
											index[1][0], index[1][1] , voting_max[1],
											index[2][0], index[2][1], voting_max[2]);

	/* Reconstruct an image from the voting array */
	clear(image);
	for (i = 0; i < ROWS - 1; i++) {
		j = (float)i * tan((index[0][0] * (PI / 180))) + index[0][1] / cos((index[0][0] * (PI / 180)));
		if (j < COLS && j >= 0)	image[i][j] = 255;
		j = (float)i * tan((index[1][0] * (PI / 180))) + index[1][1] / cos((index[1][0] * (PI / 180)));
		if (j < COLS && j >= 0)	image[i][j] = 255; 
		j = (float)i * tan((index[2][0] * (PI / 180))) + index[2][1] / cos((index[2][0] * (PI / 180)));
		if (j < COLS && j >= 0)	image[i][j] = 255;
	}


	/* Write the reconstructed figure to an image */
	strcpy(filename, "image");
	header(ROWS, COLS, head);
	if (!(fp = fopen(strcat(filename, "-reconstructed_image.ras"), "wb")))
	{
		fprintf(stderr, "error: could not open %s\n", filename);
		exit(1);
	}
	fwrite(head, 4, 8, fp);
	for (i = 0; i < ROWS; i++)
		fwrite(image[i], sizeof(char), COLS, fp);
	fclose(fp);

	printf("Press any key to exit: ");
	gets(&ch);

	return 0;
}

void clear( unsigned char image[][COLS] )
{
	int	i,j;
	for ( i = 0 ; i < ROWS ; i++ )
		for ( j = 0 ; j < COLS ; j++ ) image[i][j] = 0;
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

