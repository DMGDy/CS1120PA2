# CS1120 Spring 2022 PA2

'''
    This method takes an input file name, constructs a map from the input file data, and finds the path
    from source to destination for those values defined in the file. (add more documentation here. what parameters?
    what do they mean? what gets returned? How does this method work?)
'''
def create_map_find_path(file_name):
    # create map from input in file

    # find path from source to destination on map

    # return path

'''
    This method traverses a map and returns a path from the current element being visited to a destination.
    (add more documentation here. what parameters?
    what do they mean? what gets returned? How does this method work?)
'''
def find_path(curr_pos, dest_pos):
    # Use DCG to design a recursive solution for finding a path in a maze

    # First, must establish the base cases

    # Next, how to apply DCG? How many directions/scenarios? How many subproblems? How to solve the subproblems?

    # How to glue the solutions together?

'''
    This method prints a path list of coordinates. (add more documentation here. what parameters?
    what do they mean? what gets returned? How does this method work?)
'''
def print_path(pathList):

    print(pathList)


if __name__ == '__main__':

    # get an input file name from user
    file_name = input("Please supply an input file name to create a map and find a path from src to dest.\n")

    # create a map from given data in the input file and find a possible path from starting coord to destination
    soln_path = create_map_find_path(file_name)

    # print the solution
    print_path(soln_path)

