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
  printf ("Usage: regalloc -o [1,2] -f filename.txt -k K.txt\n");
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
  char *fvalue = "filename.txt";
  char *pvalue = "K.txt";
  int regnum = 0;
  int c;
  int result;

 

  //usage();
  printf ("Usage: regalloc -o [1,2] -f filename.txt -k K.txt\n");

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
        pvalue = optarg;
        break;
      default:
        usage();
        break;
      }

  printf ("tflag = %d, bflag = %d, fvalue = %s, reg_num_file= %s\n", tflag, bflag, fvalue, pvalue);


  result = topdown("pass3.txt", "K.txt");
  result = bottomup(fvalue, pvalue);

  return 0;
}
