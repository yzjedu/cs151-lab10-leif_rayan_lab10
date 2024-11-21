movie_list_raw = []
movie_list = []
row_count = 0

# Purpose:  this function reads the file
# Parameters: filename
# Return: the raw, unfiltered lines in the file
def read_file(filename):
    #imports external list for transferability
    global movie_list_raw
    #opens file and appends each line to the raw movie list
    file_data = open(filename, 'r')
    for line in file_data:
        movie_list_raw.append(line)
    file_data.close()

# Purpose:  creates a functional box by separating each statistic in a line
# Parameters: none
# Return: filtered and boxed movie list
def create_box():
    #imports external list and row count for later use
    global movie_list_raw
    global movie_list
    global row_count
    #for each line in the raw list, each section is broken down into each individual data piece and organized into the filtered movie list
    for section in movie_list_raw:
        # adds 1 to row count for each row
        row_count += 1
        section = section.split(',')
        gross_profit = int(section[3]) + int(section[4]) - int(section[2])
        movie_list.append([section[0],section[1],section[2],section[3],section[4],str(gross_profit)])
    #for each item in a given row, it prints the appropriate figure for each statistic
    for list in movie_list:
        print(f'Release date: {list[0]}. Film name: {list[1]}. Film budget: {list[2]}. Domestic gross: {list[3]}. International gross: {list[4]}. Total profit: {list[5]}')

# Purpose:  compares two films' profit via input from user
# Parameters: none
# Return: which movie grossed more profits
def compare():
    #imports the filtered list, row count, and indexes 1 and 2 to be used in print statement
    global movie_list
    global row_count
    global index1
    global index2
    # defines a loop end variable
    passthru = False
    # the user is asked to input a number (1-600) of a movie they want to compare. loop exists for error checking
    while not passthru:
        grab_index1 = input(f"\nWhat is the sequence number of a movie you'd like to compare?\nNOTE! There are {row_count} movies to select: ")
        if grab_index1.isdigit():
            grab_index1 = int(grab_index1) - 1
            if grab_index1 < 0 or grab_index1 >= row_count:
                print(f"This number is out of range. Remember, there are {row_count} movies to select.")
            else:
                passthru = True
        else:
            print('Invalid input. Please enter your answer as a digit')
    # the user is asked to input a DIFFERENT number of a movie they want to compare. loop once again exists for error checking
    while passthru:
        grab_index2 = input(f"\nWhat is the sequence number of a DIFFERENT movie you'd like to compare?\nNOTE! You cannot select {grab_index1 + 1} again.\nThere are {row_count - 1} movies to select: ")
        if grab_index2.isdigit():
            grab_index2 = int(grab_index2) - 1
            if grab_index2 == grab_index1:
                print('You cannot select the same movie number again. Select a new number')
            elif grab_index2 < 0 or grab_index2 >= row_count:
                print(f"This number is out of range. Remember, there are {row_count - 1} movies to select excluding #{grab_index1 + 1}.")
            else:
                passthru = False
        else:
            print('Invalid input. Please enter your answer as a digit')
    # each index is set equal to the movie corresponding to the number selected by the user
    index1 = movie_list[grab_index1]
    index2 = movie_list[grab_index2]
    # dependent on the difference in gross profits, the program will print 1 of 3 statements to the user, each the same apart from the stated profit relationship
    if index1[5] == index2[5]:
        print(f"Movie #{grab_index1 + 1} profited the same amount as movie #{grab_index2 + 1}.\n({index1[5]} = {index2[5]})\nMovie 1: Release date: {index1[0]}. Film name: {index1[1]}. Film budget: {index1[2]}. Domestic gross: {index1[3]}. International gross: {index1[4]}. Total profit: {index1[5]} \nMovie 2: Release date: {index2[0]}. Film name: {index2[1]}. Film budget: {index2[2]}. Domestic gross: {index2[3]}. International gross: {index2[4]}. Total profit: {index2[5]} ")
    elif index1[5] < index2[5]:
        print(f"Movie #{grab_index1 + 1} profited less than movie #{grab_index2 + 1}.\n({index1[5]} < {index2[5]})\nMovie 1: Release date: {index1[0]}. Film name: {index1[1]}. Film budget: {index1[2]}. Domestic gross: {index1[3]}. International gross: {index1[4]}. Total profit: {index1[5]} \nMovie 2: Release date: {index2[0]}. Film name: {index2[1]}. Film budget: {index2[2]}. Domestic gross: {index2[3]}. International gross: {index2[4]}. Total profit: {index2[5]} ")
    elif index1[5] > index2[5]:
        print(f"Movie #{grab_index1 + 1} profited more than movie #{grab_index2 + 1}.\n({index1[5]} > {index2[5]})\nMovie 1: Release date: {index1[0]}. Film name: {index1[1]}. Film budget: {index1[2]}. Domestic gross: {index1[3]}. International gross: {index1[4]}. Total profit: {index1[5]} \nMovie 2: Release date: {index2[0]}. Film name: {index2[1]}. Film budget: {index2[2]}. Domestic gross: {index2[3]}. International gross: {index2[4]}. Total profit: {index2[5]} ")

# Purpose:  this function runs the entire code
# Parameters: none
# Return: movie box and comparisons
def main():
    #imports movie list
    global movie_list
    # loop end condition is set
    passthru2 = False
    # the user is asked to input the file name. the loop exists to ensure they correct a valid file name
    while not passthru2:
        file_name = input('What is the name of the file you would like to read?\nExpress the file name WITH the suffix (.txt, .csv): ')
        if file_name != 'movies.csv':
            print('Could not find this file. Please try again\n')
        else:
            passthru2 = True
    # runs the function read_file with the given file name
    read_file(f'{file_name}')
    # runs the create_box function
    create_box()
    # the function compare is run, and the user is prompted whether they would like to compare two different movies. loop accounts for error checking
    while passthru2:
        compare()
        new_compare_query = input('\nWould you like to compare two movies again?\nExpress your answer as Y or N: ')
        if new_compare_query.upper() == 'Y':
            print('Reseting...\n')
        elif new_compare_query.upper() == 'N':
            print('Thank you for using our program!')
            passthru2 = False
        else:
            print('Invalid input. Please enter your answer as Y or N')

# runs main
main()

