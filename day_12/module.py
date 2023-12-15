# Write a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'
import random
import string

def random_user_id():
    return ''.join(random.choice(string.hexdigits.lower()) for _ in range(6))

# Example usage:
user_id = random_user_id()
print(user_id)


# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) 
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
import random
import string

def user_id_gen_by_user():
        char_count = int(input("Enter the number of characters for each user ID: "))
        id_count = int(input("Enter the number of user IDs to generate: "))
        
        if char_count <= 0 or id_count <= 0:
            raise ValueError("Both counts must be positive integers.")
        
        user_ids = []
        for _ in range(id_count):
            user_id = ''.join(random.choice(string.hexdigits.lower()) for _ in range(char_count))
            user_ids.append(user_id)

        return user_ids

# Example usage:
generated_ids = user_id_gen_by_user()
print(generated_ids)

# Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
import random

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue
# Example usage:
rgb_color = rgb_color_gen()
print(f"Generated RGB color: {rgb_color}")

# Write a function list_of_hexa_colors which returns 
# any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def list_of_hexa_colors(num_colors):
    if num_colors <= 0:
        return "Number of colors must be a positive integer."

    colors = []
    for _ in range(num_colors):
        hex_color = ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colors.append("#" + hex_color)

    return colors

# Example usage:
num_colors_to_generate = 5
hex_colors = list_of_hexa_colors(num_colors_to_generate)
print("Generated Hexadecimal Colors:")
print(hex_colors)


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

def list_of_rgb_colors(num_colors):
    if num_colors <= 0:
        return "Number of colors must be a positive integer."

    colors = []
    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colors.append((red, green, blue))

    return colors

# Example usage:
num_colors_to_generate = 5
rgb_colors = list_of_rgb_colors(num_colors_to_generate)
print("Generated RGB Colors:")
print(rgb_colors)

# Write a function generate_colors which can generate any number of hexa or rgb colors.
import random

def generate_colors(num_colors, color_format='hex'):
    if num_colors <= 0:
        return "Number of colors must be a positive integer."

    colors = []
    for _ in range(num_colors):
        if color_format == 'hex':
            hex_color = ''.join(random.choice('0123456789abcdef') for _ in range(6))
            colors.append("#" + hex_color)
        elif color_format == 'rgb':
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            colors.append((red, green, blue))
        else:
            return "Invalid color format. Use 'hex' or 'rgb'."

    return colors

# Example usage:
num_colors_to_generate = 5

hex_colors = generate_colors(num_colors_to_generate, color_format='hex')
print("Generated Hexadecimal Colors:")
print(hex_colors)

rgb_colors = generate_colors(num_colors_to_generate, color_format='rgb')
print("\nGenerated RGB Colors:")
print(rgb_colors)

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(original_list)

print(f"Original List: {original_list}")
print(f"Shuffled List: {shuffled_result}")

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def generate_unique_random_numbers():
    unique_numbers = set()

    while len(unique_numbers) < 7:
        unique_numbers.add(random.randint(0, 9))

    return list(unique_numbers)

# Example usage:
random_numbers = generate_unique_random_numbers()
print("Generated Unique Random Numbers:", random_numbers)
