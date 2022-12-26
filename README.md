# Advent-of-Code
https://adventofcode.com/

From the website:

>Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.

>You don't need a computer science background to participate - just a little programming knowledge and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.

>If you'd like to support Advent of Code, you can do so indirectly by helping to share it with others, or directly via [PayPal or Coinbase](https://adventofcode.com/2022/support).

This repository contains my original work solving Advent of Code puzzles. Most often I'll likely use Python for my solutions.

If I needed assistance or inspiration for solving the puzzle, I will make every attempt at crediting the source. I often attempt solving puzzles late at night, so documentation may come later. Usually, if I used other code for the puzzle, it will be named "dayXXstolen" with the appropriate extension.

When ChatGPT came out this year, I've also attempted to see what it can do to assist solving puzzles. Those files should be named "dayXX-chatgpt" with the appropriate extension.

## Program Interaction

I plan to write a wrapper script to be placed here in the root directory which can be used to access all other solutions. Until that time, I've lay out a few design goals I decided on to make writing the code and running the solutions easier. Not all solutions will use this but I'll attempt to go back and edit to do so later on.

- Allow switch --debug for debugging messages
- Write to allow positional parameters for file input
- For python at least, code to allow inclusion as a library. (i.e. __name__ == "__main__")
