# pangolins

A guess-the-animal game on the command line that interactively builds a decision tree.

## Dependencies

* Python3

No additional packages required.


## Running

```
$ python3 pangolins.py
```

## Example session

```
❯ python3 pangolins.py


Think of an animal... Are you ready? [y/n]
y
Does it live in the sea? [y/n]
y
Is it a Tuna fish? [y/n]
n
I give up!
What animal did you think of?
Sea turtle
Can you give me a question that is more specific than:
 --  Does it live in the sea? --
to which the answer -- Sea turtle -- would be true?
Is it a kind of reptile?
-------------------------------------------------------------
I will try my best to remember a Sea turtle.
-------------------------------------------------------------
Would you like to go again? [y/n]
y


Think of an animal... Are you ready? [y/n]
y
Does it live in the sea? [y/n]
y
Is it a Tuna fish? [y/n]
n
Is it a kind of reptile? [y/n]
y
Is it a Sea turtle? [y/n]
y
1 extra point for me! I now have 1 points.


Think of an animal... Are you ready? [y/n]
n
Thanks for playing!
```
