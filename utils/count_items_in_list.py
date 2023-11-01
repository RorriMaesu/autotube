# Define the function like before, Morty!
def count_items_in_file(file_path):
    try:
        with open(file_path, 'r') as f:
            text = f.read()
            items = text.split(',')
            num_items = len(items)
        print(f"Found {num_items} items, Morty! We did it!")
        return num_items
    except FileNotFoundError:
        print("File's not there, Morty! It's like it entered another dimension!")
        return 0

# Call the function and store the result in the variable, Morty! Pay attention!
item_count = count_items_in_file('utils/prompts.txt')

# Wanna see the magic number, Morty? Here it is!
print(f"The variable item_count has {item_count} in it. It's that easy, Morty!")
