#/bin/python
# as it is within a bisic block, suppose there is no more than 
# 15 instructions in one BB, thus max v is less than 15*3 = 45
# thus for rewriting def, we could start from  50 for safe


import re
import sys
import numpy as np
import os
import string
import fileinput

text_file = open ( 'filename.txt' , 'r')
lines = text_file.read().split('\n')
print len(lines)


# Creates a list containing len(lines) -1  lists, each of 4 items, all set to 0
w, h = 4, (len(lines) -1);
global_file = [[0 for x in range(w)] for y in range(h)] 


for i in range(len(lines) -1):
    chars = re.split(', | ',lines[i])
    global_file[i] = chars




print global_file

with open('pass0.txt', 'w') as f:
    for item in global_file:
        for chars in item:
            f.write("%s\t" % chars)
        f.write("\n")

used_set = set()

for i in range(len(lines) -1):
    temp = global_file[i][1] 
    # rename chars[1] in each line
    # then rewrite all Insts afterwards for new naming
    #num = re.split('v', global_file[i][1])
    num = global_file[i][1]

    used_set.add(global_file[i][2])
    used_set.add(global_file[i][3])
    while(num in used_set):
        num = re.split('v', num)
        num = int(num[1]) + 50
        num = 'v' + str(num)
    used_set.add(num)

    global_file[i][1] = num
    for j in range((i+1), (len(lines) -1)):
        if temp ==  global_file[j][1]:
            if temp == global_file[j][2]:
                global_file[j][2] = global_file[i][1]
            if temp == global_file[j][3]:
                global_file[j][3] = global_file[i][1]
            break;
        else:
            #replace chars_res[2] and [3] if match temp
            if temp == global_file[j][2]:
                global_file[j][2] = global_file[i][1]
            if temp == global_file[j][3]:
                global_file[j][3] = global_file[i][1]
    #print "for each change"
    #print global_file
print global_file


with open('pass1.txt', 'w') as f:
    for item in global_file:
        for chars in item:
            f.write("%s\t" % chars)
        f.write("\n")


with open('pass2.txt', 'w') as f:
    for item in global_file:
        f.write("%s\n" % item[2])
        f.write("%s\n" % item[3])
        f.write("%s\n" % item[1])


uniques = np.unique(global_file)
uniques = np.delete(uniques, 0, 0)
print uniques

live_dict = {}
# for each unique var find its occurence line
for uniq in uniques:
    live_range = []
    for i in range(len(global_file)):
        if ((uniq == global_file[i][1]) or (uniq == global_file[i][2]) or (uniq == global_file[i][3])):
            live_range.append(i) 
    start = min(live_range)
    end = max(live_range)
    live_range = range(start+1, end+2)
    live_dict[uniq] = live_range
print live_dict


def intersection(lst1, lst2):
    # Use of hybrid method
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3

graph = {}


for i in range(len(uniques)):
    graph[uniques[i]] = []
    for j in range(len(uniques)):
        if(i == j):
            continue
        inter = intersection(live_dict[uniques[i]], live_dict[uniques[j]])
        print uniques[i], uniques[j], inter
        if(len(inter) != 0):
            graph[uniques[i]].append(uniques[j])
print graph

def color_nodes(graph, K):
  # Order nodes in descending degree
  nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]), reverse=True)
  color_map = {}

  for node in nodes:
    available_colors = [True] * K
    for neighbor in graph[node]:
      if neighbor in color_map:
        color = color_map[neighbor]
        available_colors[color] = False
    for color, available in enumerate(available_colors):
      if available:
        color_map[node] = color
        break
  return color_map

K_file = open ( 'K.txt' , 'r')
K = int(K_file.read().split('\n')[0])

if(K <= 3):
    print "K is too small"
    sys.exit("K should be larger than 3!")
print K


def min_k(graph, uniques):
    i = 0
    while(len(color_nodes(graph, i)) != len(uniques)):
        i = i + 1
    return i

# print min_k(graph, uniques) 

#spill vars to mem
def degree_graph(graph, deg_num):
    keys_deleted = []
    for i in range(deg_num):
        key_to_delete = max(graph, key=lambda k: len(graph[k]))
        del graph[key_to_delete]
        keys_deleted.append(key_to_delete) 
    return graph, keys_deleted 


register_map = {}

if ( K>= min_k(graph, uniques) ):
    register_map = color_nodes(graph, K)
else:
    new_graph, keys_deleted  = degree_graph(graph, min_k(graph, uniques)-K+2)
    print keys_deleted # these ones alternatively use the Kth register for load and store
    # print new_graph
    register_map = color_nodes(new_graph, K-2)
    #for items in keys_deleted:
    #    register_map[items] = K-1

print "allocated map:", register_map

def p1mapp0():
    p1mp0 = {}
    pass0_file= open ("pass0.txt" , 'r')
    lines = pass0_file.read().split('\n')
    w, h = 4, (len(lines) -1)
    pass0 = [[0 for x in range(w)] for y in range(h)] 
    for i in range(len(lines) -1):
        chars = re.split('\t',lines[i])
        for j in range(len(chars)-1):
            pass0[i][j] = chars[j]
    pass1_file= open ("pass1.txt" , 'r')
    lines = pass1_file.read().split('\n')
    w, h = 4, (len(lines) -1)
    pass1 = [[0 for x in range(w)] for y in range(h)] 
    for i in range(len(lines) -1):
        chars = re.split('\t',lines[i])
        for j in range(len(chars)-1):
            pass1[i][j] = chars[j]
    for i in range(len(pass1)):
        for j in range(len(pass1[0])):
            if(pass1[i][j] not in p1mp0):
                p1mp0[pass1[i][j]] = pass0[i][j]
    return p1mp0

p1mp0 = p1mapp0()

in_reg = list(set(uniques) - set(keys_deleted))

with open('alloc_var.txt', 'w') as f:
    f.write("allocated:%s\n" % in_reg)
    f.write("spilled:%s\n" % keys_deleted)


print uniques
print "allocated:",in_reg
print "spill:", keys_deleted


loaded = []
spill_res_flag = 0
with open('pass3.txt', 'w') as f:
    for chars in global_file:
        if((chars[2] in register_map) and (chars[2] not in loaded)):
            f.write("load %s\t\t" % ('r'+str(register_map[chars[2]])))
            f.write("%s\n" % chars[2])
            loaded.append(chars[2])
        if((chars[2] not in register_map) and (chars[2] not in loaded)):
            f.write("load %s\t\t" % ('r'+str(K-1)))
            f.write("%s\n" % chars[2])
            loaded.append(chars[2])
        if((chars[3] in register_map) and (chars[3] not in loaded)):
            f.write("load %s\t\t" % ('r'+str(register_map[chars[3]])))
            f.write("%s\n" % chars[3])
            loaded.append(chars[3])
        if((chars[3] not in register_map) and (chars[3] not in loaded)):
            f.write("load %s\t\t" % ('r'+str(K-2)))
            f.write("%s\n" % chars[3])
            loaded.append(chars[3])
        f.write("%s\t" % chars[0])
        if(chars[1] in register_map):
            new_char = 'r'+ str(register_map[chars[1]])
        else:
            spill_res_flag = 1
            new_char = 'r'+str(K-1)
        f.write("%s\t" % new_char)
        if(chars[2] in register_map):
            new_char = 'r'+ str(register_map[chars[2]])
        else:
            new_char = 'r'+str(K-1)
        f.write("%s\t" % new_char)
        if(chars[3] in register_map):
            new_char = 'r'+ str(register_map[chars[3]])
        else:
            new_char = 'r'+str(K-2)
        f.write("%s\n" % new_char)
        #if(spill_res_flag == 1):
        if(chars[1] not in register_map):
            f.write("store %s\t" % ('r'+str(K-1)))
            f.write("%s\n" % chars[1])
        else:
            f.write("store %s\t" % ('r'+str(register_map[chars[1]])))
            f.write("%s\n" % chars[1])
        spill_res_flag = 0
        



print p1mp0


for key, value in p1mp0.iteritems():
    s = open("pass3.txt").read()
    s = s.replace(key, value)
    f = open("pass3.txt", 'w')
    f.write(s)
    f.close()



for key, value in p1mp0.iteritems():
    s = open("alloc_var.txt").read()
    s = s.replace(key, value)
    f = open("alloc_var.txt", 'w')
    f.write(s)
    f.close()














