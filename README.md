# Rock-Paper-Scissors App

* Let us look at writing a complete Rock-Paper-Scissors Program from scratch using Python.

* When we plan out a program like this, we actually write things out in normal human readable form, plan what we need, write out our business logic, and only then actually start writing code. **We call this an algorithm**.

Key things to lay out:

1. Types of players: human, computer
2. Human player moves - user input
3. Computer player moves - random selection from a list of moves
4. Compare the moves - what are the possibilities
```
r,r/r,s/r,p/s,r/s,s/s,p/p,r/p,s/p,p
```
5. What are the possible outcomes?
    * Tie
    * Did the human win? From the human's perspective, the options are: (`pr, sp, rs`)
    * Did the computer win?
    * Otherwise, we assume an invalid input

6. Tally score. Human vs. Computer

7. Ability for human player to break from the game with an entry like `q`

### Game Algorithm

Add your code to your `main.py`.

&nbsp;
>1. Set initial scores to 0 for:
  * `player_score`
  * `computer_score`
  * `ties`

&nbsp;
>2. Define a list `approved_moves` with the values: `r`, `p`, `s`

&nbsp;
>3. Define a list `winning_moves` with the combinations: `pr`, `rs`, `sp`

&nbsp;
>4. Ask keyboard user for input `(r, p or s)` and assign it to the variable `player_move`

&nbsp;
>5. Have the computer randomly pick from the list of approved moves and assign it to the variable `computer_move`. Use the imported `random` module as follows:
```
random.choice(<list>)
```

&nbsp;
>6. `print()` out both the `player_move` and `computer_move` values

&nbsp;
>7. Using the `if/elif/else` flow control statements:

* `if` the `player_move` is the same as the `computer_move`:
    * Increment `ties` by 1
    * print: `'Game is a draw'`

* `elif` the `player_move + computer_move` in `approved_moves`:
    * Increment `player_score` by 1
    * print: `'Player wins'`

* `elif` the `computer_move + player_move` in `approved_moves`:
    * Increment `computer_score` by 1
    * print: `'Computer wins'`

* `else`:
    * print: `'Invalid move. Please try again'` 

&nbsp;
>8. Use `f-strings` to print out a scoreboard like the following:
```
Scoreboard - Player: 1, Computer: 1, Ties: 1
```