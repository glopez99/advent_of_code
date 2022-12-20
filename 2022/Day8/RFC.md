# AoC 2022 Day 8
## Overview:
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a 
previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location
for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the 
number of trees that are visible from outside the grid when looking directly along a row or column.

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider 
trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to 
block the view.

## Glossary:

## Part 1:
### Goal:
Consider your map; how many trees are visible from outside the grid?

### Out of Scope:
What problems are you not trying to solve?

### Design:

#### Parsing:
We will model the trees into a class, `Tree`, with the fields of `height`, `left_neighbor`, `right_neighbor`, `up_neighbor`
`down_neighbor`, `visible`. The left/right/up/down will point to the `Tree` objects.

To create these models, we will parse the information twice. The first time will be to create a list of lists of `Tree`s. 
This pass will add in the `height` field, but leave the others empty. The key to the map will be the row number (ex 1, 2, 3)
and the value will be a list of the trees in that row.

On the second pass, we will then iterate through that map populating each trees neighbors. There will be a few checks
to write in to handle the edge trees, but otherwise, using the location of the tree in the map, we'll be able to find and
link it to its neighbors.

#### Solution:
Now that every tree has a height and its neighbors, we can iterate through the trees, setting their `visibility` field
by checking their height compared to that of their neighbors/neighbors-neighbors until the edge.

To do this, we can have a `decide_visibility` method in our tree class that sets booleans based upon the tree's neighbor's
height. This will have a check of whether the `visibility` is already `True`. If it is we can exit the method and move to 
the next tree. These checks will check the tree's height against it's neighbor's height, and if it's larger, it will then continue
checking against trees further down the row (using recursion) until it either returns a true or a false.

I'm curious as to whether we could use `or` logic in this method or whether we should just check one direction at a time.

Thinking we'll check one direction at a time, after we've checked the other directions, we can then combine the list of 
lists and filter it for trees' `visibility` that is true.

## Project Risks
There are no known risks to this project. 

## Alternatives Considered/Prior Art:






