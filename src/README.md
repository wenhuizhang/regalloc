# Register Allocation

Please put instructions in ***filename.txt***

Please put your K register number in ***K.txt***


Then perform:

```
Wenhuis-MacBook-Pro:src wenhuizhang$ make clean 
rm -f  alloc_var.txt pass* ./*.o regalloc main
Wenhuis-MacBook-Pro:src wenhuizhang$ python parser.py 
Wenhuis-MacBook-Pro:src wenhuizhang$ make
gcc -c -o main.o main.c -I./
gcc -o regalloc main.o -I./
Wenhuis-MacBook-Pro:src wenhuizhang$ ./regalloc 
This is topdown register allocation with graph coloring:
rewritted functions
load r0		v2

Op	r2	r0	r0

store r2	v1

load r2		v1

load r0		v4

Op	r1	r2	r0

store r1	v3

load r2		v5

Op	r3	r2	r2

store r3	v1

load r2		v6

load r1		v3

Op	r4	r2	r1

store r4	v7

load r3		v1

Op	r1	r3	r3

store r1	v1

Op	r1	r2	r0

store r1	v4

allocated registers
allocated:['v1', 'v2', 'v1', 'v1', 'v4', 'v3', 'v4', 'v5', 'v6', 'v7']

spilled:[]

This is bottomup register allocation for:
load r0		v2 

Op	r4	r0	r0

store r4	v1

load r1		v1 

load r2		v4 

Op	r4	r1	r2

store r4	v3

store r1	v1

store r2	v4

load r3		v5 

Op	r4	r3	r3

store r4	v1

store r3	v5

load r1		v6 

load r2		v3 

Op	r4	r1	r2

store r4	v7

store r1	v6

store r2	v3

load r3		v1 

Op	r4	r4	r4

store r4	v1

load r1		v6 

load r2		v4 

Op	r4	r1	r4

store r4	v4

store r1	v6


```
