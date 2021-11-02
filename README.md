# Borg's Connect 4
Connect FOUR game created using Python.

Dependencies / Prerequisite:
  1. 'import colorama' &rarr used to allow colours within the console, differentiating player one & player 2.
  2. 'import random' &rarr used to generate a random number within a Min,Max Range.

## Challenge Outline
The initial challenge I chose to undertake was the popular game 'Connect FOUR'. A strategic game whereby players take turns dropping chips into a board in hopes of connecting four chips to win. There are many strategies behind this rather simple game, some of which I had to explore to incorporate into the AI bot, the goal of which was to create an intelligent bot which is smarter than random, and has the ability to beat many average-skilled players through favouring positions which increase its probability of winning and blocking its opponent from taking winning positions to decrease its chances of losing.

* a. Summary and review of the problem, overall proposed solution.
With the creation of the initial game, I wanted to ensure I wasn't using any libraries which would take away from the complexity of the project, for example using a library such as 'numpy' would allow for complex operations to be shortcutted, hence, taking away from the project's complexity.

My proposed solution for overcoming the project's complexity was to use an object-oriented approach, creating modules to store functions, and ensuring these functions were *pure* meaning they do not have any side effects.

As the scope of creating an intelligent bot is extremely complex, my initial solution was to first 'import random', enabling me to use the 'random.randint(min,max)' function to allow the bot to randomly select a position on the board which was available. However, this was not at all complex my main goal was to create something which is *hard to beat*, hence, I used a basic algorithm to score each of the columns, allowing the bot to choose the best position every turn.

* b. UML style diagram illustrating initial overall solution (linked to 1a)
* c. Initial working plan, overall approach, development strategy and approach to quality (linked to 1a, 1b).
* d. Analysis and decomposition of the overall problem into key ‘epic’ style tasks (linked to 1b, 1c).
* e. Initial object-oriented design ideas and planned phased breakdown into smaller tasks (linked to 1d).

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
