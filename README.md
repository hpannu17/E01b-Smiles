# E01b-Smiles
An exercise exploring variables and loops using Python Arcade.

This repository contains several files that you will need to alter to complete the assignment. The instructions for the exercise are also on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

As with your assignments, please edit the LICENSE file (replace the [year] [fullname] with the current year and your name); you will also be expected to edit README.md (this file) to describe what you have accomplished.

---

As always, Fork this repository, and then Clone it to your local computer.

Before you begin, you will need to install Python Arcade, the graphics library we will be using for the first half of the semester. Open the Terminal (either by clicking on the magnifying glass and searching for CMD, or open the Terminal in VS Code) and type the following:

*pip install arcade --user*

pip is a tool for downloading and installing Python packages. arcade is the name of the package we will be using. When you type the command, you should see the components it is installing (with corresponding progress bars).

When arcade has been installed, we can get to work:

First, open main1.py. I am drawing several shapes that, if properly assembled, can form a smiley face. Right now, the shapes are all being drawn at (0,0), which is the bottom-left corner of the window. See if you can use those shapes to draw a smiley face in the center of the window. The small gray dots are catch lights for the eyes.

The end result should look something like this:

![Smile!](https://github.com/BL-MSCH-C220-F19/E01b-Smiles/blob/master/smile.png)

When you have placed the shapes correctly, save the file and open main2.py. The only change I have made is to define coordinates (face_x and face_y) that represent the center of the circle. Figure out offsets for the other shapes in relation to face_x and face_y. Use face_x and face_y to move all the shapes to the middle of the window. Save your changes.

Next, in main3.py, I have created several new coordinates to represent each of the shapes: smile, eye1, eye2, catch1, and catch2. Use what you learned in main2.py to define each of those coordinates in relation to face_x and face_y. Move the face to the middle of the window. You should only have to edit lines 13 through 18. Save your changes.

Open main4.py. You will now be drawing many faces in the window. Editing lines 20 through 24, draw a grid of overlapping faces. Now, play with the values on lines 16 and 18. What happens when you adjust those numbers? Save your changes.

What happens is that it affects where the smiles are placed on the window, like how many there are across the board, if there are spaces between them and where they start on the window because you could start these series of smiles outside the window and only see a portion of them on the window.

When you have completed the exercise, commit your changes and push them back to GitHub. Turn in the URL of your repository on canvas.

*Extra credit:* 

main5.py is much more complicated, but it allows the smiley face to track mouse movements. Add a comment to every line describing what is happening. Save those changes.

If you want to further explore Python Arcade, the API and some sample projects are available at [arcade.academy](http://arcade.academy).

---

The grading criteria will be as follows:

* [1 point] Repository contains an appropriate software license
* [1 point] Repository contains a descriptive README.md
* [8] Accomplishes the objective of the exercise

10 points total
