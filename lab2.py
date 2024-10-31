
def main():
    print ("ET0735 (DevOps for AIoT) - Lab2 - Introduction to Python")
    display_main_menu()
    num_list=get_user_input()
    average =calc_average(num_list)
    print ("Average Temperature is " +str(average))
    max_min = find_min_max(num_list)
    print("Maximum Temperature is "+ str(max_min[0]))
    print("Minimum Temperature is "+ str(max_min[1]))

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

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature(temp):
    print("calc_median_temperature")
    sorted_temp = sorted(temp)
    n = len(sorted_temp)
    mid = n // 2

    # If odd number of elements, return the middle one
    if n % 2 != 0:
        median = sorted_temp[mid]
    # If even number of elements, return the average of the two middle ones
    else:
        median = (sorted_temp[mid - 1] + sorted_temp[mid]) / 2
    return median


if __name__=="__main__":
    main()