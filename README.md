[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/q01fVkoE)
<h1>CS151 Lab 10</h1>

 <h3>🔴 DO NOT Start to code before the instructor Approve your algorithm, and test cases🔴</h3>

- **Grade: EMRN**
- **Due: Before Next Lab**

<h3>Table of contents</h3>

  * [`Problem`](#problem)
  * [`Purpose`](#purpose)
  * [`Details`](#details)
    * [Programming Hint](#programming-hint)
    * [Error Checking](#error-checking)
    * [Output](#output)
  * [`Testing`](#testing)
  * [`Steps`](#steps)
  * [`What to Submit in GitHub`](#what-to-submit-in-github)


## `Problem`

In this lab assignment you will analyze data on movies, their budgets, and their profits

## `Purpose`

In this lab you will practice:

1. working with files (reading, writing)
2. working with functions
3. working with tables (aka lists of lists)

## `Details`

- Provided in this repo is a file named `movies.csv` which contains information regarding approximately 600 movies. 
  - Format: `9-Dec-22,Avatar: The Way of Water,460000000,684075767,2319591720`
- Each line contains `comma-separated values (CSV)` about each movie in the following order:
  * Release Date
  * Movie Title
  * Movie Budget
  * Domestic Gross (e.g. money brought in from theaters)
  * Worldwide Gross (e.g. money brought in from theaters)


Given the name of a file of this format and the name of an output file, write a program which
- Writes all movie information from the input file to the output file, but also adds a new column with the movie's profit 
  - Profit is computed as box office worldwide gross minus the budget. 
- Additionally, the program should determine which movie had either the highest profit or the lowest profit 
  - Output to the console all information related to that movie. 
  - 🟢**You choose which one you'd like to do**🟢

### Programming Hint

The `split()` string function can split on something other than whitespace. 
- You just pass the thing you want to split on as an argument when you call it.

### Error Checking
Unfortunately, you don’t really trust your user to follow the directions in your program.
- Protect your program from bad user input.  
- You must continue asking for a file name until you are given one that exists for the input file. 
- You do NOT need to check the name of the output file.
  - Python creates your output file for you if it doesn't exist.

### Output
The information you output to the `file should be comma delimited` (i.e. have a comma separating each value). 
- There should be `one movie per line`. 
- Remember that you can use `string concatenation with "+" to combine two strings` together before writing.

## `Testing`

You can use Excel to determine what your answers should be. 
- Open the movies.csv file in Excel, and save it as an Excel file somewhere other than your repository. 
- You should create a new column that is profit. 
  - Then calculate what the highest/lowest revenue should be. 
- These are your value to test that your program correctly finds.

## `Steps`

We are going to do a new type of iterative development this lab:

1. Make sure you understand the problem
2. Use `algorithm.md` and plan how you will solve ONE of the tasks you need to do with this data 
   - E.g. writing the data plus profit to a new file, OR finding the highest/lowest revenue movie. 
3. Code your `main.py` file while only writing the first 3 functions: 
   - a function to read in the filename from the user, 
   - a function to read the data from the file into a list of lists, and 
   - main to call these functions. 🟢**take turns driving**🟢
4. Test that your code works correctly by adding in output in main.
5. Write your code to solve this one task following your algorithm. 
   - Test it. **whoever didn't drive on the algorithm, should drive on the code**
6. Now write your algorithm for the remaining task.
   - 🟢**whoever didn't write the last algorithm, writes this one**🟢
7. Write your code for this remaining task. Test it. 
   - 🟢**whoever didn't write the code in step 5, writes this code**🟢

You should be commenting your code as you go, but if you haven't already done so, make sure you put in all of the comments you need:
1. Comments within each function
2. Comments at the start of each function (purpose, paramters, return value)
3. Intro comments


## `What to Submit in GitHub`

1. Completed `main.py` file  
2. `algorithm.md`
3. Encrypt your files using the `keys` and `process_reflection.py`
   1. `RD1.md` -> Reflection for Drive 1
   2. `RD2.md` -> Reflection for Drive 2
   3. If you use a different key, it is considered unsubmitted

**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get?
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working with your partner?

**Make sure the file in your PyCharm and Github is the same (i.e. Commit and Push)**