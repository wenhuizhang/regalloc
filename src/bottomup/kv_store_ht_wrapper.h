/************************************************
 *                 Key Value Store
 *
 * Copyright 2018 Wenhui Zhang, Phil Lopreiato,
 *   Neel Shah, Eric Armbrust
 *
 * kv_store_ht_wrapper.h - Declares the functions
 *    for the kv_store_ht_wrapper.c file
*************************************************/

#ifndef kv_store_HT_WRAPPER
#define kv_store_HT_WRAPPER

#include <stdlib.h>
#include <pthread.h>
#include "hashtable.h"
#include "murmurhash.h"


/* Defines for returned status */
#define STORED          0
#define NOT_STORED      1
#define EXISTS          2
#define NOT_FOUND       3

/* Types of hashing algorithms we support */
typedef enum {
       MURMUR
} hash_type;

/* All encompassing datatype for server datastore */
struct kv_store {
        struct ht* hashtable;
        hash_type hash;
        pthread_mutex_t lock;
};

/* Defines for hashtable params */
#define HT_SIZE 10 // number of buckets
#define HT_BUCKET_LENGTH 10 // max entry/bucket (only if rebalancing)
#define HT_FILL_PCT 0.1 // % bucket fill (only if rebalancing)
#define HT_REBAL 0 //disable rebalancing for now

/* Initialize a new key/value datastore */
struct kv_store*
kv_store_init(hash_type hash_algorithm);

/* Function to perform MD5 hash of key */
int
kv_store_murmur_hash(char* key);

/* Function to compare the equality of two entries */
int
kv_store_node_cmp(struct ht_node* node1, struct ht_node* node2);

/**
 * Wrapper function to set a value in the hashtable
 * Preconditions:
 *      - server has been initialized with kv_store_init
 *      - key and value are not NULL
 * Returns either STORED or NOT_STORED (defined above)
 */
int
kv_store_set (struct kv_store* server,
                 char *key,
                 size_t key_length,
                 char *value,
                 size_t value_length);

/**
 * Wrapper function to read a value from the hashtable
 * Returns the data if sucessful, or NULL on error
 * These correspond to the EXISTS and NOT_FOUND codes above
 * Preconditions:
 *      - server is initialized with kv_store_init
 *      - key is not NULL
 */
char*
kv_store_get (struct kv_store* server,
                 char *key,
                 size_t key_length,
                 size_t value_length);

/* Frees all memory associated with the datastore */
void
kv_store_free(struct kv_store* server);

#endif
