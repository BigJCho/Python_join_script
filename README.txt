This is an assignment from my Databases course within my Master's of Computer Science program

The purpose of this script is to re-create how database software would execute join functions in 3 ways.
It is meant to take 2 csv files in as input and output a csv file.

Method 1: nested loop join, wherein the table will be joined by iterating through file2 for every entry of file1 to find a match.

Method 2: merge join, wherein the table will be joined by sorting both files and iterating through them at the same time to find a match.

Method 3: hash join, wherein the table will be joined by hashing the key of the first file into a dictionary, then iterating through the second file and hashing each key, outputting any matches where the key is contained in the dictionary.

