user_input = input('Please input the data as a raw string: ')
user_input_list = user_input.split(',')

valid_chars = '0123456789.'
input_index = 0

for input in user_input_list:
    decimal_point_count = 0

    for element in input:
        if element in valid_chars:
            if element == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    print('Invalid Input')
                    break
        else:
            # print('Invalid characters')
            break
    else:
        pass
        # print('Valid float')
        # element = float(element)
        # print(isinstance(element, float))

    # input = float(input)
    # print(isinstance(input, float))

    user_input_list[input_index] = float(input)
    input_index += 1

print(user_input_list)

# Calculating the mean
running_total = 0
for i in range(len(user_input_list)):
    running_total += user_input_list[i]
mean_value = running_total / len(user_input_list)
print(mean_value)

# Calculating the mode
number_of_instances = 1
mode = 0
for i in range(len(user_input_list)):
    # number_of_instances += user_input_list.count(i) - number_of_instances 
    if user_input_list.count(user_input_list[i]) > number_of_instances:
        number_of_instances = user_input_list.count(user_input_list[i])
        mode = user_input_list[i]  
print(mode) 

# Calculating the standard deviation
mean_deviations = 0
for i in range(len(user_input_list)):
    mean_deviations += pow(user_input_list[i] - mean_value, 2)
standard_deviation_value = pow(mean_deviations / len(user_input_list), 1/2)
print(standard_deviation_value)

# Sorting
# first_number = 0
# second_number = 0
# new_arr = []
for i in range(len(user_input_list)):
    if user_input_list[i] > user_input_list[i+1]:
        if user_input_list[i] != user_input_list[len(user_input_list) - 1]:
            # user_input_list = [user_input_list[i+1], user_input_list[i]]
            user_input_list.append(user_input_list[i+1])
            user_input_list.append(user_input_list[i])
        else:
            continue
print(user_input_list)