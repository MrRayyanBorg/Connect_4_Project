# Borg's Connect 4
Connect FOUR game created using Python.

Dependencies / Prerequisite:
  1. `import colorama` &#8594; used to allow colours within the console, differentiating player one & player 2.
  2. `import random` &#8594; used to generate a random number within a Min,Max Range.
  3. `import copy` &#8594; used to create deep copies of variables/methods.

## Challenge Outline
The initial challenge I chose to undertake was the popular game 'Connect FOUR'. A strategic game whereby players take turns dropping chips into a board in hopes of connecting four chips to win. There are many strategies behind this rather simple game, some of which I had to explore to incorporate into the AI bot, the goal of which was to create an intelligent bot which is smarter than random, and has the ability to beat many average-skilled players through favouring positions which increase its probability of winning and blocking its opponent from taking winning positions to decrease its chances of losing.

**Summary and review of the problem, overall proposed solution**

With the creation of the initial game, I wanted to ensure I wasn't using any libraries which would take away from the complexity of the project, for example using a library such as 'numpy' would allow for complex operations to be shortcutted, hence, taking away from the project's complexity.

My proposed solution for overcoming the project's complexity was to use an object-oriented approach, creating modules to store functions, and ensuring these functions were *pure* meaning they do not have any side effects.

As the scope of creating an intelligent bot is extremely complex, my initial solution was to first `import random`, enabling me to use the `random.randint(min,max)` function to allow the bot to randomly select a position on the board which was available. However, this was not at all complex and my main goal was to create something which is *hard to beat*, hence, I used a basic algorithm to score each of the columns, allowing the bot to choose the best position every turn.

**UML style diagram illustrating initial overall solution**


**Initial working plan, overall approach, development strategy and approach to quality**
My initial plan when starting this project was to understand the rules of Connect FOUR first, this is because the full set of rules must be understood in order to code the rules of the game for users to follow. I would use levels of abstraction and decomposition to simplify complex problems into small steps to create simple solutions. I would then plan to build onto the basic functionality, introducing validation related commits, as well as ensuring the game state and user input validations were in order.

My object oriented approach meant my code would be relatively easy to understand as the major functionalities were split into modules, to then be imported into the `main.py` script. This also relates to my approach to quality as the code is readable, and can be easily maintained in the event of error.

**Analysis and decomposition of the overall problem into key ‘epic’ style tasks**
This section is a breakdown of key tasks which need to be complete in order for the program to properly function as the intended game.
  1. Create the game board
  2. Create Player entities
  3. Build Turn Alternator
  4. Allow Users to input column
  5. Validate user inputs
  6. Apply user chip to game board
  7. Activate Turn Alternator after every input
  8. Check Win Condition after every turn alternation
  9. If a player wins - Output it
  10. else - continue

Ofcourse these can be further decomposed into smaller and smaller problems, but having the major objectives outlined generated a structure for me to abid by in order to complete the development of the game.

**Initial object-oriented design ideas and planned phased breakdown into smaller tasks**
As my game already uses an object oriented approach whereby major components are broken down into Modules, I will list out each of these modules, as well as their associated functions to give a better understanding of how the program was initially designed.

Module | Class | Class description | 
--- | --- | --- |
Board | `create_board()` | Creates the initial board, set using constant variables `ROW_COUNT` and `COLUMN_COUNT` |
Board | `flip_board()` | Inverts the board along the Y-axis, giving the illusion of gravity on the game board |
Board | `print_board()` | Loops throught the board to output each row |
Board | `get_next_open_row()` | checks a specific column of the board to find the position of the unoccupied column, closest to the bottom |
Menu | `menu_screen()` | Outputs the initial menu, allowing input from the user as the `menu_option` |
Menu | `gameover_screen()` | Outputs the initial game over screen, allowing input from the user as the `menu_option` |
Player | `colour_selector()` | Sets a colour to each corresponding player, based on PlayerID | 
Player | `add_chip()` | Adds a chip to the board based on playerID | 
Player | `player_win()` | Outputs which player won, in the specific player colour | 
Validator | `column_slot_check()` | Shuffles all the cards in the deck |
Validator | `column_input()` | Matches player card to the card at the top of the deck, includes handle for Wild card |
Validator | `validate_win()` | Finds wild card and resets its color back to black | 
Bot | `random_number()` | Runs's all functions required to initialise a new game | 
Bot | `check_window()` | Returns all cards in the computer hand | 
Bot | `score_position()` | Returns all cards in the player hand | 
Bot | `get_all_valid_columns()` | Returns deck |
Bot | `pick_best_move()` | Displays count of player and computer cards and displays all cards in player hand |

As you can see, I've listed the modules in order of *date of implementation*, meaning the modules at the top were higher phases which had to be complete before going onto the more advanced aspects. To give context, i've listed out the phases below:
  * Create Board Module for everything related to the Board.
  * Create Menu Module for user navigation through game states and modes.
  * Create Player Module for players to interact with the game.
  * Create Validator Module to validate all inputs through prevention and mitigation of errors.
  * Create Bot Module to add complexity and allow user to be challenged by the computer.

The first three phases were to get the basis of the game started and functioning properly, hence their prioritisation. The last two phases were to make the program more effective in handling errors, as well as adding an additional part to the game allowing for a single player mode against an intelligent bot, making the development of the game more complex overall.

## Development
* a. Adoption and use of ‘good’ standards (linked to 1a, 1b, 1c).
* b. Phase 1 development: tasks, code review and changes (linked to 1d,1e).
* c. ..repeated for each development phase.
* d. Phase n development: tasks, code review and changes (linked to 1d,1e).
* e. Ensuring quality through testing and resolving bugs (linked to 1a, 1b, 2a, 2b..2c).
* f. Reflection on key design challenges, innovations and how they were solved (with examples).

## Evaluation
* a. Analysis with embedded examples of key code refactoring, reuse, smells.
* b. Implementation and effective use of ‘advanced’ programming principles (with examples).
* c. Features showcase and embedded innovations (with examples) - opportunity to ‘highlight’ best bits.
* d. Improved algorithms – research, design, implementation, and tested confirmation (with examples).
* e. Reflective review, opportunities to improve and continued professional development.
