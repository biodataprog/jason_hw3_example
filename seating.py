#!/usr/bin/env python3

# you will have some code here to do the work
import argparse

parser = argparse.ArgumentParser(prog="Assign guests to Tables")

parser.add_argument('-g', "--guests", 
                    default="guests_20.txt",
                    help='list of guests')
parser.add_argument('-t', "--num_per_table", type=int, 
                    default=4, 
                    help='number per table')
args = parser.parse_args()

num_per_table = args.num_per_table
guestlistfile = args.guests
print(f'The guestlist file is {guestlistfile}')
tables = []
guestscount = 0
# open the guestlist file

# read each line in the file
# add guests to the tables list
# but organize so for example it will look like
# tables = [ [ guest1, guest2, guest3, guest4],
#            [ guest5, guest6, guest7, guest8],
# ]
print(f'There are {num_per_table} per table requested, that means {int(guestscount/num_per_table)} tables')

print("Seating is as follows:")
for (idx, table) in enumerate(tables):
	print(f'Table {idx}: {", ".join(table)}')
