# Airport Data Analysis

### Dependencies/Imports:

- `csv`: Used to aid in the manipulation of CSV and TSV files.

## Important Note:
Due to the file size of`CompleteData.csv`, uploading it to GitHub, which has a file size restriction, is impossible. With
this information in mind, please drop a copy of `CompleteData.csv` into the same directory as `main.py`. Failure to do
so will render the script inoperable.

## Purpose:

The purpose of this program is to analyze airport data to determine the most popular departing and arriving cities based
on the number of flights. It retrieves data from two CSV files, 'Stations.csv' and 'CompleteData.csv', and outputs the
top N popular departing and arriving cities along with the number of departing and arriving flights, respectively.

## Input:

- User input: The program prompts the user to enter a positive integer representing the number of popular cities they
  would like to receive information for.

## Expected Output:

- The program generates two TSV (Tab-Separated Values) files:
    1. `popular_departing_cities.tsv`: Contains information about the top N popular departing cities, including the city
       name, state, and the number of departing flights.
    2. `popular_arriving_cities.tsv`: Contains information about the top N popular arriving cities, including the city
       name, state, and the number of arriving flights.

## Execution:

The program is executed in a sequential manner. Upon running the script, the user is prompted to enter the number of
popular cities they wish to receive information for. Then, the program retrieves airport and flight data, processes the
data to determine popular cities, and writes the results to TSV files.

## Improvements:

- Error Handling: Enhance error handling to provide more informative error messages to the user in case of file reading
  or data processing errors.
- Efficiency: Optimize data processing algorithms for better performance, especially for handling large datasets.
