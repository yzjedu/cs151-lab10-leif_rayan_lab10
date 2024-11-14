movie_list_raw = []
movie_list = []

def read_file(filename):
    global movie_list_raw
    file_data = open(filename, 'r')
    for line in file_data:
        movie_list_raw.append(line)
    file_data.close()

def create_box():
    global movie_list_raw
    global movie_list
    box_count = 0
    for section in movie_list_raw:
        section = section.split(',')
        gross_profit = int(section[3]) + int(section[4]) - int(section[2])
        movie_list.append([section[0],section[1],section[2],section[3],section[4],str(gross_profit)])

def main():
    global movie_list
    file_name = input('What is the name of the file you would like to read?\nExpress the file name WITH the suffix (.txt, .csv): ')
    read_file(f'{file_name}')
    create_box()
    for list in movie_list:
        print(f'Release date: {list[0]}. Film name: {list[1]}. Film budget: {list[2]}. Domestic gross: {list[3]}. International gross: {list[4]}. Total profit: {list[5]}')

main()

