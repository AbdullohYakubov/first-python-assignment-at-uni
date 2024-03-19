user_input = input('Please input the data as a raw string: ')
user_input_list = user_input.split(',')

valid_chars = '0123456789.'
input_index = 0
is_valid = True

for input in user_input_list:
    decimal_point_count = 0

    for element in input:
        if element in valid_chars:
            if element == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    is_valid = False
                    print('Invalid Input')
                    break
        else:
            is_valid = False
            print('Error: Invalid characters!')
            break
    else:
        pass

    if is_valid and (not input == ''):
        user_input_list[input_index] = float(input)
        input_index += 1

if is_valid:
    print(f'The converted list: {user_input_list}')

# Calculating the mean
running_total = 0
for i in range(len(user_input_list)):
    if is_valid and (not user_input_list[i] == ''):
        running_total += user_input_list[i]
    else:
        break
mean_value = running_total / len(user_input_list)

if is_valid:
    print(f'The mean: {mean_value}')

# Calculating the mode
number_of_instances = 1
mode = 0
for i in range(len(user_input_list)):
    if user_input_list.count(user_input_list[i]) > number_of_instances:
        number_of_instances = user_input_list.count(user_input_list[i])
        mode = user_input_list[i]  
    else:
        mode = user_input_list[0]
if is_valid:
    print(f'The mode: {mode}') 

# Calculating the standard deviation
mean_deviations = 0
for i in range(len(user_input_list)):
    if is_valid and (not user_input_list[i] == ''):
        mean_deviations += pow(user_input_list[i] - mean_value, 2)
    else:
        break
standard_deviation_value = pow(mean_deviations / len(user_input_list), 1/2)

if is_valid:
    print(f'The standard deviation: {standard_deviation_value}')

# Sorting
index = 0
for i in range(0, len(user_input_list)):
    if is_valid and (not user_input_list[i] == ''):
        for j in range(i + 1, len(user_input_list)):
            if user_input_list[i] >= user_input_list[j]:
                user_input_list[i], user_input_list[j] = user_input_list[j], user_input_list[i]
    else:
        break

if is_valid:
    print(f'The sorted list: {user_input_list}')