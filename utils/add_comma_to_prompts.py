def add_comma_to_file(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Add comma to the end of each line
    updated_lines = [line.strip() + ',' + '\n' for line in lines]

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

# Usage:
file_path = "C:\\Users\\autotube\\Documents\\autotube\\utils\\prompts.txt"
add_comma_to_file(file_path)
