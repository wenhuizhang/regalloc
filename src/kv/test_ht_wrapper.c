/* File to test hashtable wrapper */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kv_store_ht_wrapper.h"
#include "hashtable.h"

int
main(){
        struct kv_store* server;
        char* data;
        int result;

        printf("Testing hashtable wrapper\n");
        printf("Allocating server memory...");
        server = kv_store_init(MURMUR);
        assert(server);
        printf("OK\n");

        printf("Testing getting a nonexistent value...");
        data = kv_store_get(server, "foobar", 0, 0);
        assert(data == NULL);
        printf("OK\n");

        printf("Testing inserting a value...");
        result = kv_store_set(server, "foobar", 0, "meow", 0);
        assert(result == STORED);
        printf("OK\n");

        printf("Testing getting a value...");
        data = kv_store_get(server, "foobar", 0, 0);
        assert(strcmp(data, "meow") == 0);
        printf("OK\n");

        printf("All tests passed\n");
}
