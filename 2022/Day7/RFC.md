# AoC 2022 Day 6
## Overview:
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear 
much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

```
$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
```

Perhaps you can delete some files to make space for the update?

The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). 
The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and 
listing the contents of the directory you're currently in.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. 
To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the 
sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

## Glossary:

## Part 2:
### Goal:
The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. 
You need to find a directory you can delete that will free up enough space to run the update.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. 
What is the total size of that directory?

### Design:
#### Parsing:
No additional parsing needed.

#### Solution:
The first thing to do is to find how much space we need to free up to get the requirement. We can do that by taking the
size of directory "/" and subtracting that from the total disk space available.

Now that we have our limit, we can simply add a new method to the `Directory` class, that finds the smallest directory to
be deleted that would free up enough space, by finding every directory's size that is larger or equal to the limit, and 
taking the smallest one of those.

## Part 1:
### Goal:
Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

### Out of Scope:
What problems are you not trying to solve?

### Design:

#### Parsing:
First we are going to create a few classes called: `Directory` and `File`. `Directory` will have a `size` and `name` 
field and it will have a map of its subdirectories and files. `Directory` will have the ability to add files to its 
“contents” map. It will also have the ability to find all of the subdirectories within it. `File` will have a `size` 
and `name` field. 

While reading through the input, we are going to watch for two strings:  `cd {string}` and `cd ..`. Everything following
that does not start with `$` will be parsed into either a `File` or `Directory` depending upon the string. Ex. ‘dir e’ 
would create a `Directory` whereas ‘2557 g’ would be created into a `File`. These will then be added to the current `Directory`.

To keep track of which directory is the current directory files are being added to, we will have a list called, 
`current_directory`, that will live outside the line iteration. This variable will be updated when we come across 
`cd {string}` by adding the `{string}` or `cd ..` by popping the last element. This will keep our tree structure of 
the computer.

The only one oddity for this, is for the very first directory, `/`. That will need to be created before we can start 
reading through the the input.

#### Solution:
Now that our puzzle input is set up nicely for us by directory, this becomes a straightforward filter problem.

We will call start by finding all directories and subdirectories by calling that method for the directory, `/`. When 
this returns, we can than filter that list for any directory that has a size less than the limit and sum that filtered list.

## Project Risks
There are no known risks to this project. 

## Alternatives Considered/Prior Art:






