# Programmers:  [your names here]
# Course:  CS151, [Instructors Name]
# Due Date: [date assignment is due]
# Lab Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Input Files: [description of the format of the input files you need for this program to work]


import os

# Purpose: Read a valid input filename from the user.
# Parameters: None
# Returns: A valid filename as a string.
def read_filename():
    filename = input("Enter the name of the input file: ").strip()
    while not os.path.isfile(filename):
        print("Error: File does not exist. Please try again.")
        filename = input("Enter the name of the input file: ").strip()
    return filename


# Purpose: Read data from the input file and return it as a list of lists.
# Parameters: filename (string)
# Returns: A list of lists where each list contains movie data from a single row.
def read_to_table(filename):
    table = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            for i in range(2, len(row)):
                row[i] = int(row[i])  # Convert numeric columns to integers
            table.append(row)
    return table


# Purpose: Write data to an output file with an additional profit column.
# Parameters: data (list of lists), output_file (string)
# Returns: None
def write_with_profit(table, output_file):
    with open(output_file, 'w') as file:
        for row in table:
            profit = row[4] - row[2]  # Calculate profit (Worldwide Gross - Budget)'
            row.append(profit)
            file.write(','.join(map(str, row)) + '\n')


# Purpose: Find the movie with the highest profit.
# Parameters: data (list of lists)
# Returns: The row (list) of the movie with the highest profit.
def find_highest_profit(table):
    highest_movie_row = table[0]
    highest_profit = highest_movie_row[4] - highest_movie_row[2]

    for row in table[1:]:
        profit = row[4] - row[2]
        if profit > highest_profit:
            highest_movie_row = row
            highest_profit = profit

    return highest_movie_row

# Purpose: Find the movie with the lowest profit.
# Parameters: data (list of lists)
# Returns: The row (list) of the movie with the lowest profit.
def find_lowest_profit(table):
    lowest_movie_row = table[0]
    lowest_profit = lowest_movie_row[4] - lowest_movie_row[2]

    for row in table[1:]:
        profit = row[4] - row[2]
        if profit < lowest_profit:
            lowest_movie_row = row
            lowest_profit = profit

    return lowest_movie_row

# Purpose: Display the details of a movie.
# Parameters: movie (list of values) - The movie data, label (string) - Label to specify highest/lowest profit.
# Returns: None
def display_movie_details(movie, label):
    print(f"\nMovie with the {label} profit:")
    print(f"Release Date: {movie[0]}")
    print(f"Movie Title: {movie[1]}")
    print(f"Budget: {movie[2]}")
    print(f"Domestic Gross: {movie[3]}")
    print(f"Worldwide Gross: {movie[4]}")
    print(f"Profit: {movie[4] - movie[2]}")

# Purpose: Main function to drive the program.
# Parameters: None
# Returns: None
def main():
    print("Welcome to the Movie Data Analyzer!")
    print("-----------------------------------")

    input_file = read_filename()
    movie_table = read_to_table(input_file)

    output_file = input("Enter the name of the output file: ").strip()
    write_with_profit(movie_table, output_file)
    print(f"Data with profit column has been written to '{output_file}'.\n")

    # Display a number-based menu for the user
    print("\t1. Find the movie with the highest profit.\n\t2. Find the movie with the lowest profit.")
    
    # Prompt the user for their choice
    choice = input("Enter your choice (1 or 2): ").strip()

    # Validate the user's input
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice (1 or 2): ").strip()

    # Process the user's choice
    if choice == "1":
        highest_movie = find_highest_profit(movie_table)
        display_movie_details(highest_movie, "highest")
    elif choice == "2":
        lowest_movie = find_lowest_profit(movie_table)
        display_movie_details(lowest_movie, "lowest")

# Run the program
main()