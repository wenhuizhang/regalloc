CC=gcc
IDIR=./
CFLAGS=-I$(IDIR)
DEPS = main.c topdown.c bottomup.c
OBJ = main.o  

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

regalloc: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

test:
	echo "test: regalloc -o 1 -f filename.txt -k 9"
	./regalloc -o 1 -f filename.txt -k 9
	echo "test: regalloc -o 2 -f filename.txt -k 9"
	./regalloc -o 2 -f filename.txt -k 9

.PHONY: clean

clean:
	rm -f ./*.o regalloc main

