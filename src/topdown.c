#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


int 
topdown(char *file, char *k_file){
    printf ("This is topdown register allocation with graph coloring:\n");
    
    FILE* fp;
    char buffer[255];
    fp = fopen(file, "r");

    printf("rewritted functions\n");
    while(fgets(buffer, 255, (FILE*) fp)){
        printf("%s\n", buffer);
    }

    fclose(fp);
    
    fp = fopen("alloc_var.txt", "r");

    printf("allocated registers\n");
    while(fgets(buffer, 255, (FILE*) fp)){
        printf("%s\n", buffer);
    }

    fclose(fp);
    
    return 0;
};
