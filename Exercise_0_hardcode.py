#This is a hardcoded version of the exercise.
# I know this would NOT work on a very large scale, but I couldn't quite get the other version
def main():
    header()
    print_info(driver_dict(get_info()))


#Just prints a simple header
def header():
    print("2021 F1 Drivers")
    print("===============")
    print("")
    print("")


#Uses already seperated data to sort drivers info into lists
def get_info():
    driver_info =[]
    info_list = {
        "Max, Verstappen, 33, Red Bull",
        "Lewis, Hamilton, 44, Mercedes",
        "Valtteri, Bottas, 77, Mercedes",
        "Lando, Norris, 4, McLaren",
        "Sergio, Perez, 11, Red Bull",
        "Charles, Leclerc, 16, Ferrari",
        "Carlos, Sainz, 55, Ferrari",
        "Daniel, Ricciardo, 3, McLaren",
        "Pierre, Gasly, 10, AlphaTauri",
        "Fernando, Alonso, 14, Alpine",
        "Esteban, Ocon, 31, Alpine",
        "Sebastian, Vettel, 5, Aston Martin",
        "Lance, Stroll, 18, Aston Martin",
        "Yuki, Sonoda, 22, AlphaTauri",
        "George, Russell, 63, Williams",
        "Nicholas, Latifi, 6, Williams",
        "Kimi, Raikkonen, 7, Alfa Romeo",
        "Antonio, Giovinazzi, 99, Alfa Romeo",
        "Mick, Schumacher, 47, Haas",
        "Nikita, Mazepin, 9, Haas"
    }
    #Loop that iterates through the dict and assigns each driver and their info to an index
    for driver in info_list:
        d_info = driver.split(", ") #Splitting each line based on the commas
        d_info[2] = int(d_info[2])
        driver_info.append(d_info)
    return driver_info

#Turns the lists of info to dicts to sort
def driver_dict(driver_info):
    dict_list = [ ]
    for drivers in driver_info:
        driver_dict = {"first": drivers[0], "last": drivers[1], #Assigning terms to each index to use later
                       "num": drivers[2], "car": drivers[3]} 
        dict_list.append(driver_dict)
    return dict_list

def print_info(dict_list):
    dict_list = sorted(dict_list, key = lambda item: item["last"])
    print("Drivers sorted alphabetically by lastname printed L, F, N, I")
    for driver in dict_list:
        if driver["first"] == "Lewis":
            print(driver["last"], driver["first"], driver["num"], driver["car"], "YEET!!")
        else:
            print(driver["last"], driver["first"], driver["num"], driver["car"])
    print('\n' "Drivers sorted numerically by number from low to high" '\n')
    
    dict_list = sorted(dict_list, key = lambda item: item["num"])
    for driver in dict_list:
        if driver["first"] == "Lewis":
            print(driver["last"], driver["first"], driver["num"], driver["car"], "YEET!!")
        else:
            print(driver["last"], driver["first"], driver["num"], driver["car"])
            
main()