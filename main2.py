import structs
def main():
    maze_map(create_map_info())
    print(StartEnd.starting_pos(), StartEnd.dest_pos())
    NodeHead = structs.CurrentPosition(StartEnd.start_i,StartEnd.start_j,1)

    find_path(NodeHead)
    f_weight_check(NodeHead)
    f_weight_check(NodeHead)
    visual_map()

def find_path(NodeHead):
    completed = True
    for x in range(n):
        for y in range(n):
            if DataMap[x][y].weight == n*n + 1:
                completed = False
    if completed == True:
        return 0;
    while completed == False:
        #try moving up
        if valid_direction(NodeHead,"up") == True:
            add_node_weight(NodeHead)
            NodeHead.i -= 1
            visual_map()
            find_path(NodeHead)

        #try moving right
        elif valid_direction(NodeHead,"right") == True:
            add_node_weight(NodeHead)
            NodeHead.j += 1
            print("right")
            visual_map()
            find_path(NodeHead)

        #try moving down
        elif valid_direction(NodeHead,"down") == True:
            add_node_weight(NodeHead)
            NodeHead.i += 1
            visual_map()
            find_path(NodeHead)

        #try moving left
        elif valid_direction(NodeHead,"left") == True:
            add_node_weight(NodeHead)
            NodeHead.j -= 1
            visual_map()
            find_path(NodeHead)
        else:
            DataMap[NodeHead.i][NodeHead.j].beenTo = 1
            visual_map()
            if backtrack(NodeHead) == 0:
                return
            else:
                find_path(NodeHead)
def add_node_weight(NodeHead):
    NodeHead.weight = DataMap[NodeHead.i][NodeHead.j].weight
    #add weight to up
    if (NodeHead.i - 1) >= 0:
        if DataMap[NodeHead.i -1][NodeHead.j].weight < NodeHead.weight + 1:
            pass
        else:
            DataMap[NodeHead.i - 1][NodeHead.j].weight = NodeHead.weight + 1
            DataMap[NodeHead.i - 1][NodeHead.j].i = NodeHead.i
            DataMap[NodeHead.i - 1][NodeHead.j].j = NodeHead.j

    #add weght to rigth
    if (NodeHead.j + 1) <= (n - 1):
        if DataMap[NodeHead.i][NodeHead.j + 1].weight < NodeHead.weight + 1:
            pass
        else:
            DataMap[NodeHead.i][NodeHead.j + 1].weight = NodeHead.weight + 1
            DataMap[NodeHead.i][NodeHead.j + 1].i = NodeHead.i
            DataMap[NodeHead.i][NodeHead.j + 1].j = NodeHead.j

    #add weight to down
    if (NodeHead.i + 1) <= (n - 1):
        if DataMap[NodeHead.i + 1][NodeHead.j].weight < NodeHead.weight + 1:
            pass
        else:
            DataMap[NodeHead.i + 1][NodeHead.j].weight = NodeHead.weight +1
            DataMap[NodeHead.i + 1][NodeHead.j].i = NodeHead.i
            DataMap[NodeHead.i + 1][NodeHead.j].j = NodeHead.j


    #add weight left and create pointer coord to NodeHead
    if (NodeHead.j - 1) >= 0:
        if DataMap[NodeHead.i][NodeHead.j - 1].weight < NodeHead.weight + 1:
            pass
        else:
            DataMap[NodeHead.i][NodeHead.j - 1].weight = NodeHead.weight + 1
            DataMap[NodeHead.i][NodeHead.j - 1].i = NodeHead.i
            DataMap[NodeHead.i][NodeHead.j - 1].j = NodeHead.j


    #mark that present node has been explored
    DataMap[NodeHead.i][NodeHead.j].beenTo = 1
def print_path():
    print(path)

def valid_direction(NodeHead, direction):
    if direction == "up":
        if (NodeHead.i - 1) >= 0:
            if DataMap[NodeHead.i - 1][NodeHead.j].weight != -1 and DataMap[NodeHead.i -1][NodeHead.j].beenTo == 0:
                return True;
            else:
                return False;
        else:
            return False;

    elif direction == "right":
        if (NodeHead.j + 1) <= (n - 1):
            if DataMap[NodeHead.i][NodeHead.j + 1].weight != -1 and DataMap[NodeHead.i][NodeHead.j + 1].beenTo == 0:
                return True;
            else:
                return False;
        else:
            return False;
    elif direction == "down":
        if (NodeHead.i + 1) <= (n -1):
            if DataMap[NodeHead.i + 1][NodeHead.j].weight != -1 and DataMap[NodeHead.i + 1][NodeHead.j].beenTo == 0:
                return True;
            else:
                return False;
        else:
            return False;
    elif direction == "left":
        if (NodeHead.j - 1) >= 0:
            if DataMap[NodeHead.i][NodeHead.j - 1].weight != -1 and DataMap[NodeHead.i][NodeHead.j - 1].beenTo == 0:
                return True;
            else:
                return False;
        else:
            return False;

def backtrack(NodeHead):
    #start from bottom right of map and check for any valid new start positions 
    for x in range(n-1,-1,-1):
        for y in range(n-1,-1,-1):
            if DataMap[x][y].beenTo == 0 and DataMap[x][y].weight != (n*n + 1):
                NodeHead.i = x
                NodeHead.j = y
                NodeHead.weight = DataMap[x][y].weight
                return NodeHead;
    return 0;

def create_map_info():
    try:
        with open("sample5.txt") as my_file:
            raw_text = my_file.readlines()
    except:
        print('File not found.')
        exit()
    map_info, holder = [], []
    for line in range(len(raw_text)):
        holder = structs.less_bloated_split(raw_text[line]," ")
        map_info.append(holder)
    return map_info


def refresh_nodes():
    for x in range(n):
        for y in range(n):
            if maze_map[x][y] == "1":
                DataMap[x][y].beenTo = 1
            else:
                DataMap[x][y].beenTo = 0
def weight_check(NodeHead):
    #check if weight above is lower
    if (NodeHead.i - 1) >= 0:
        if DataMap[NodeHead.i - 1][NodeHead.j].weight + 1 < DataMap[NodeHead.i][NodeHead.j].weight and DataMap[NodeHead.i - 1][NodeHead.j].weight != -1:
            if DataMap[NodeHead.i][NodeHead.j].weight - DataMap[NodeHead.i - 1][NodeHead.j].weight > 1:
                DataMap[NodeHead.i][NodeHead.j].weight = DataMap[NodeHead.i - 1][NodeHead.j].weight + 1
                DataMap[NodeHead.i][NodeHead.j].i = NodeHead.i - 1
                DataMap[NodeHead.i][NodeHead.j].j = NodeHead.j

    #check if weight to right is lower
    if (NodeHead.j + 1) <= n - 1:
        if DataMap[NodeHead.i][NodeHead.j + 1].weight + 1 < DataMap[NodeHead.i][NodeHead.j].weight and DataMap[NodeHead.i][NodeHead.j + 1].weight != -1:
            if DataMap[NodeHead.i][NodeHead.j].weight - DataMap[NodeHead.i][NodeHead.j + 1].weight > 1:
                DataMap[NodeHead.i][NodeHead.j].weight = DataMap[NodeHead.i][NodeHead.j + 1].weight + 1
    #check if weight below is lower
    if (NodeHead.i + 1) <= n - 1:
        if DataMap[NodeHead.i + 1][NodeHead.j].weight + 1 < DataMap[NodeHead.i][NodeHead.j].weight and DataMap[NodeHead.i + 1][NodeHead.j].weight != -1:
            if DataMap[NodeHead.i][NodeHead.j].weight - DataMap[NodeHead.i + 1][NodeHead.j].weight > 1:
                DataMap[NodeHead.i][NodeHead.j].weight = DataMap[NodeHead.i + 1][NodeHead.j].weight + 1
    #check if weight to left is lower
    if (NodeHead.j - 1) >= 0:
        if DataMap[NodeHead.i][NodeHead.j - 1].weight + 1 < DataMap[NodeHead.i][NodeHead.j].weight and DataMap[NodeHead.i][NodeHead.j - 1].weight != -1:
            if DataMap[NodeHead.i][NodeHead.j].weight - DataMap[NodeHead.i][NodeHead.j - 1].weight > 1:
                DataMap[NodeHead.i][NodeHead.j].weight = DataMap[NodeHead.i][NodeHead.j - 1].weight + 1

    return 0;


def f_weight_check(NodeHead):
    for x in range(n):
        for y in range(n):
            if DataMap[x][y].weight != -1:
                NodeHead.i = x
                NodeHead.j = y
                weight_check(NodeHead)
















def maze_map(map_info):
    global DataMap, StartEnd, n, maze_map
    maze_map = []
    n = int(map_info[0][0])
    for x in range(n):
        maze_map.append(map_info[3+x][0])

    DataMap = [[ structs.Map(0,0,0,0) for x in range(n)] for j in range(n)]
    for x in range(n):
        for y in range(n):
            if maze_map[x][y] == "1":
                DataMap[x][y].beenTo = 1
                DataMap[x][y].weight = -1
            else:
                DataMap[x][y].weight = n*n + 1

    StartEnd = structs.StartDest(int(map_info[1][0]), int(map_info[1][1]),int(map_info[2][0]),int(map_info[2][1]))
    DataMap[StartEnd.start_i][StartEnd.start_j].weight = 0
    DataMap[StartEnd.start_i][StartEnd.start_j].beenTo = 0


    return DataMap, StartEnd, n;

def visual_map():
    for x in range(n):
        for y in range(n):
            print(str(DataMap[x][y].beenTo).center(3), end="|")
        print()
    print()
    return 0;

main()
