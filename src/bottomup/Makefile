#/************************************************
#*                    Key Value Store
#* Copyright 2018  Wenhui Zhang, Phil, Neel Shah,
#*    Eric Armbrust, Chenghu He, 
#*    Wei Zhang, Pradeep Kumar
#*
#* This program is licensed under the MIT license.
#*
#* Makefile - Compiles the hashtable wrapper
#*************************************************/

#Use the gcc compiler
CC = gcc
CFLAGS = -pthread -std=c99 -pedantic -Wall
LDFLAGS =
DEPS = hashtable.c linkedlist.c kv_store_ht_wrapper.c murmurhash.c
TEST = test_bottomup.c
OBJS = kv_store
TEST_BIN = test

#Ensure compiling is done with all necessary dependencies
%.o: %.c $(DEPS)
	$(CC) $(CFLAGS) -c -o $@ $<


all: $(OBJS) $(TEST_BIN)

kv_store:
	$(CC) $(CFLAGS) -c $(DEPS)

test:
	$(CC) $(CFLAGS)  -o $(TEST_BIN) $(DEPS) $(TEST) 

.PHONY: make clean && make all 
clean:
	rm -f *.a *.o $(OBJS) *.gch $(TEST_BIN)

