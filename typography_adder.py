# specify the path to the prompts.txt file inside the utils folder
file_path = 'utils/prompts.txt'

try:
    # read the content from the existing text file
    with open(file_path, 'r') as file:
        content = file.read()

    # add the text "bold text says bharani nakshatra" before each comma
    modified_content = content.replace(',', ' "bold text clearly says bharani nakshatra" typography,')

    # specify the path for the output file inside the utils folder
    output_path = 'utils/output_file.txt'

    # write the modified content to a new text file
    with open(output_path, 'w') as file:
        file.write(modified_content)

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
