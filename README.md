### Grading Rubric

You will be graded on the following criteria:

* [10 points] A reasonable history of `red-green-refactor` commits.
    Yes.
* [5 points] Test coverage for the expected "happy path", the most commonly expected error situations, and edge cases.
    Yes.
* [5 points] Code that is readable, well-tested and refactored.
    Yes.

### Instruction:

1. Open terminal
2. Start my app (python3) <br />
    $ python box_office.py
3. ? to list commands <br />
    `> ?`
4. Set today's date <br />
    `> setd 20180401`
5. Buy a ticket <br />
    command buy syntax -- buy movie_name date tier <br />
    `> buy my_movie_1 20180401 3` <br />
    *this will print ticket's serial number* <br />
    `> buy my_movie_2 20180401 4` <br />
    *this will print ticket's serial number* <br />
    `> buy my_movie_1 20180410 1` <br />
    *this will print 7-day warning* <br />
6. Refund a ticket <br />
    command refund syntax -- refund ticket_sn <br />
    `> refund 2018040101213` <br />
    *this will print refund done* <br />
    `> setd 20180402` <br />
    `> refund 2018040102314` <br />
    *this will print not-refundable warning* <br />
7. Show stats <br />
    command stats syntax -- stats date (screen_num) <br />
    `> stats 20180401` <br />
    *this will report the total tickets sold on given date* <br />
    `> stats 20180401 2` <br />
    *this will report the total tickets sold and unsold on given date for given screen* <br />
8. Quit <br />
    `> quit`