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

## Part 2:
### Goal:
Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head of the rope and 
moves according to the series of motions. Each knot further down the rope follows the knot in front of it using the same 
rules as before.

Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope 
visit at least once?

### Out of Scope:
What problems are you not trying to solve?

### Design:

#### Parsing:
No additional parsing needed

#### Solution:
We will start by creating a class called `Rope` that will keep track of `Rope_Segments` in the rope via an array called,
`rope_segments`. It will have the following methods:`get_head`, `get_tail`, `move_segments`, and `add_segment_to_end`.
`get_head` and `get_tail` will return the first/last `Rope_Segments` in the `rope_segments`. 
`move_segments` will take a direction as a parameter. `add_segment_to_end` will take a `Rope_Segment` as a parameter, adding it
to the end of the `rope_segments` array.

In `move_segments` it will first call `move`, passing in direction as the argument on `rope_segments`' first element's `move`. 
This will be followed by iterating through the remaining elements in `rope_segments` and calling`follow` using the 
previous' element as the parameter.

Now that we have a `Rope` class, we will create 10 `Rope_Segments`, adding each of those segments to the `Rope` class.

We will need to adapt `move_rope` to take a `Rope` instead of taking two `Rope_Segments`. We will also need to adapt it
to just call `move_segments` on the `Rope` passing in `instruction.get_dir` as the parameter. Since the `Rope` class is
handling the `move` and `follow` for all of the sections, we will need to create a local variable `tail` that calls 
`Rope.get_tail()`. Using that variable we can then add the tuple (tail location) to our set.

Once we have iterated through all of the instructions, we can take the size the `tail_locations` set for our answer.

Since we are doing some refactoring, we'd like to propose refactoring our `follow` method in our `Rope_Segment` class to
first check if the segments are touching and if not, using `signum` to update the location. By doing this change, the
`follow` method becomes easier to read.
    
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






