# Overview
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant
Rock Paper Scissors tournament is already in progress.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say
will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C
for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for
each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for
Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

## Glossary
- Rock, Paper, Scissors - Rock Paper Scissors is a game between two players. Each game contains many rounds; in each
round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for
that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose
the same shape, the round instead ends in a draw.

## Part 1

### Goal
Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if
you were to follow the strategy guide. What would your total score be if everything goes exactly according to your
strategy guide?

### Out of Scope
What problems are you not trying to solve?

### Design

#### Parsing
In a hopefully useful optimization, I am going to start building out my parsers into a parser file, so that they can
be reused as the days go on. This way, hopefully, more time can be spent on the solution, and less on the parser.
Instead just calling the appropriate parser for that day.

Today’s parser will be titled, `list_with_stripped_whitespaces.` As the name suggests, this parser will return a list
where all whitespaces have been stripped from it. My reasoning behind this being, all that we really care about from
this input are the combinations, i.e. ay, bx, cz. Those combinations are what will define our points.

I did consider renaming all of these to rock, paper, scissor for a couple of reasons (namely, readability of the code
from an outsider). But ultimately, I decided this would be unneeded complication and would actually limit me should
the encryption change in any way.

#### Solution
To solve this problem, I will iterate through the parsed input and scoring each line. I will keep track of the sum
total via the variable `total_score`. At the end of the iteration, all I need to do is print `total_score`.

To score each line, I will create a dict with all the scoring named `possible_total_scores`. The keys will be the
combination and the values will be the combined scores (taking points for the outcome and for the shape selected).
For example, `{"AX": 4, "AY": 8, "AZ": 3}`

I have debated back and forth a bit on whether doing a combination of the score is the best option or if it’s better
to split out the score to a `outcome_score` map and `shape_score` map. I ultimately decided on doing the combination as
a slight preemptive optimization. I am betting that at some point (part 2),we will learn that the cheat sheet is
“incomplete” or “wrong” and that  we will want to optimize the cheat sheet to get the best score possible, using some
logic (ex. 2 wins in a row followed by a loss or a draw).. By doing a combination of the scores, I can quickly choose
the best option (highest, middle, lowest) score, since dict look up is O(1). For example to choose the highest point
value every round, I can do `max(possibleScores[{whatTheElfChose}], key = possibleScores[{whatTheElfChose}].get)`

Even if that is not the case though, by having them combined, I feel I am not constrained as long as I ensure to have
proper comments in the code so that future Greg understands what is happening.

## Project Risks
There are no known risks to this project.

## Alternatives Considered/Prior Art