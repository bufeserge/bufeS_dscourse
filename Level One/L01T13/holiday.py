# L01T13 : Programming With User-Defined Functions


# INSTRUCTIONS: My task is to calc a users total holiday cost, including:
#                       -Plane Cost     -Hotel Cost     -Car Rental cost
#               Get user inputs city_flight = where they'll be flying too
#                               num_nights = num nights at hotel
#                               rental_days = num days hiring car
#               Create the following for functions:
#                       -   hotel_cost() : take num_nights as argument and return a total cost based on hotel price(you choose daily)
#                       -   plane_cost() : take city_flight as argument and return cost for flight (use if else)
#                       -   car_rental() : take rental_days as argument and return total cost of car (you choose daily)
#                       -   holiday_cost() : take three arguments and call on last three functions to calc the the total cost for the holiday
#               Print this in a legible way


# ill begin by setting fixed costs for daily hotel price and daily car rental price
# ill create some print to help the user understand their choices they have, as well as an input for three variables city_flight, num_nights, rental_days
# ill then define functions:
#   -   for plane_cost() ill have to run through pre-defined choices and pre-defined costs in an if/elif/else statement, with the argument being the inputted city
#   -   for hotel_cost() ill mulitply inputted number (argument) of nights by the cost per night to stay at the hotel
#   -   for car_rental() ill mulitply inputted number (argument) of days by the daily rental cost of the car
#   -   for holiday_cost() ill have to pass all three inputs (the city, the number of nights at the hotel and then the number of days renting car), then utilise the three
#           previous functions wihtin this function, passing the inputs into these as arguments respectfully as to calculate a total cost of the holiday
#  ill then use these functions and pass in the respective variables in order to calculate total holiday cost
# ill then print this information in a formatted sense, using string manipulation in order to correctly display money values in a R0.00 format


# FIXED COSTS
hotel_price_per_night = 900  # Set the nightly hotel rate
car_rental_per_day = 450  # Set the daily car rental rate

# USER INPUT TIME BABBBYYYYYYYY
print("Welcome to the Holiday Cost Calculator!\n")  # Display welcome message
print(
    "Available destinations: Hoedspruit, Springbok, Welkom, Other"
)  # Show valid city options


city_flight = input(
    "Enter the city you are flying to: "
).strip()  # Ask for destination and strip extra spaces
num_nights = int(
    input("Enter number of hotel nights: ")
)  # Ask for hotel nights and convert to int
rental_days = int(
    input("Enter number of car rental days: ")
)  # Ask for car rental days and convert to int


# PLANE COST FUNCTION
def plane_cost(city_flight):
    if city_flight.lower() == "hoedspruit":  # Check if city is Hoedspruit
        return 1500  # Return R1500 for Cape Town flight
    elif city_flight.lower() == "springbok":  # Check if city is springbok
        return 1000  # Return R1000 for Johannesburg flight
    elif city_flight.lower() == "welkom":  # Check if city is welkom
        return 800  # Return R800 for Durban flight
    else:
        return 1200  # Return a default price for any other city, or if the input is not one of these three


# HOTEL COST FUNCTION - num_nights * daily hotel cost
def hotel_cost(num_nights):
    return (
        num_nights * hotel_price_per_night
    )  # Multiply number of nights by the nightly rate


# CAR RENTAL COST FUNCTION - rental days * daily rate
def car_rental(rental_days):
    return (
        rental_days * car_rental_per_day
    )  # Multiply number of rental days by the daily rate


# HOLIDAY COST FUNCTION - Receives all three inputs as arguments and utilises PLANE COST, HOTEL COST & CAR RENTAL functions and then passes inputted variables into these functions as arguments
def holiday_cost(num_nights, city_flight, rental_days):
    # Add hotel, flight, and car rental costs together
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total  # Return the total holiday cost


# CREATE VARIABLES TO STORE AND UTILISE FUNCTIONS TO CALC
hotel_total = hotel_cost(num_nights)  # Get total hotel cost
flight_total = plane_cost(city_flight)  # Get flight cost
car_total = car_rental(rental_days)  # Get car rental cost
holiday_total = holiday_cost(
    num_nights, city_flight, rental_days
)  # Calculate total holiday cost

# OUTPUT PRINT OF INFORMATION
print("\n----- Holiday Summary -----")  # Header for summary section
print(f"Destination: {city_flight}")  # Print the city
print(
    f"Hotel: R {hotel_total:.2f} for {num_nights} night(s)"
)  # Print formatted hotel cost
print(
    f"Flight: R {flight_total:.2f}"
)  # Print formatted flight cost, as a float to two decimal points
print(
    f"Car Rental: R {car_total:.2f} for {rental_days} day(s)"
)  # Print formatted car rental cost
print(
    f"TOTAL HOLIDAY COST: R {holiday_total:.2f}"
)  # Print formatted total holiday cost
