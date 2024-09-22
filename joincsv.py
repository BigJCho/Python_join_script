#Main method to join two CSV files
import argparse
import work
import sys
import time

#Beginning timer
start= time.time()

parser = argparse.ArgumentParser(description="Joins two csv files to a third destination on a column name.")
parser.add_argument("file1", type=str, help="The first file name")
parser.add_argument("file2", type=str, help="The second file name")
parser.add_argument("destination", type=str, help="The destination file name")
parser.add_argument("on", type=str, help="The \"on\" clause")
parser.add_argument("join_type", type=int, help="1, 2, or 3 based on algorithm to use")
args = parser.parse_args()

#Algorithms method will perform all the work and return the line count upon completion
total = work.joinalgorithm(args.file1, args.file2, args.destination, args.on, args.join_type)
print("Total " + str(total) + " lines written to file.\n")

#Displaying completion message with timer
end = time.time()
elapsed = end - start
print("Operation completed.\nTotal time elapsed: " + str(elapsed))

sys.exit(0)