#/bin/python
# as it is within a bisic block, suppose there is no more than 
# 15 instructions in one BB, thus max v is less than 15*3 = 45
# thus for rewriting def, we could start from  50 for safe


import re


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
