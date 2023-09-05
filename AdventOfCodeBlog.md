# Advent of Code Blog

Did not complete all days (completed ~1/3). 2d maze type problem (day 12), didn't get the right search algo. Will return to the challenges in 2023.

## Day 1

Simple reading lines and storing the values in array. Then using numpy to get single max and sum of max 3

## Day 2

Some dicts for rps winning mapping, and finding index of these strings to get the value to add. For A B C each a string and then for part 2 X Y Z to get the right rps value (1, 2, 3).

## Day 3

String char ascii values. Python has 6 special characters between lower and upper case. Intersection of strings in Python done through converting string to set and then calling .intersection. Remembering to sanitize input with '\n'.

## Day 4

Multiple if statements to see if one of the edge values of one section is in the other section. Edge cases for internal. In hindsight might not need the internal edge case.

## Day 5

Diff input. Needed some start string finding. In general easily solvable with list of stacks and then insertion instead of appending for part 2. Some issues with copying the list of stacks. Make sure to copy also all the stacks inside the list, or else they are passed by reference.

## Day 7

I might have made it more complicated than it had to be. Created a Node class for the directory structure. Propagated the recursive directory size up through the tree. For part 1 go through tree and add any directories with less than 1e5 to output. For part 2 recursively get list of directory sizes, sort and find first that is more than required empty space needed.

## Day 10

Messed up the edges HMMMMMM.

## Day 11

Part 1 worked quite well and is very straight forward. Coming up with the modulous for part 2 is managable. The tricky part was with python on this one.
First I tried using string to lamba conversion with `eval()`, but the main problem was python typing.

`mFunc = lambda x: eval(monkeLamb[i].strip())`

Got overflows because the type was long for some reason, maybe??? Fixed this with using `int()` for the rest. Spent too much time on this one.
