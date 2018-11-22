/* File to test hashtable wrapper */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kv_store_ht_wrapper.h"
#include "linkedlist.h"
#include "hashtable.h"

int items[K], front = -1, rear = -1;


// queue for register tank
void enqueue(int value){
    if(rear == SIZE-1)
        printf("\nqueue is Full!!");
    else {
        if(front == -1)
            front = 0;
        rear++;
        items[rear] = value;
        printf("\nInserted -> %d", value);
    }
}

int dequeue(){
    int temp;
    if(front == -1)
        printf("\nqueue is Empty!!");
    else{
        temp = front;
        printf("\nDeleted : %d", items[temp]);
        front++;
        if(front > rear)
            front = rear = -1;
    }
    return items[temp];
}


int
main(void){
        struct kv_store* server;
        char* data;
        int result;
        char reg_name[12]; // register name as value
        int temp_reg;
        int K = 10; // we have 10 virtual registers in total
        //struct ll *list; // linked list for storing unused register

        printf("Init Queue to size of K ...");
        for(int i = 0; i <= K; i++){
          enqueue(i);
        }



        printf("Init KV Store ...");
        server = kv_store_init(MURMUR);
        assert(server);
        printf("OK\n");

//
// for (all elements in the list), each new_element is a v%d, val_elm

        for(all elements in the list){
          data = kv_store_get(server, val_elm , 0, 0);
          if(data == NULL){
            int temp_reg = dequeue();
            if( temp_reg == 0 ) { // not enough registers, pick one spill, delete one from kv, enqueue it, then dequeue

            }
            sprintf(reg_name, "reg_%d", temp_reg);
            result = kv_store_set(server, val_elm , 0, reg_name, 0);
          }else{
            continue;
          }
        }

}
