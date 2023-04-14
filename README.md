# README.md

## Author: Aaron Stone

## Repository Overview

This repository contains a program to study a Pascal's triangle, specifically the center "column" (also known as the central binomial coefficients). For example, the first 15 rows of Pascal's triangle are as follows:

<pre>
                                              1
                                           1     1
                                        1     2     1
                                     1     3     3     1
                                  1     4     6     4     1
                               1     5    10    10     5     1
                            1     6    15    20    15     6     1
                         1     7    21    35    35    21     7     1
                      1     8    28    56    70    56    28     8     1
                   1     9    36    84   126   126    84    36     9     1
                1    10    45   120   210   252   210   120    45    10     1
             1    11    55   165   330   462   462   330   165    55    11     1
          1    12    66   220   495   792   924   792   495   220    66    12     1
       1    13    78   286   715  1287  1716  1716  1287   715   286    78    13     1
    1    14    91   364  1001  2002  3003  3432  3003  2002  1001   364    91    14     1
</pre>

So, the center column of this triangle is:
<pre>
[1, 2, 6, 20, 70, 252, 924, 3432]
</pre>

# From this sequence, I have defined a new sequence as follows:

## 1. Take the digital root of each element:
<pre>
[1, 2, 6, 2, 7, 9, 6, 3]
</pre>
## 2. Identify all 3's, 6's, and 9's in the sequence, and partition the sequence using these elements as the "cutting points":
<pre>
[1, 2], [6], [2, 7], [9], [6], [3]
</pre>
## 3. Sum the elements in each partition:
<pre>
[3], [6], [9], [9], [6], [3]
</pre>
## 4. Take the digital root of each sum, yielding the final sequence (this section of the sequence remains unchanged):
<pre>
[3, 6, 9, 9, 6, 3]
</pre>

# Observations / Findings

## After testing my initial, hand-written observations with thousands of additional, programmatically generated examples, the results seem to indicate that this sequence only yields 3's, 6's and 9's. Additionally, as the sequence increases in length, it seems to converge to repeating 9's. Further testing is required to confirm this, and the reason for this behavior is not entirely clear.

# Files

## generate.py

This file provides a terminal-based user interface for generating and displaying Pascal's triangles.

## pascal.py

This file provides functions for generating and displaying Pascal's triangles. It includes:

- A function to generate a Pascal's triangle of a given size.
- A function to neatly print Pascal's triangles to the terminal.

## study.py

This file contains the necessary functionality to study the sequence I have defined above.

# Usage Instructions

To use the program to generate Pascal's triangles, simply run the `generate.py` file with Python:

<pre>
python main.py
</pre>

This will launch a user interface that allows you to generate Pascal's triangles. You will be prompted to enter the number of rows for the triangle, and the program will then generate and display the Pascal's triangle with the specified number of rows. After viewing the generated triangle, you can choose to generate a new triangle or exit the program by entering 'Y' (yes) or 'N' (no) when prompted.

To use the program to study the sequence I have defined above, simply run the `study.py` file with Python:

<pre>
python study.py
</pre>

This will generate and display the sequence for the first `ROWS_TO_STUDY` rows of Pascal's triangle. To adjust the number of rows you wish to study, simply modify this variable to your desired value. The default value is `100`.