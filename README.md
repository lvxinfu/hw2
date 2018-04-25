# Homework #2

**DUE: April 25, 5:30pm**

For this assignment, we will learn how to take "legacy" code
and upgrade its design.

At the end of this assignment, the legacy code should be transformed
into beautiful code with a corresponding test suite that can assure
a certain level of code quality.

### Starting Point

You may start with the code you wrote for homework #1, or you can use
the included solution I wrote for the airline counter project.


### How To Turn In This Assignment

Create a repository named `hw2` and add Rachel and I as collaborators
(`rkillackey` and `jeffcohen`).



### Requirements

All of the previous requirements from homework #1 are hereby rescinded!

Convert the code into elegant, well-design software.

Specifically:

* Use well-named methods and files
* Handle error situations and edge cases
* Follow the DRY and Once-And-Only-Once principles
* Apply the Single Responsibility Principle as needed
* Adhere to other refactoring principles as appropriate
* Don't forget: YAGNI


### Procedure

Similar to homework #1, I am not overly concerned with the overall
functionality of the resulting code, nor am I very concerned with
your coding style or overall coding skills.

Instead, I am focused on your ability to incorporate a test-driven
*process* that can help you design software systematically without
being subject to the natural over-engineering that we all tend to do.

Therefore, the real challenge of this assignment is to work in very
tiny steps.  Since I am not sitting with you, you must take snapshots
of your code (git commits) every tiny step of the way.

By the end, you should have a very long commit history that provides
a play-by-play of every step you took in order to redesign the code.

**Red-Green-Refactor Commit History**

You should solve this assignment with the following procedure, using
the exact specific commit message (I am using an automated tool that
  will depend on these exact commit messages):

|What You Should Do|Then You Should...|Using This Exact Commit Message|
|------------------|------------------|-------------------------|
|1. Think of a failing test.  Write the test and verify that it fails. (If the test immediately passes, that's great too!)|Commit all changes|`red`|
|2. Modify the production code to pass the test|Verify that the entire test suite is green. Commit all changes.|`green`|
|3. Refactor the code to improve the design, if possible.|Verify that the entire test suite is green.  Commit all changes.|`refactor`|

Do not add embellish the commit messages!  Only use the words given above.

Repeat this cycle until you feel that the code is Good Enough. What is "Good Enough?"
It is when the code feels stable, is easier to read than when you started, and would
be amenable to change.  




### Grading Rubric

You will be graded on the following criteria:

* [10 points] A reasonable history of `red-green-refactor` commits.

* [5 points] Test coverage for the expected "happy path", the most commonly
  expected error situations, and edge cases.

* [5 points] Code that is readable, well-tested and refactored.
