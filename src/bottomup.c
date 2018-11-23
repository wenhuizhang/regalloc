/*bottom up:
 * Focus on replacement rather than allocation
 * Keep values “used soon” in registers
 * Only parts of a live range may be assigned to a physical register
 *
 * algorithm:
 * Start with empty register set
 * Load on demand
 * When no register is available, free one
 */


#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


int 
bottomup(char *file, int regnum){
    printf ("This is bottomup register allocation for:\n");
    printf ("fvalue = %s, register number = %d\n", file, regnum);
    
    FILE* fp;
    char buffer[255];
    fp = fopen(file, "r");

    while(fgets(buffer, 255, (FILE*) fp)){
        printf("%s\n", buffer);
    }

    fclose(fp);
    return 1;
};
