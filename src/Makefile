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
	python ./parser.py
	./regalloc -o 1 -f pass2.txt -k 9
	./regalloc -o 2 -f pass2.txt -k 9

.PHONY: clean

clean:
	rm -f ./*.o regalloc main

