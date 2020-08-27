from matrix import Matrix

"""Input number of tests"""
while True:
    try:
        number_of_tests = int(input("Number of tests: "))
        if number_of_tests > 0:
            print (number_of_tests)
        break
    except:
        print("Please, input correct number of tests!")

"""Input number of cities"""
while True:
    try:
        number_of_cities = int(input("Number of cities: "))
        if number_of_cities > 0:
            print (number_of_cities)
        break
    except:
        print("Please, input correct number of cities!")

matrix = Matrix(number_of_cities) #class instance
current_city_number = 0
city_names = [number_of_cities] #list of number of cities

"""Tests"""
for test in range(number_of_tests):
    for i in range(number_of_cities):
        """Input city name and Number of neighbours"""
        while True:
            try:
                name = input("City name: ")
                city_names.append(name)
                p = int(input("Number of neighbours in " + name + ": "))
                if (p >= number_of_cities):
                    raise
                break
            except:
                print ("BAD INPUT!!!\n")
        """Input number of city and cost"""
        for j in range(p):
            while True:
                try:
                    number_cost = input("Number of city and cost: ").split(' ')
                    neighbour_city_number = int(number_cost[0]) - 1
                    transport_cost = int(number_cost[1])
                    if (neighbour_city_number == current_city_number
                            or neighbour_city_number < 0
                            or transport_cost < 1):
                        raise
                    matrix[current_city_number][neighbour_city_number] = transport_cost
                    break
                except:
                    print ("BAD INPUT!\n")
        current_city_number += 1

    matrix.floyd() #method Matrix.floyd

    """Input number of test travels"""
    while True:
        try:
            number_of_test_travels = int(input("Number of test travels: "))
            if number_of_test_travels > 0:
                print (number_of_test_travels)
            break
        except:
            print("Please, input correct number test travels!")
    """Input start and end"""
    for i in range(number_of_test_travels):
        while True:
            cost_btw_cities = input("Input start and end: ").split(' ')
            try:
                start_city = int(city_names.index(cost_btw_cities[0]))  - 1
                end_city = int(city_names.index(cost_btw_cities[1])) - 1
                break
            except:
                print("Input correct name of cities!")

        print("Cost:", matrix[start_city][end_city]) #cost