movie_list_raw = []
movie_list = []
row_count = 0

def read_file(filename):
    global movie_list_raw
    file_data = open(filename, 'r')
    for line in file_data:
        movie_list_raw.append(line)
    file_data.close()

def create_box():
    global movie_list_raw
    global movie_list
    global row_count
    for section in movie_list_raw:
        row_count += 1
        section = section.split(',')
        gross_profit = int(section[3]) + int(section[4]) - int(section[2])
        movie_list.append([section[0],section[1],section[2],section[3],section[4],str(gross_profit)])
    for list in movie_list:
        print(f'Release date: {list[0]}. Film name: {list[1]}. Film budget: {list[2]}. Domestic gross: {list[3]}. International gross: {list[4]}. Total profit: {list[5]}')

def compare():
    global movie_list
    global row_count
    global index1
    global index2
    passthru = False
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
    index1 = movie_list[grab_index1]
    index2 = movie_list[grab_index2]
    if index1[5] == index2[5]:
        print(f"Movie #{grab_index1 + 1} profited the same amount as movie #{grab_index2 + 1}.\n({index1[5]} = {index2[5]})\nMovie 1: Release date: {index1[0]}. Film name: {index1[1]}. Film budget: {index1[2]}. Domestic gross: {index1[3]}. International gross: {index1[4]}. Total profit: {index1[5]} \nMovie 2: Release date: {index2[0]}. Film name: {index2[1]}. Film budget: {index2[2]}. Domestic gross: {index2[3]}. International gross: {index2[4]}. Total profit: {index2[5]} ")
    elif index1[5] < index2[5]:
        print(f"Movie #{grab_index1 + 1} profited less than movie #{grab_index2 + 1}.\n({index1[5]} < {index2[5]})\nMovie 1: Release date: {index1[0]}. Film name: {index1[1]}. Film budget: {index1[2]}. Domestic gross: {index1[3]}. International gross: {index1[4]}. Total profit: {index1[5]} \nMovie 2: Release date: {index2[0]}. Film name: {index2[1]}. Film budget: {index2[2]}. Domestic gross: {index2[3]}. International gross: {index2[4]}. Total profit: {index2[5]} ")
    elif index1[5] > index2[5]:
        print(f"Movie #{grab_index1 + 1} profited more than movie #{grab_index2 + 1}.\n({index1[5]} > {index2[5]})\nMovie 1: Release date: {index1[0]}. Film name: {index1[1]}. Film budget: {index1[2]}. Domestic gross: {index1[3]}. International gross: {index1[4]}. Total profit: {index1[5]} \nMovie 2: Release date: {index2[0]}. Film name: {index2[1]}. Film budget: {index2[2]}. Domestic gross: {index2[3]}. International gross: {index2[4]}. Total profit: {index2[5]} ")



def main():
    global movie_list
    passthru2 = False
    while not passthru2:
        file_name = input('What is the name of the file you would like to read?\nExpress the file name WITH the suffix (.txt, .csv): ')
        if file_name != 'movies.csv':
            print('Could not find this file. Please try again\n')
        else:
            passthru2 = True
    read_file(f'{file_name}')
    create_box()
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

main()

