# Mazeworld
AI that navigates a maze using informed search algorithms.

## Bansharee Ireen

COSC76
14 Oct, 2022

## How To Run

### Mazeworld

Simply run the test cases in `test_mazeworld.py`. You can add more test cases by varying the goal states and the maze file read.

### Sensorless Robot

Simply run the test cases in `test_sensorless.py`. The code to run the test cases is very similar to that of the provided example code for mazeworld. Simply create a `SensorlessProblem` object and then run `astar_search` on it. The `animate_maze` method has been altered to display the robot's belief state as it changes. Run `animate_maze` as previously done for mazeworld problems (also as show in the test cases in `test_mazeworld.py`).

## Assumptions

### Mazeworld

- A robot may choose not to move, even if there are spots it can move to, if it decides that the cost of not moving is smaller or equal to the cost of moving. I was not sure if it should only stay in place if it did not have anywhere else to move to.
- The maze given to the search is rectangular (`length` by `width` cells) and valid, that is, it uses the characters `#` to represent obstacles and `.` to represent floors.

### Sensorless Robot

- The number of floors is limited to the number of ASCII characters. Not doing so, as in maze8, causes empty floors to be displayed in locations that have robots when running `animate_maze`.