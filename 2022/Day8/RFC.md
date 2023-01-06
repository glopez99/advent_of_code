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

## Part 2:
### Goal:
The Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an 
edge or at the first tree that is the same height or taller than the tree under consideration. If a tree is right on the 
edge, at least one of its viewing distances will be zero.

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions.

Consider each tree on your map. **What is the highest scenic score possible for any tree?**

### Out of Scope:
What problems are you not trying to solve?

### Design:

#### Parsing:
No additional parsing will be needed.

#### Solution:
We can create a new method in our tree class to find it's scenic score called, `find_scenic_score`. This method will multiple
the distances of each direction to return a "scenic score" for that tree. It will call a method, `find_distance`.

The `find_distance` method will iterate through each of the directions (left, right, up, down) finding the distance to 
a tree that is an edge or is the same height /taller. It will be similar to the `check_neighbor` method in that it will 
check the  original tree's height against it's neighbor's. The difference will be instead of returning a boolean, it will
return an int of how far that tree's visibility is.

One of the edge cases we'll have to watch for is trees on the edge. If the tree being checked is an edge, it will automatically
return a zero since anything times zero is zero.

With this method, we can filter the tree list and take the max.


## Part 1:
### Goal:
Consider your map; how many trees are visible from outside the grid?

### Out of Scope:
What problems are you not trying to solve?

### Design:

#### Parsing:
We will model the trees into a class, `Tree`, with the fields of `height`, `left_neighbor`, `right_neighbor`, `up_neighbor`
`down_neighbor`. The left/right/up/down will point to the `Tree` objects.

To create these models, we will do our parsing in two passes. The first time will be to create a list of lists of `Tree`s. 
This pass will add in the `height` field, but leave the others empty. The key to the map will be the row number (ex 1, 2, 3)
and the value will be a list of the trees in that row.

On the second pass, we will then iterate through that map populating each trees neighbors. There will be a few checks
to write in to handle the edge trees, but otherwise, using the location of the tree in the map, we'll be able to find and
link it to its neighbors.

At the end of that second pass, we will consolidate the list of lists into a singular list of `Tree`s to be returned.

#### Solution:
Now that every tree has a height and its neighbors, we can filter our parsed list of `Tree`s based upon our `is_visible`
method.

Our `is_visibile` method sets booleans based upon the tree's neighbor's height. This will use `or` logic to check 
visibility in all directions, so that if one direction is visible, it will return `True`. To check this we will have two 
smaller methods, `is_edge` and `check_neighbor`. 

`is_edge` is a simple return of whether the tree is an edge based upon whether it is missing any neighbors. 

`check_neighbor` will check the original tree's height against it's neighbor's height, and if the original tree's height
is larger than it's neighbors, it will then continue checking the original tree's height against it's neighbor's 
neighbors further down the row (using recursion) until it either returns a true or a false. `check_neighbor` will take 
in the direction to check (i.e. left, right, up, down), so that we minimize duplicate code.

We can then take the length of that filtered list for our answer to part one. 

## Project Risks
There are no known risks to this project. 

## Alternatives Considered/Prior Art:






