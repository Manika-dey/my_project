'''
Calculate a user's holiday cost including the plane cost, 
hotel cost and car rental cost

'''


#Get the user input

city_flight = input('\nManchester\nLondon\nEdinburgh\nPlease enter which city you will be flying to from the above options: ').lower()

num_nights = int(input('How many nights you will be staying at a hotel: '))

rental_days = int(input('For how many days that you will be hiring a car: '))


def hotel_cost(num_nights):
    price_per_night = 130
    return num_nights * price_per_night # return the total cost for hotel stay

def plane_cost(city_flight):
    
    if city_flight == 'Manchester'.lower():
        return 250    #return the flight ticket price for the city 'Manchester'
    
    elif city_flight == 'London'.lower(): 
        return 300    #return the flight ticket price for the city 'London'
    
    elif city_flight == 'Edinburgh'.lower():
        return 280   #return the flight ticket price for the city 'Edinburugh'
    else: 
        print("you have enterted wrong city name")

def car_rental(rental_days):
    per_day_cost = 100
    return rental_days * per_day_cost   #return total car rental cost for the holiday

def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    flight_fare = plane_cost(city_flight)
    car_rental_cost = car_rental(rental_days)
    total_cost = total_hotel_cost + flight_fare + car_rental_cost
    return total_cost   #return the total holiday cost

#display the total holiday cost
print("Your total holiday cost is:", holiday_cost(num_nights, city_flight, rental_days), "GBP")
    
