# AoC 2022 Day 9
## Overview:
This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.

You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; 
maybe you can even figure out where not to step.

Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far 
enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a 
two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can 
determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always 
be touching (diagonally adjacent and even overlapping both count as touching).

You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail 
both start at the same position, overlapping.

## Glossary:
    
## Part 1:
### Goal:
Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?

### Out of Scope:
What problems are you not trying to solve?

### Design:

#### Parsing:
We will create a class called `Instruction` that keeps track of the `direction` and `times`.

We ultimately will be returning a list of `Instruction`s called `instructions`. As we go through the input, we will split the string into a
direction and times. We will create a new instance of `Instruction` passing in the appropriate direction and times. That
instance will then be added to `instructions`.

#### Solution:
We will create class called `Rope_Segment` that keeps track of the `x` and `y` coordinates for that segment of rope.
This class will also have two methods, `move` and `follow`. Neither method will return anything. `move` will take a direction
as the parameter and will adjust the appropriate coordinate by 1. `x` will be changed by the directions `right/left` and
`y` will be changed by the directions `up/down`. `follow` will take a `Rope_Segment` as a parameter and will adjust the 
coordinates based upon the passed in `Rope_Segment`'s coordinates. (i.e. ensuring the segments are touching).

After we parse the input, we will create three variables, `head` and `tail`, that are `Rope_Segment`s, and a `tail_locations` 
that is a set. We will then iterate through the parsed input, instruction by instruction. For each direction we will call the
method, `move_rope`. `move_rope` will take an instruction as a parameter. `move_rope` will return a set that will
be joined with `tail_locations`

In `move_rope`, we will loop through the following logic: we will first call `move`, passing in `instruction.get_dir` as
the argument on the `head` followed by calling `follow` on the `tail` passing in the new `head` as the argument. We 
then will add a tuple of `tail.x` and `tail.y` to a local `tail_locations` set. This loop of logic will be repeated the 
appropriate number of times based upon `instruction.get_times()`.

After iterating through all of the parsed directions, we will take the size of `tail_locations` for the answer to part one.

## Project Risks
There are no known risks to this project. 

## Alternatives Considered/Prior Art:






