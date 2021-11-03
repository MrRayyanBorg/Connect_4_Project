# Borg's Connect 4
Connect FOUR game created using Python.

Dependencies / Prerequisite:
  1. `import colorama` &#8594; used to allow colours within the console, differentiating player one & player 2.
  2. `import random`   &#8594; used to generate a random number within a Min,Max Range.
  3. `import copy`     &#8594; used to create deep copies of variables/methods.

## Challenge Outline
The initial challenge I chose to undertake was the popular game 'Connect FOUR'. A strategic game whereby players take turns dropping chips into a board in hopes of connecting four chips to win. There are many strategies behind this rather simple game, some of which I had to explore to incorporate into the AI bot, the goal of which was to create an intelligent bot which is smarter than random, and has the ability to beat many average-skilled players through favouring positions which increase its probability of winning and blocking its opponent from taking winning positions to decrease its chances of losing.

### Summary and review of the problem, overall proposed solution

With the creation of the initial game, I wanted to ensure I wasn't using any libraries which would take away from the complexity of the project, for example using a library such as 'numpy' would allow for complex operations to be shortcutted, hence, taking away from the project's complexity.

My proposed solution for overcoming the project's complexity was to use an object-oriented approach, creating modules to store functions, and ensuring these functions were *pure* meaning they do not have any side effects.

As the scope of creating an intelligent bot is extremely complex, my initial solution was to first `import random`, enabling me to use the `random.randint(min,max)` function to allow the bot to randomly select a position on the board which was available. However, this was not at all complex and my main goal was to create something which is *hard to beat*, hence, I used a basic algorithm to score each of the columns, allowing the bot to choose the best position every turn.

### UML style diagram illustrating initial overall solution
UML is a standard language used for designing and documenting a system in an object-oriented manner. Below is identified as a structural diagram and outlines how the program is structured with regards to Modules and classes.

![image](https://user-images.githubusercontent.com/42804334/140051952-14a33f5a-2a9b-4ce1-8734-71d9c2239011.png)


### Initial working plan, overall approach, development strategy and approach to quality
My initial plan when starting this project was to understand the rules of Connect FOUR first, this is because the full set of rules must be understood in order to code the rules of the game for users to follow. I would use levels of abstraction and decomposition to simplify complex problems into small steps to create simple solutions. I would then plan to build onto the basic functionality, introducing validation related commits, as well as ensuring the game state and user input validations were in order.

My object oriented approach meant my code would be relatively easy to understand as the major functionalities were split into modules, to then be imported into the `main.py` script. This also relates to my approach to quality as the code is readable, and can be easily maintained in the event of error.

### Analysis and decomposition of the overall problem into key ‘epic’ style tasks
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

### Initial object-oriented design ideas and planned phased breakdown into smaller tasks
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
### Adoption and use of ‘good’ standards
In order to use good coding standards I followed several steps when writing new code and to be applied to existing code, to ensure the coding standards followed were consistent and concise. These steps include:
  1. Write as few lines as possible as code blocks that are smaller in size are generally easier to understand and than large paragraph-like blocks.
  2. Use appropriate naming conventions within my constants and variables; this would make the use of variables easier to understand throughout the program.
  3. Use indentation to mark the beginning and end of controlled structures such as loops, conditional statements, and functions.
  4. Avoid deep nesting functions and ensure that they are pure - this did become a little hard to manage when using my modular approach as functions needed to be nested together to ensure they were kept simple and did not carry any side products.
  5. Following the DRY (Don’t Repeat Yourself) principle as it takes away from the efficiency of code due to duplication of code blocks.

### Development Phases: tasks, code review and changes
Phase | Tasks | Code Review | Description | 
--- | --- | --- | --- |
Phase 1: Board | <ul><li>Creating the board</li><li>Finding open rows</li><li>Outputting board</li></ul> | ![image](https://user-images.githubusercontent.com/42804334/139970168-8e2be784-2c24-4c1b-95a2-3d81ada2056a.png) ✅Naming conventions&nbsp; ✅DRY principles&nbsp; ✅Indentation&nbsp; ✅Pure Functions | <ul><li>I had previously created the board using the numpy library, however I didn't want to use any shortcuts which may of impacted the complexity of the project, hence, the change to a 2D array.</li><li>Finding the next open row on a column has a great functionality of knowing where the chip goes, once a user selects a column.</li><li>Outputting the board was done in two steps, first flipping the board to ensure it started from the bottom up, then using a for loop to output each row of the board, stacked ontop of one another.</li></ul> |
Phase 2: Menu | <ul><li>Creating the menu screen</li><li>Creating the gameover screen</li></ul> | ![image](https://user-images.githubusercontent.com/42804334/139970999-a7074c9c-12a2-4128-9a44-b8dad97a4265.png) ✅Naming conventions&nbsp; 🚩DRY principles&nbsp; ✅Indentation&nbsp; ✅Pure Functions ![image](https://user-images.githubusercontent.com/42804334/139972407-32bdb92c-af67-49cc-b898-109636f79873.png) ✅Naming conventions&nbsp; ✅DRY principles&nbsp; ✅Indentation&nbsp; ✅Pure Functions| <ul><li>I have flagged DRY princples as both of these functions repeat an 8-line code block which takes input from the user as the menu option, to mitigate this, I could create a new function to take input, then feed that function into each of the menu and gameover classes.</li></ul> |
Phase 3: Player | <ul><li>Allocating player colour</li><li>Adding player chip to board</li><li>Player win event</li></ul> | ![image](https://user-images.githubusercontent.com/42804334/139975029-f4e712e2-b635-4641-b963-307ce9012da9.png) ✅Naming conventions&nbsp; ✅DRY principle&nbsp; ✅Indentation&nbsp; ✅Pure Functions | <ul><li>Generally, I feel the development of this phase was clean, and made up of three very simple code blocks. I did have the oppourtunity to further normalize in having a seperate function to allocate the colours to each playerID, however I did not want to add any unnecessary complexity to my program.</li></ul> |
Phase 4: Validator | <ul><li>Checking column availability</li><li>Validating column input</li><li>Processing win condition</li></ul> | ![image](https://user-images.githubusercontent.com/42804334/139979017-1f8ea454-5889-46a0-b612-7595702a4f7c.png) ✅Naming conventions&nbsp; ✅DRY principle&nbsp; ✅Indentation&nbsp; ✅Pure Functions | <ul><li>The `column_slot_check` function is used within the program, to check if a column is full or has available space. This is usefull for ensuring users cannot go out of bounds with regards to the game board.</li><li>The `column_input` function validates the input of an integer from the user, this is a form of error handling whereby my main approach was to use a `try; except` block to catch **Value Errors**.</li></ul> |
Phase 5: Bot | <ul><li>Random position input (No longer used)</li><li>Check windows of oppourtunity</li><li>Score the position of a chip (Based on windows of oppourtunity)</li><li>Collate all valid column inputs</li><li>Process which column is the best</li></ul> | ![image](https://user-images.githubusercontent.com/42804334/139987523-df456217-5ae9-44d9-bd96-64d88142a513.png) ![image](https://user-images.githubusercontent.com/42804334/139999021-19c6c688-94dd-490c-a9ee-1fa8c9844530.png) ✅Naming conventions&nbsp; ✅DRY principle&nbsp; ✅Indentation&nbsp; ✅Pure Functions | <ul><li>The `random_number` function is a basic function to return a random column input for the bot - this is no longer used as the bots strategy</li><li>`check_window` is where the bot analyses a specific positions window (a space of 4 positions) to know whether it has the potential to win (3 friendly chips, 1 unallocated), or get lines of three counters (2 friendly chips, 2 unallocated), the `Score` variable shows you the weight i've attached to each oppourtunity, in order of priority. e.g. the bot will prioritise winning in all cases, or stopping the opponent from winning rather than getting a line of three chips.</li><li>The `score_position` function uses the `check_window` function on a specific position of the board, taking into account where the opponent has their chips, and where the bot has its chips. This is done a horizontal, vertical, positive diagonal, and negative diagonal slope.</li><li>`get_all_valid_columns` will use the validator module to check all columns that can be accessed, this is a simple tool which is very useful for ensuring the bot can only choose from available columns.</li><li>Finally, the function which strings all of this together, the `pick_best_move` function, this will analyse all valid columns, to then run a simulated analysis (using the .deepcopy function) on the outcome of a position if a chip were to be inserted. The `score_position` function would then assign a weight to each coilumn, and the column with the highest weight will be returned as `best_col`, this is the column that is selected by the bot.</li></ul> |


## Evaluation
This Evaluation section covers the evaluation of the project overall, including many key parts such as code refactoring, use of advanced principles, improved algorithms, and reflective review.
### Analysis with embedded examples of key code refactoring, reuse, smells
Within the implementation of my code, I tried to avoid the use of random numbers throughout the program to do this, I would assign these numbers to constants at the start of the program and use good naming conventions. This allows other uses looking in the program to understand what something is and why it's there. A good example of this would be  rows and columns of the game board as well as playerIDs and Player Turns.

![image](https://user-images.githubusercontent.com/42804334/140045527-323350d5-dca6-44a3-8484-6b19c8650b20.png)


Another example of having a good code smell would be my use of modules and object oriented approach these modules wood house functions in relation to the objects they referred to for example the board  module would use various functions within its class to relate to the board.

![image](https://user-images.githubusercontent.com/42804334/140045808-3916bbe5-67ed-45d7-9909-ceeb7bcf3010.png)

![image](https://user-images.githubusercontent.com/42804334/140045882-752e3b20-e6ea-4937-9fe8-3b2248ea47c7.png)


Another good example of having a good coat smell within my program was to reduce the repetition of code on to do this I've created functions within modules that can be cooled upon that prevent me from having to repeat code blocks.

![image](https://user-images.githubusercontent.com/42804334/140046242-4a211153-ec75-474f-b24e-afb472d244b0.png)

### Implementation and effective use of ‘advanced’ programming principles
With regards to my use of advanced programming principles I've ensured that my code uses an object oriented approach as well as a modular approach to keep code easy to manage and maintain there are various cases within my program encapsulation has been used as well as validation I never handling of user inputs my code also uses pure functions and methods meaning they do not carry any side effects and returned an expected value when run.

#### Evidence: Object Oriented Approach
![image](https://user-images.githubusercontent.com/42804334/140046692-3fb28619-6464-40a4-93df-708f41397f42.png)

#### Evidence: Pure Functions
![image](https://user-images.githubusercontent.com/42804334/140046766-bce3ee59-245d-441d-accd-ddc8820371e3.png)

#### Evidence: Modularity
![image](https://user-images.githubusercontent.com/42804334/140046817-757bdeaf-93f9-49ba-b95f-21a1d631bce1.png)

### Features showcase and embedded innovations
In regards to my Showcase of features an embedded Innovations I believe my main feature is the but which is somewhat hard to beat for an average player the bought uses an initial algorithm and I will talk about the improved algorithm within the next section however it features the ability to school Collins based on potential of winning losing and gaining the potential to win through a line of three chips.

![image](https://user-images.githubusercontent.com/42804334/140047080-d5a10215-6705-484f-a69f-893676c5ce66.png)

I'm guilty of losing to my own bot however I know that the strategy of this bot can be improved several times through something like a Minimax method, which is an algorithm used in many board games which will score positions based on the next couple positions it opens up to. using all of this data the Minimax method will choose the best column to input. My implementation of this is similar to the Minimax algorithm in the sense that the bot will look for winning positions and lines of three, and also blocks the opponent from winning however my bot does not look at the potential of potential positions meaning it doesn't go down more than one layer, where is the Mini Max  method can go down to seven layers making it several times smarter.

![image](https://user-images.githubusercontent.com/42804334/140047877-3d3ecd56-e160-41f4-a001-6a32b188ed25.png)

### Improved algorithms – research, design, implementation, and tested confirmation
As I said the way to improve my botd algorithm would be to make you use of a Minimax algorithm whereby my bot is able to score positions based on future positions that open up. As recollected my bot can only stick down to one layer of thinking meaning it thinks one step ahead, whereas the most advanced bots can think 7 steps ahead.

![image](https://user-images.githubusercontent.com/42804334/140048319-955c9645-0680-49a9-901b-91f3027d8a7e.png)

The image above represents the scoring mechanism my bot uses. It in an order of priority where a winning position would be very highly prioritized over a `line of three` and The blocking of an opponent's winning position would be prioritized over a `line of three`,  `a line of three` would also be prioritised over a line of to for example.

### Reflective review, opportunities to improve and continued professional development
To review upon this project I believe there were many areas that I could have improved upon to ensure the delivery of the projects within the time frame firstly making use of a time management plan for cancer would have benefited me greatly in ensuring the delivery time for the project as I would have been able to plan out days rather than make use of guesswork in my head.

Another opportunity to improve my project was to add complexity by adding a third player to the game hence it would have made for a more fun game if there was 3 game modes as opposed to two, but relating back to my earlier point this project had a tight deadline for its scope.

Lastly I believe the best way to gain more insight on my code, was through scheduling program reviews with my peers,  as it had given me a better understanding of where I could have improved my program and I added new features.
