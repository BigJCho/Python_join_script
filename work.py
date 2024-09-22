import sys

def joinalgorithm(file1: str, file2: str, destination: str, on: str, type: int) -> int:
    total = 0
    if type != 1 and type != 2 and type != 3:
        print("Type of join not defined.")
        print("Please enter 1, 2, or 3.")
        print("Exiting now.")
        sys.exit(1)
    elif type == 1:
        total = join_one(file1, file2, destination, on)
    elif type == 2:
        total = join_two(file1, file2, destination, on)
    elif type == 3:
        total = join_three(file1, file2, destination, on)
    return total

#Formats the header of the CSV file and returns the index of the joining key
def joincheck(file: str, on) -> int:
    with open(file, 'r') as file:
        header = file.readline().strip()
        words = header.split(',')
        try:
            index = words.index(on)
            return index
        except ValueError:
            print("On not found.\nExiting now.")
            sys.exit(1)
    return 0

#Identifies headline for writing to head of file
def header_line(file1: str, file2: str) ->str:
    with open(file1, 'r') as file1, open(file2, 'r') as file2:
        phrase1 = file1.readline().strip()
        phrase2 = file2.readline().strip()
        headline = phrase1 + ',' + phrase2
    return headline

#Nested loop join
def join_one(file1, file2, destination, on) ->int:
    print("Method 1, nested loop join")
    dest = open(destination, 'w')
    total = 0
    #Defining the index which needs to be value checked in the loop
    key_left = joincheck(file1, on)
    key_right = joincheck(file2, on)
    #Loop
    with open(file1, 'r') as left:
        for i in left:
            line = [word.strip() for word in i.split(',')]
            with open(file2, 'r') as right:
                for j in right:
                    line2 = [word.strip() for word in j.split(',')]
                    #Combine on each key == key
                    if line[key_left] == line2[key_right]:
                        #Format the list into a string so it can be .write()
                        out_list = line + line2
                        out = ','.join(out_list)
                        dest.write(out + "\n")
                        total += 1
    dest.close()
    return total

#Merge join
def join_two(file1, file2, destination, on):
    print("Method 2, merge join")
    total = 0
    dest = open(destination, 'w')
    #Find the index of the key used to be sorted
    index_left = joincheck(file1, on)
    index_right = joincheck(file2, on)
    #Find the headline to input at start and not enter again
    headline = header_line(file1,file2)
    dest.write(headline + '\n')
    #Populate 2 lists from the files to be sorted
    left = []
    right = []
    with open(file1,'r') as left_file:
        for i in left_file:
            left.append([word.strip() for word in i.split(',')])
    with open(file2, 'r') as right_file:
        for i in right_file:
            right.append([word.strip() for word in i.split(',')])
    #Sort using lambda with the indexes from above
    left.sort(key=lambda x: x[index_left])
    right.sort(key=lambda x: x[index_right])
    #Two pointers to loop through each list
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        #We have the index of the keys in index_left/index_right
        #Now i and j are associated with the line entry in the database
        if left[i][index_left] < right[j][index_right]:
            i += 1
        elif left[i][index_left] > right[j][index_right]:
            j += 1
        elif left[i][index_left] == right[j][index_right]:
            out_list = left[i] + right[j]
            out = ','.join(out_list)
            if out != headline:
                dest.write(out + "\n")
            total += 1
            j += 1
    dest.close()
    return total

#Hash join
def join_three(file1, file2, destination, on):
    print("Method 3, hash join")
    dest = open(destination, 'w')
    total = 0
    #Find where the index of the key is
    index_left = joincheck(file1, on)
    index_right = joincheck(file2, on)
    #Stores the hash of the key, and the entire entry in the dictionary left
    left = {}
    with open(file1, 'r') as file1:
        for i in file1:
            line = [word.strip() for word in i.split(',')]
            left[hash(line[index_left])] = line
    #Loop through file2, hash the key, then output matches
    with open(file2, 'r') as file2:
        for i in file2:
            line = [word.strip() for word in i.split(',')]
            key = hash(line[index_right])
            if key in left:
                out_list = left[key] + line
                out = ','.join(out_list)
                dest.write(out + "\n")
                total += 1
    dest.close()
    return total