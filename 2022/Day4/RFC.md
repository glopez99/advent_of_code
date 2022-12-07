# AoC 2022 Day 4
## Overview:
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been 
assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a 
range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the 
assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big 
list of the section assignments for each pair (your puzzle input).

Some of the pairs have noticed that one of their assignments fully contains the other.  In pairs where one assignment 
fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be 
cleaning, so these seem like the most in need of reconsideration.

## Glossary:

Part 2:
Goal:
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all. In how many assignment pairs do the ranges overlap?

Design:

Parsing:
No extra parsing is needed.

Solution:
To find how many assignment pairs are overlapping, we can perform a simple check using the start and end for both ranges. 

To perform this check we need to check that the elf 2’s start falls between elf 1’s range or that elf 1’s start falls between elf 2’s range. 

With the this check, we can run a filter on the parsed input and print the size of that filtered list.


## Part 1:
### Goal:
In how many assignment pairs does one range fully contain the other?

### Out of Scope:

### Design:

#### Parsing:
For this problem, we’re going to create a `camp_section` class. This class will have a `start` and `end` that will 
capture the start and end of the camp sections. Depending on part two of the question, I can add other fields to the 
class.

To that end, we will iterate through the input and split the line on the comma. We will then take each half of the 
string, and create a new `camp_section` for that section and add it to a local list. Once both `camp_section` have been 
created and added to the local list, that list will be added to the larger list to be returned at the end of the input 
iteration.

#### Solution:
To find how many assignment pairs have one range fully contained inside the other, we can perform a simple check using 
the start and end for both ranges. 

To perform this check we need to check that the start of elf 1’s range is less than or equal to the start of elf 2’s 
range and that the end of elf 2’s range is less than or equal to the end of elf 1’s range. If that proves to be false, 
we can check the opposite (so elf 2’s start is less than or equal elf 1’s start AND end of elf 1’s range is less than 
or equal to elf 1’s end).   

With this check, we can run a filter on the parsed input and print the size of that filtered list.

## Project Risks
There are no known risks to this project. 

## Alternatives Considered/Prior Art:







