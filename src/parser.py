#/bin/python
# as it is within a bisic block, suppose there is no more than 
# 15 instructions in one BB, thus max v is less than 15*3 = 45
# thus for rewriting def, we could start from  50 for safe


import re
import sys
import numpy as np

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
    for items in keys_deleted:
        register_map[items] = K-1

print register_map


in_reg = list(set(uniques) - set(keys_deleted))


with open('pass3.txt', 'w') as f:
    for pre_load in in_reg:
        new_chars = 'r'+ str(register_map[pre_load])
        f.write("load %s\t" % new_chars)
        f.write("%s\n" % pre_load)
    for item in global_file:
        if(item[2] not in in_reg):
            new_chars = 'r'+ str(register_map[item[2]])
            f.write("load %s\t" % new_chars)
            f.write("%s\n" % item[2])
            in_reg.append(item[2])
        if(item[3] not in in_reg):
            new_chars = 'r'+ str(register_map[item[3]])
            f.write("load %s\t" % new_chars)
            f.write("%s\n" % item[3])
            in_reg.append(item[3])
        f.write("%s\t" % item[0])
        new_chars = 'r'+ str(register_map[item[1]])
        f.write("%s\t" % new_chars)
        new_chars = 'r'+ str(register_map[item[2]])
        f.write("%s\t" % new_chars)
        new_chars = 'r'+ str(register_map[item[3]])
        f.write("%s\t" % new_chars)
        f.write("\n")
        in_reg.append(item[1])
        if(item[1] in keys_deleted):
            new_chars = 'r'+ str(register_map[item[1]])
            f.write("store %s\t" % new_chars)
            f.write("%s\n" % item[1])
            in_reg.remove(item[1])
        if(item[2] in keys_deleted):
            new_chars = 'r'+ str(register_map[item[2]])
            f.write("store %s\t" % new_chars)
            f.write("%s\n" % item[2])
            in_reg.remove(item[2])
        if(item[3] in keys_deleted):
            new_chars = 'r'+ str(register_map[item[3]])
            f.write("store %s\t" % new_chars)
            f.write("%s\n" % item[3])
            in_reg.remove(item[3])















