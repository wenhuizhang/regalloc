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




int
main (int argc, char **argv)
{
  int result;


  result = topdown("pass3.txt", "K.txt");
  result = bottomup("pass5.txt", "K.txt");

  return 0;
}
