
def main():
    print ("ET0735 (DevOps for AIoT) - Lab2 - Introduction to Python")
    display_main_menu()
    num_list=get_user_input()
    average =calc_average(num_list)
    print ("Average Temperature is " +str(average))
    max_min = find_min_max(num_list)
    print("Maximum Temperature is "+ str(max_min[0]))
    print("Minimum Temperature is "+ str(max_min[1]))
    sorted = sort_temperature(num_list)
    print("Sorted Temperature is "+ str(sorted))
    median = calc_median_temperature(sorted)
    print("Median Temperature is "+ str(median))

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (eg.5, 67,32)")

def get_user_input():
    print("get_user_input")
    user_input = input()
    string_list = user_input.split(",")
    float_list = [float(i) for i in string_list]
    return float_list
    
def calc_average(temp):
    print("calc_average")
    average = sum(temp)/len(temp)
    return average




def find_min_max(temp):
    print("find_min_max")
    max_temp = max(temp)
    min_temp = min(temp)

    return [max_temp,min_temp]

def sort_temperature(temp):
    print("sort_temperature")
    sorted_temp = sorted(temp)  # Sort the list in ascending order
    #sorted_temp = sorted(temp, reverse=True) #in descending order
    return sorted_temp

def calc_median_temperature(temp):
    print("calc_median_temperature")
    n = len(temp)
    mid = n // 2

    # If odd number of elements, return the middle one
    if n % 2 != 0:
        median = temp[mid]
    # If even number of elements, return the average of the two middle ones
    else:
        median = (temp[mid - 1] + temp[mid]) / 2
    return median


if __name__=="__main__":
    main()