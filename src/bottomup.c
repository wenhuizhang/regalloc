#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


int 
bottomup(char *file, int regnum){
    printf ("This is bottomup register allocation for:\n");
    printf ("fvalue = %s, register number = %d\n", file, regnum);
    return 1;
};
