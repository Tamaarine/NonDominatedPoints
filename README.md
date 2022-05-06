# CSE 555 Final Project ![Picture](https://img.shields.io/github/repo-size/Tamaarine/NonDominatedPoints) ![Picture](https://img.shields.io/github/contributors/Tamaarine/NonDominatedPoints)

This project is the implementation of the gift-wrapping (Jarvis march) algorithm in order to compute the non-dominated points
of an input point set in the 2D plane.

## Description

This project allows input of points by mouse, read from a text file, and randomly generate points for you to run the algorithm in.
When you start up the program ideally by running `python gwnondominated.py` or `python3 gwnondominated.py` you will be prompted to
enter in three of the options, type in
* `mouse`: if you wish to enter points by mouse.
* `file`: if you wish to read points by text.
* `random`: if you wish to randomly generate points. Follow the rest of the prompted instructions to generate points.

After you finished entering points by either three of the options, press the `space bar` to begin the animation. Then press `z` to
step through the algorithm. Blue points indicates the non-dominated points that is found. 

### Dependencies

* matplotlib
* numpy