"""
Name: Jalen Vaughn
Date: 4/21/24
File: main.py
Dependencies/Imports:
    - csv
        Used to manipulate CSV and TSV files.
"""
import csv


def retrieve_airport_data():
    """
    Reads CSV data from 'Stations.csv' and formats the data containing
    airport codes and their respective city, and state.
    :return: Dictionary containing airport data
    """
    # File path to CSV
    csv_file = "Stations.csv"
    
    # Open the CSV file in read mode
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        
        # Initialize an empty dict to store airport data
        data = {}
        for row in csv_reader:
            # Extract required elements from the row
            airport_code = row['AIRPORT']
            location = row['DISPLAY_AIRPORT_CITY_NAME_FULL']
            city = row['DISPLAY_AIRPORT_CITY_NAME_FULL'].split(",")[0]
            state = row['AIRPORT_STATE_NAME']
            
            # Store the data
            data[airport_code] = {"LOCATION": location, "CITY": city, "STATE": state}
        
        return data


def retrieve_flight_data():
    """
    Reads CSV data from 'CompleteData.csv' and retrieves departing and arriving flights.
    :return: Tuple containing lists of departing and arriving flights
    """
    # File path to CSV
    csv_file = "CompleteData.csv"
    
    # Open the CSV file in read mode
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        
        # Initialize empty dicts to store departing and arriving flights
        departing, arriving = {}, {}
        for row in csv_reader:
            departing[row['ORIGIN']] = departing.get(row['ORIGIN'], 0) + 1
            arriving[row['DEST']] = arriving.get(row['DEST'], 0) + 1
        
        # Sort departing and arriving flights by count in descending order
        departing = sorted(departing.items(), key=lambda x: x[1], reverse=True)
        arriving = sorted(arriving.items(), key=lambda x: x[1], reverse=True)
    
    return departing, arriving


def get_input() -> int:
    """
    Prompts the user to enter a positive integer.
    :return: Positive integer entered by the user
    """
    while True:
        # Prompt user for input
        user_input: str = input("Enter an endpoint (positive integer): ")
        
        try:
            # Error handle conversion to integer
            validated_input: int = int(user_input)
            
            # Check if input is negative
            if validated_input < 1:
                raise ValueError("Please enter a non-zero positive integer.")
            
            return validated_input
        # Catch exceptions
        except ValueError:
            print(f"Invalid number: '{user_input}'. Input must be an integer.")
            continue


def write_cities_data_to_tsv(file_path, cities_data, airport_data, header):
    """
    Writes cities data to a TSV file.
    :param file_path: Path to the TSV file.
    :param cities_data: List of tuples containing city data.
    :param airport_data: Dictionary containing airport data.
    :param header: Header for the TSV file.
    """
    # Create/Open TSV file in write mode
    with open(file_path, 'w', newline='') as tsv_file:
        # Create CSV writer object
        writer = csv.writer(tsv_file, delimiter='\t')
        
        # Add header to first row
        writer.writerow(header)
        
        # Iterate through each city
        for airport, count in cities_data:
            # Write row with city, state, and number of flights data
            writer.writerow([
                airport_data.get(airport, {}).get('CITY', ''),
                airport_data.get(airport, {}).get('STATE', ''),
                count
            ])


def main():
    """
    Main function to execute the program.
    """
    
    # Get user input for the number of popular cities
    print("How many popular cities would you like to receive info for?")
    num_cities = get_input()
    
    try:
        # Load airport data
        airport_data = retrieve_airport_data()
        
        # Load flight data
        departing_cities, arriving_cities = retrieve_flight_data()
        
        # Extract the specified number of popular departing/arriving cities
        popular_departing_cities = departing_cities[:num_cities]
        popular_arriving_cities = arriving_cities[:num_cities]
        
        # Write departing cities data to a TSV file
        write_cities_data_to_tsv('popular_departing_cities.tsv',
                                 popular_departing_cities,
                                 airport_data,
                                 ['City', 'State', 'Number of Departing Flights'])
        
        # Write arriving cities data to a TSV file
        write_cities_data_to_tsv('popular_arriving_cities.tsv',
                                 popular_arriving_cities,
                                 airport_data,
                                 ['City', 'State', 'Number of Arriving Flights'])
    except OSError as e:
        print(f"There was an error reading a CSV file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


main()
