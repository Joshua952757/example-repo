def hotel_cost(num_nights):
    """
    Calculates the total cost of a hotel stay.
    
    Parameters:
    num_nights (int): The number of nights staying at the hotel.
    
    Returns:
    int: The total cost for the stay ($100 per night).
    """
    return num_nights * 100  


def plane_cost(city_flight):
    """
    Returns the flight cost based on destination.
    
    Parameters:
    city_flight (str): The city to which the flight is booked.
    
    Returns:
    int: The cost of the flight. If the city is not listed, a default price of $400 is used.
    """
    prices = {"New York": 500, "Paris": 700, "Tokyo": 900}
    return prices.get(city_flight, 400)  


def car_rental(rental_days):
    """
    Calculates the total cost for car rental.
    
    Parameters:
    rental_days (int): Number of days the car is rented.
    
    Returns:
    int: The total cost for car rental ($50 per day).
    """
    return rental_days * 50  


def holiday_cost(num_nights, city_flight, rental_days):
    """
    Calculates the total holiday cost including hotel, flight, and car rental.
    
    Parameters:
    num_nights (int): Number of nights at the hotel.
    city_flight (str): The city for the flight.
    rental_days (int): Number of days for car rental.
    
    Returns int The total holiday cost.
    """
    hotel = hotel_cost(num_nights)
    flight = plane_cost(city_flight)
    car = car_rental(rental_days)
    total = hotel + flight + car
    
    return hotel, flight, car, total


# User input
city = input("Enter destination (New York, Paris, Tokyo): ")
nights = int(input("Enter number of nights: "))
days = int(input("Enter car rental days: "))

hotel, flight, car, total = holiday_cost(nights, city, days)

# Output with cost breakdown
print("\nHoliday Cost Breakdown:")
print(f"Destination: {city}")
print(f"Hotel ({nights} nights): ${hotel}")
print(f"Flight to {city}: ${flight}")
print(f"Car Rental ({days} days): ${car}")
print(f"Total Holiday Cost: ${total}\n")