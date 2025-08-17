# with open ("demo.txt", "w") as file:
#     content = file.write('''Twinkle Twinkle little star, \nHow I wander what you are
# Up about you were so high \nLike a diamond in the sky
# ''')

# def check_word(filename, word):
#     print("Checking if word exist in file or not....")
#     try:
#           with open(filename, "r") as file:
#             content_read = file.read()

#           if word.lower() in content_read.lower():
#               print(f"The word {word} exists in file")
#           else:
#              print(f"The word {word} doesnot exists in file")
#     except FileNotFoundError:
#       print(f'An exception occurred: {filename} is not found')
#     except IOError:
#         print(f"Could not able to read file {filename}")

# check_word('demo.txt', "Twinkle")

#program to generate tables in different files and store in folder
import os

def generate_multiplication_tables(start, end):
    """
    Generates multiplication tables from a specified start to end number.
    Each table is saved to a separate file in a new directory.
    """
    # 1. Define the folder name
    folder_name = "Multiplication_Tables_for_13_Year_Olds"

    # 2. Create the folder if it doesn't exist
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Created directory: '{folder_name}'")
    except OSError as e:
        print(f"Error creating directory '{folder_name}': {e}")
        return

    # 3. Loop through the numbers from 2 to 20
    for i in range(start, end + 1):
        # 4. Construct the file path for each table
        file_path = os.path.join(folder_name, f"table_of_{i}.txt")

        # 5. Open and write the multiplication table to the file
        try:
            with open(file_path, "w") as file:
                file.write(f"--- Multiplication Table of {i} ---\n")
                # Inner loop to generate the table from 1 to 10
                for j in range(1, 11):
                    result = i * j
                    file.write(f"{i} x {j} = {result}\n")
            print(f"Generated {file_path}")
        except IOError as e:
            print(f"Error writing to file '{file_path}': {e}")

# Run the program to generate the tables
generate_multiplication_tables(2,4)