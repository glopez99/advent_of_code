# AoC 2022 Day 6

## Overview:
As you move through the dense undergrowth, one of the Elves gives you a handheld device. He says that it has many fancy 
features, but the most important one to set up right now is the communication system.

However, because he's heard you have significant experience dealing with signal-based systems, he convinced the other 
Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.

As if inspired by comedic timing, the device emits a few colorful sparks.

To be able to communicate with the Elves, the device needs to lock on to their signal. The signal is a series of 
seemingly-random characters that the device receives one at a time.

To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in the 
datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters 
that are all different.

The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify the 
first position where the four most recently received characters were all different. Specifically, it needs to report 
the number of characters from the beginning of the buffer to the end of the first such four-character marker.

## Glossary:

## Part 2:
### Goal:
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs 
to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather 
than 4.

How many characters need to be processed before the first start-of-message marker is detected?

### Design:

#### Parsing:
While coding Part 1, we realized, we don’t even need to split it into a list, we can keep it as a string and splice the 
string to get the grouping.

#### Solution:
Using the method we created in part 1 to find the start of the packet for a size 4, we can refactor that to take a 
variable, `number_of_chars`, to get the correct group size, check the length, and add to the position in the return. 
(Note, we need to add it to the position since we’re starting at location 0 in the iteration, but it’s looking for the 
position of the last character in the group.)

Once this is refactored, we simply pass in 14 when calling the method for part two.

## Part 1:

### Goal:
How many characters need to be processed before the first start-of-packet marker is detected?

### Design:

#### Parsing:
The parsing on this one is rather straightforward of taking the input and splitting it into a list.

#### Solution:
We can utilize a set, `start_of_packet`, for the deduplication portion of this problem. Once that set’s length is 4, 
we know we’ve found the start of the packet marker.

Starting at the fourth element in the list, we can iterate through the parsed input creating a grouping of four elements, 
it and the three elements before it.  We can then change that list to a set and check if its size is equal to 4, 
indicating that there are no duplicates. If it is, we return the current location we’re at in the list, adding one to 
account for the list being an index 0, but advent of code being an index of 1.

## Project Risks
There are no known risks to this project. 

## Alternatives Considered/Prior Art:







