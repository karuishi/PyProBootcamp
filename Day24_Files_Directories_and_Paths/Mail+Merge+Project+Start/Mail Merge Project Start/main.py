#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

    
# Read the invited names
with open("./Input/Names/invited_names.txt") as invited_names:
    names_list = invited_names.readlines()
    
# Read the starting letter
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    contents = starting_letter.read()
    # Replace the [name] placeholder with the actual name of the guest
    for guest_name in names_list:
        formatted_name = guest_name.strip()
        new_letter = contents.replace("[name]", formatted_name)
        with open(f"./Output/ReadyToSend/letter_for_{guest_name}.docx", "w") as invite:
            invite.write(new_letter)
