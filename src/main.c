/*  Register Allocation 
 *  Toplevel Interface
 *  Author : Wenhui
 */


#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include "topdown.c"
#include "bottomup.c"

void 
usage(void)
{
  printf ("Usage: regalloc -o [1,2] -f filename.txt -k [0-9]*\n");
  printf (" Please choose from the following options for o:\n");
  printf ("     1. top down register allocation\n");
  printf ("     2. bottowm up register allocation\n");
  printf (" Please use -f filename.txt to specify instruction sequences\n");
  printf (" Please use integer to specify your register number K");
  printf ("\n\n");
}



int
main (int argc, char **argv)
{
  int tflag = 0;
  int bflag = 0;
  char *fvalue = NULL;
  int regnum = 0;
  int c;
  int result;

 
  //usage();

  while ((c = getopt (argc, argv, "o:f:k:")) != -1)
    switch (c)
      {
      case 'o':
        {
            if((!strncmp(optarg, "1", 1)) & (!strncmp(optarg, "2", 1))){
                usage();
            }   
            if(!strncmp(optarg,"1", 1))
                tflag = 1;
            if(!strncmp(optarg, "2", 1))
                bflag = 1;
            break;
        }
      case 'f':
        fvalue = optarg;
        break;
      case 'k':
        regnum = atoi(optarg);
        if(regnum < 3){
            printf("Register number size should be >= 3\n");
            return 0;
        }
        break;
      default:
        usage();
        break;
      }

  printf ("tflag = %d, bflag = %d, fvalue = %s, register number = %d\n", tflag, bflag, fvalue, regnum);



  if(tflag == 1)
    result = topdown(fvalue, regnum);
  if(bflag == 1)
    result = bottomup(fvalue, regnum);

  return 0;
}
