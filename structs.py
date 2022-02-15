class CurrentPosition:
    def __init__(self,i,j,weight):
        self.i       = i;
        self.j       = j;
        self. weight = weight;

        pass;

    pass;

class StartDest:
    def __init__(self,start_i,start_j,end_i,end_j):
        self.start_i = start_i;
        self.start_j = start_j;

        self.end_i   = end_i;
        self.end_j   = end_j;

        pass

    def starting_pos(self):
        return (self.start_i,self.start_j);

    def dest_pos(self):
        return (self.end_i,self.end_j)

    pass

class Map:
    def __init__(self,j,i,weight,beenTo):
        self.j  = j;
        self.i  = i;
        self.weight = weight;
        self.beenTo = beenTo
        pass
    pass



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
    temp = less_bloated_split(map_text[line]," ");
    map_info.append(temp);

