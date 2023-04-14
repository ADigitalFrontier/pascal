# README.md

## Author: Aaron Stone

## Repository Overview

This repository contains a program to study the digital roots of the center "column" of Pascal's Triangle, along with code for generating and displaying Pascal's triangles. The central elements exhibit interesting properties with their digital roots, and this project aims to explore these properties and validate hand-written observations with thousands of additional programmatically-generated examples.

## Files

### main.py

This file is the entry point of the program. It generates and displays Pascal's triangles using the functions provided in `pascal.py`.

### pascal.py

This file provides functions for generating and displaying Pascal's triangles. It includes:

- A function to generate a Pascal's triangle of a given size.
- A function to display a Pascal's triangle.

### study.py

This file contains the program to study the digital roots of the center "column" of Pascal's triangle, i.e., [1, 2, 6, 20, 70, 252, 924, etc.]. The observations made include:

1. The digital root of each center element is either 3, 6, or 9.
2. When the digital root of an element is not 9, adjacent elements to the left and right are considered. These adjacent elements are summed, excluding any with digital roots of 3, 6, or 9, until a 3, 6, or 9 is encountered on either side. The sum of these non-369 elements, when their digital root is taken, seems to always yields either 3, 6, or 9.
3. The sequence of digital roots seems to converge to repeating 9s as it increases in length.

The program verifies the hand-written observations with thousands of additional, programmatically generated examples, which seem to indicate that this property likely holds for any number of rows.

## Usage Instructions

To use the program, simply run the `main.py` file with Python:

<pre>
python main.py
</pre>

This will launch a user interface that allows you to generate Pascal's triangles. You will be prompted to enter the number of rows for the triangle, and the program will then generate and display the Pascal's triangle with the specified number of rows. After viewing the generated triangle, you can choose to generate a new triangle or exit the program by entering 'Y' (yes) or 'N' (no) when prompted.
