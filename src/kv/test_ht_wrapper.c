/* File to test hashtable wrapper */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kv_store_ht_wrapper.h"
#include "linkedlist.h"
#include "hashtable.h"




int
main(void){
    struct kv_store* v2r;
    char* var_elm;
    char* var_elm_spill;
    int result;
    char* reg_name_tmp; // register name as value
    int K = 2; // we have 10 virtual registers in total
    struct ll *unused_reg; // linked list for storing unused register
    struct ll *unmap_var; // linked list for storing unmapped var
    struct ll *map_var; // linked list for storing unmapped var
    struct ll_node *node;
    struct ll_node *node_spill;
    struct ll_node *node_reg;
    struct ll_node *reg_name_node; //spill and append back to unused reg
    int i = 0;
    int j = 0; // every 3 lines, print out current v2r translation with instructions


    printf("Init Queue for unmapped value ...\n");
    FILE* fp;
    char buffer[8*1000];
    fp = fopen("../pass2.txt", "r");
    unmap_var = ll_init();
    int nr_line = 0;
    while(fgets(buffer + nr_line * 8, 255, (FILE*) fp)){
        //printf("%s\n", buffer);
        node = ll_create_node(buffer + nr_line * 8);
        ll_append(unmap_var, node);
        // ll_print_node(unmap_var);
        nr_line++;
    }



    printf("Init reg Queue to Size of K = %d ...\n", K);
    char reg_name_buffer[8*1000];
    unused_reg = ll_init();
    map_var = ll_init();
    int nr_reg = 0;
    for(i = 1; i <= K; i++){
        memset(reg_name_buffer + nr_reg * 8, 0, 8);
        sprintf(reg_name_buffer + nr_reg * 8, "r%d", i);
        node = ll_create_node(reg_name_buffer + nr_reg * 8);
        ll_append(unused_reg, node);
        nr_reg++;
    }
    //printf("init registers....:\n");
    //ll_print_node(unused_reg);

    printf("Init KV Store ...\n");
    v2r = kv_store_init(MURMUR);

//
// for (all varaible elements in the list), each new_element is a v%d, var_elm

    int len = ll_get_size(unmap_var);
    //printf("len=%d\n", len);

    for(i = 0; i < len; i++){
      //printf("i=%d, j=%d\n", i, j);
      if((j+2)%3 == 0){
        printf("After %d th Instruction, Allocated Vars: \n", (j+2)/3);
        ll_print_node(map_var);
        printf("\n");
      }
      //printf("unmap_var=%p\n", unmap_var);
      //printf("unmap_var size=%p\n", ll_get_size(unmap_var));

      if (ll_get_size(unmap_var) > 1) {
          node = ll_first(unmap_var);
      } else {
          node = ll_first_peek(unmap_var);
          unmap_var->size--;
      }
      //printf("node=%p\n", node);
      var_elm = node->data;
      //printf("var_elm = %s\n", var_elm);
      reg_name_tmp = kv_store_get(v2r, var_elm , 0, 0);
      //printf("reg name tmp 1 = %s\n", reg_name_tmp);
      if(reg_name_tmp == NULL) {
        //printf("unused_reg size=%p\n", ll_get_size(unused_reg));

        if(ll_get_size(unused_reg) == 0 ) {
          //spill one register from key value store
          // printf("map_var size=%p\n", ll_get_size(map_var));
          node_spill = ll_first(map_var);


          var_elm_spill = node_spill->data;
          printf("spilling %s\n", var_elm_spill);
          reg_name_tmp = kv_store_get(v2r, var_elm_spill , 0, 0);
          result = kv_store_set(v2r, var_elm_spill , 0, NULL, 0); //delete it from KV
          reg_name_node = ll_create_node(reg_name_tmp);
          ll_append(unused_reg, reg_name_node);
        }

        if (ll_get_size(unused_reg) > 1)  {
            node_reg = ll_first(unused_reg);
        } else {
            node_reg = ll_first_peek(unused_reg);
            unused_reg->size--;
        }
        reg_name_tmp = node_reg->data;
        result = kv_store_set(v2r, var_elm , 0, reg_name_tmp, 0);
        ll_append(map_var, node);
        //printf("reg name tmp 2 = %s\n", reg_name_tmp);
      }
    j = j + 1;
  }
  fclose(fp);
}
