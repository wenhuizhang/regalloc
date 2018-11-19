#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


int 
topdown(char *file, int regnum){
    printf ("This is naive topdown register allocation for:\n");
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
