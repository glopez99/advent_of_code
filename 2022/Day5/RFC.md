# Overview:
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks
of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or 
fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are 
rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which 
crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). 
In each step of the procedure, a quantity of crates is moved from one stack to a different stack. Crates are moved one 
at a time, so the first crate to be moved ends up below the second and third crates.

# Glossary:

# Part 1:
## Goal:
The Elves just need to know which crate will end up on top of each stack. After the rearrangement procedure completes, 
what crate ends up on top of each stack?

## Out of Scope:
What problems are you not trying to solve?

## Design:
### Parsing:
The first thing to do in the parsing is to create two classes that model `cargo_hold` and `cargo_stack`. The 
`cargo_hold` class will hold the `cargo_stack` models, which will be a deque of the boxes in that stack.

Until we come upon a line that doesn’t start with “[“ we will split that line every 4 characters. This will allow us to 
know which stack to put the box in. We can map it by its index + 1, i.e. line[0] goes into stack 1. Since, splitting 
the line by characters, this will account for empty strings (which are used in the input for visualization purposes). 
We can have a check that if it is an empty string, we can just continue on and not pass anything in.

We will have to assign names to each stack which will be the number that stack is, which again we know by the index of 
the box + 1. This can be done by checking if that stack exists yet. If not, we can create it. If so, we can just add 
the box to it. 

Once we reach the line that has the numbers of each stack and the empty line, we can skip those lines. 

Then to parse the remaining lines, we’ll parse each line into a class that models the instructions. The class will be 
called `instruction` and have the fields: `number_of_boxes`, `from_stack`, and `to_stack`. We will add all of those 
instructions to a list.

### Solution:
To solve we need to go instruction by instruction, moving the appropriate number of boxes from one stack to the other. 

To do this, we will create a method in `cargo_hold` that will handle moving a number of boxes from one stack to another.
This way since `cargo_hold` owns the information for the stacks, it alone gets to modify that data. 

At the end of this, we can take the top box from each stack and return them.

## Project Risks
There are no known risks to this project. 

## Alternatives Considered/Prior Art:
