def main():
    return 0;

def create_map_find_path(file_name):



    return 0;



def find_path(starting_pos, dest_pos):
    total = 0
    global weight
    global i_s
    global j_s
    global n
    print(i_s,j_s)
    for x in range(n):
        for y in range(n):
            total += int(Map[x][y][0])
    if total != 64:
        try:
            if weight_map[i_s - 1][j_s][0] != -1 and (i_s - 1) >= 0 and (i_s - 1) <= n -1 and weight_map[i_s-1][j_s][0] > weight:
                #after weight map 
                weightadder()
                i_s -= 1;
                for row in weight_map:
                    print(*row, sep="")
                for row in Map:
                    print(*row, sep="")

                find_path((i_s,j_s), dest_pos)
            else:
                raise IndexError
        except IndexError:
            #move right
            try:
                if weight_map[i_s][j_s + 1][0] != -1 and (j_s + 1) <= n - 1 and (j_s + 1) >= 0 and weight_map[i_s][j_s + 1][0] > weight + 1:
                    weightadder()
                    j_s += 1;
                    for row in weight_map:
                        print(*row, sep="")
                    for row in Map:
                        print(*row, sep="")

                    find_path((i_s, j_s), dest_pos)
                else:
                    raise IndexError
               #move down
            except IndexError:
                try:
                    if weight_map[i_s + 1][j_s][0] != -1 and (i_s  + 1) <= n - 1 and (i_s + 1) >= 0 and weight_map[i_s + 1][j_s][0] > weight + 1:
                        weightadder()
                        i_s += 1
                        for row in weight_map:
                            print(*row, sep="")
                        for row in Map:
                            print(*row, sep="")
                        find_path((i_s, j_s), dest_pos)
                    else:
                        raise IndexError
                except IndexError:
                    try:
                        if weight_map[i_s][j_s - 1][0] != -1 and (j_s - 1) >= 0 and (j_s - 1) <= n -1 and weight_map[i_s][j_s - 1][0] > weight + 1:
                            weightadder()
                            j_s -= 1
                            for row in weight_map:
                                print(*row, sep="")
                            for row in Map:
                                print(*row, sep="")

                            find_path((i_s, j_s), dest_pos)
                        else:
                            raise IndexError
                    except IndexError:
                        try:
                                for row in weight_map:
                                    print(*row, sep="")
                                for row in Map:
                                    print(*row, sep="")
                                Map[i_s][j_s][0] = 1
                                find_path(scan(),dest_pos)
                        finally:
                            pass

    return 0;

def weightadder():
    global weight
    global i_s
    global j_s
    weight += 1
    #upwards
    if (i_s - 1) >= 0:
        if weight_map[i_s - 1][j_s][0] > weight + 1:
            weight_map[i_s - 1][j_s][0] = weight
        elif weight_map[i_s - 1][j_s][0] < weight + 1:
            pass
        else:
            weight_map[i_s - 1][j_s][0] = weight

    #left
    if (j_s - 1) >= 0:
        if weight_map[i_s][j_s - 1][0] > weight +1:
            weight_map[i_s][j_s -1][0] = weight
        elif weight_map[i_s][j_s -1][0] < weight +1:
            pass
        else:
            weight_map[i_s][j_s - 1][0] = weight

    #rigth
    if (j_s + 1) <= (n-1):
        if weight_map[i_s][j_s + 1][0] > weight +1:
            weight_map[i_s][j_s + 1][0] = weight
        elif weight_map[i_s][j_s + 1][0] < weight + 1:
            pass
        else:
            weight_map[i_s][j_s + 1][0] = weight

    #down
    if (i_s + 1) <= (n -1):
        if weight_map[i_s + 1][j_s][0] > weight + 1:
            weight_map[i_s + 1][j_s][0] = weight
        elif weight_map[i_s + 1][j_s][0] < weight + 1:
            pass
        else:
            weight_map[i_s + 1][j_s][0] = weight

    Map[i_s][j_s][0] = 1

    return 0;
def scan():
    global i_s
    global j_s
    global dest_pos
    global weight
    global Map
    global map_h
    global Map_def
    Map_def = [[ [] for i in range(n)] for j in range(n)]
    for j in range(n):
        for k in range(n):
            Map_def[j][k].append(int(map_h[j][0][k]))
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if Map[i][j][0] == 0 and weight_map[i][j][0] !=(n*n+1) and weight_map[i][j] != 65:
                print(i,j)
                i_s = i
                j_s = j
                weight = weight_map[i][j][0]
                print(weight)
                print(Map)
                return (i,j)




def print_path(path):
    return 0;


def less_bloated_split(my_string, my_delimiter):
    #initializing empty list and empty string to add char to
    new_list, list_entry = [], str("");

    #for each char not equal to delimiter and ',', added to empty string until loop iterates through it
    for char in range(len(my_string)):
        if (my_string[char] == my_delimiter or my_string[char] == "\n"):
            new_list.append(list_entry)
            list_entry = str("");
        else:
            list_entry += str(my_string[char]);

    return new_list;

#organize into functions later

#file_name = input('What file do you want to parse?: ')
try:
    with open("sample.txt") as my_file:
        map_text = my_file.readlines()
except:
    print('File not found.')
    exit()

weight_map, map_h, temp, map_info= [], [], [], [];

for line in range(len(map_text)):
    temp = less_bloated_split(map_text[line]," ");
    map_info.append(temp);
print(map_info)
n = int(map_info[0][0])
Map = [[ [] for i in range(n)] for j in range(n)]
Map_def = [[ [] for i in range(n)] for j in range(n)]
weight_map = [[ [] for i in range(n)] for j in range(n)]
for x in range(n):
    map_h.append(map_info[3+x])
for j in range(n):
    for k in range(n):
        Map[j][k].append(int(map_h[j][0][k]))
for j in range(n):
    for k in range(n):
        Map_def[j][k].append(int(map_h[j][0][k]))
print(Map_def)
for i in range(n):
    for j in range(n):
        if Map[i][j][0] != 1:
            weight_map[i][j].append(n*n+1);
        elif Map[i][j][0] == 1:
            weight_map[i][j].append(-1)
for row in Map:
    print(*row, sep="")
pointer_map = [[ "" for i in range(n)] for j in range(n)]
start_dest  = [map_info[1],map_info[2]]
dest_pos    = tuple(start_dest[1])
start_pos   = tuple(start_dest[0])
weight = 0;
print(start_pos)
i_s = int(start_pos[0]);
j_s = int(start_pos[1]);
weight_map[i_s][j_s][0] = 0
for row in weight_map:
    print(*row, sep="")

total = int(0)
find_path(start_pos,dest_pos)
for row in weight_map:
    print(*row, sep="")
for row in Map:
    print(*row, sep="")
