# Algorithm for the Movie Data Analyzer Program

---

### Algorithm for `read_filename`
- **Purpose**: Prompt the user for a valid filename and ensure the file exists.
- **Name**: `read_filename`
- **Parameters**: None
- **Return**: The valid filename entered by the user as a string.
- **Algorithm**:
  1. Prompt the user to enter the name of the input file.
  2. While the file does not exist:
     1. Display an error message indicating the file does not exist.
     2. Prompt the user to enter the name of the input file again.
  3. Return the valid filename.

---

### Algorithm for `read_data`
- **Purpose**: Read data from the input file and convert it into a structured format.
- **Name**: `read_data`
- **Parameters**: 
  - `filename` (string): The name of the file to read.
- **Return**: A list of lists where each sublist contains movie data from one row.
- **Algorithm**:
  1. Open the file in read mode.
  2. For each line in the file:
     1. Strip any leading or trailing whitespace.
     2. Split the line into columns by commas.
     3. Convert numeric columns (starting from the third column) to integers.
     4. Append the processed row to the `table`.
  3. Return the `table`.

---

### Algorithm for `write_with_profit`
- **Purpose**: Write movie data to an output file with an additional column for profit.
- **Name**: `write_with_profit`
- **Parameters**:
  - `table` (list of lists): The movie data.
  - `output_file` (string): The name of the file to write to.
- **Return**: None
- **Algorithm**:
  1. Open the file in write mode.
  2. For each row in the `table`:
     1. Calculate the profit as `Worldwide Gross - Budget`.
     2. Append the profit to the row.
     3. Convert the row into a comma-separated string and write it to the file.
  3. Close the file.

---

### Algorithm for `find_highest_profit`
- **Purpose**: Find the movie with the highest profit in the dataset.
- **Name**: `find_highest_profit`
- **Parameters**:
  - `table` (list of lists): The movie data.
- **Return**: The row (list) of the movie with the highest profit.
- **Algorithm**:
  1. Initialize `highest_movie_row` as the first row in the `table`.
  2. Calculate the profit for `highest_movie_row` as `Worldwide Gross - Budget`.
  3. For each subsequent row in the `table`:
     1. Calculate the profit for the current row.
     2. If the current row's profit is greater than `highest_profit`:
        1. Update `highest_movie_row` to the current row.
        1. Update `highest_profit` to the current row's profit.
  4. Return `highest_movie_row`.

---

### Algorithm for `find_lowest_profit`
- **Purpose**: Find the movie with the lowest profit in the dataset.
- **Name**: `find_lowest_profit`
- **Parameters**:
  - `table` (list of lists): The movie data.
- **Return**: The row (list) of the movie with the lowest profit.
- **Algorithm**:
  1. Initialize `lowest_movie_row` as the first row in the `table`.
  2. Calculate the profit for `lowest_movie_row` as `Worldwide Gross - Budget`.
  3. For each subsequent row in the `table`:
     1. Calculate the profit for the current row.
     2. If the current row's profit is less than `lowest_profit`:
        1. Update `lowest_movie_row` to the current row.
        1. Update `lowest_profit` to the current row's profit.
  4. Return `lowest_movie_row`.

---

### Algorithm for `display_movie_details`
- **Purpose**: Display details of a movie, including its profit.
- **Name**: `display_movie_details`
- **Parameters**:
  - `movie` (list): The movie data.
  - `label` (string): Specifies whether the movie has the "highest" or "lowest" profit.
- **Return**: None
- **Algorithm**:
  1. Print a heading that includes the `label` (e.g., "highest profit" or "lowest profit").
  2. Display the following details of the movie:
     - Release Date
     - Movie Title
     - Budget
     - Domestic Gross
     - Worldwide Gross
     - Profit (calculated as `Worldwide Gross - Budget`).

---

### Algorithm for `main`
- **Purpose**: Drive the program and provide the user with options to analyze movie data.
- **Name**: `main`
- **Parameters**: None
- **Return**: None
- **Algorithm**:
  1. Print a welcome message.
  2. Call `read_filename()` to get the name of the input file.
  3. Call `read_data()` with the input filename to retrieve the movie data.
  4. Prompt the user to enter the name of the output file.
  5. Call `write_with_profit()` to write the movie data along with the profit column to the output file.
  6. Print a message confirming the data has been written to the output file.
  7. Display the menu options:
     - 1 Find the movie with the highest profit.
     - 2 Find the movie with the lowest profit.
  8. Prompt the user to enter their choice (1 or 2).
  9. While the input is invalid (not 1 or 2):
     1. Display an error message.
     2. Prompt the user to enter a valid choice.
  10. If the user chooses 1:
      1. Call `find_highest_profit()` and pass the movie data.
      1. Call `display_movie_details()` with the highest-profit movie and "highest" as the label.
  11. If the user chooses 2:
      1. Call `find_lowest_profit()` and pass the movie data.
      1. Call `display_movie_details()` with the lowest-profit movie and "lowest" as the label.