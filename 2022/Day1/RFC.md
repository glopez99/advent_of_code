# AoC 2022 Day 1

## Overview
This year to save Christmas, we need to gather enough food for the reindeer, specifically the magical Star fruit that
helps them fly. Traveling with the elves, who are always tragically underprepared, to the grove where the magical fruit
grows, we start our journey.

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves expedition
traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One
important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc.
that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's
inventory (if any) by a blank line. This file is called the puzzle input.

## Glossary
- Puzzle Input: The file where the elves wrote their inventories that they brought. There is one item per line and each
    inventory is separated by a blank line. 
  - Ex.
     ```
     1000
     2000
     3000

     4000

     5000
     6000

     7000
     8000
     9000

     10000
    ```

## Part 2
### Goal
The Elf carrying the most Calories of food might eventually run out of snacks. To avoid this unacceptable situation,
the Elves would like to know the total Calories carried by the top three Elves carrying the most Calories.

### Design
Thanks to my preemptive optimization in part 1, part 2 is even more straightforward.

#### Parsing
This parsing part is already done and can be used in its current state. No changes are needed.

#### Solution
We can sort from most to least `sum_caloric_inventories` and then sum the first three items.

To do the sorting, we can use a built-in sorter, as it is a simple sort so there is no need to custom build one ourselves.

## Part 1
### Goal
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many
Calories are being carried by the Elf carrying the most Calories.

### Design
This is a straight-forward parsing question. To find the elf with the most calories, we need to read through the
puzzle input line by line, sum each elf’s inventory, and return the max. My proposed solve for this is:

#### Parsing
To start, we will parse the puzzle input into a list of lists of integers. This list of lists will be called
`elves_caloric_inventories`. To do this parsing, we will start by creating a variable array called, `elf_inventory`.
Iterating through the puzzle input, when a line contains a non-empty string, we will take that string, change it to an
Integer and add it to `elf_inventory`. Once we come upon an empty string, we will take the `elf_inventory` and add it to
`elves_caloric_inventories` and reset it to an empty list.

At the end of the puzzle input, we will put in the final `elf_inventory` to `elves_caloric_inventories`.

#### Solution
Now that we have the puzzle input parsed, we’ll create a new variable, a list called `sum_caloric_inventories`.

Instead of just looking for the max calories,  the `sum_caloric_inventories` is a preemptive optimization for part 2, as
I am guessing we will need to do something with every elf’s inventory. Possibly seeing how many days we can last in the
jungle before needing to turn back.  (I will note that this optimization might not be useful, but since we are already
iterating through the puzzle input and will be calculating the sum of each elf’s caloric inventory, saving them into an
array is pretty low cost in my opinion.)

We’ll iterate through `elves_caloric_inventories`, summing each list and adding that sum to `sum_caloric_inventories`.

Once we reach the end of the puzzle input, we can print the max of the `sum_caloric_inventories`.

## Project Risks
There are no known risks to this project.

## Alternatives Considered/Prior Art:
As this is day 1, there are no prior or alternatives considered. As the days go on, I will use this section to see if I
 can reuse previous days solutions with minor changes.
