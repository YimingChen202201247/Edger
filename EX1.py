# Step 1: Read the content of file_to_read.txt
with open('file_to_read.txt', 'r') as file:
    content = file.read()

# Step 2: Count occurrences and perform replacements
word_to_replace = "terrible"
occurrences = content.count(word_to_replace)
new_content = content.split()

for i in range(len(new_content)):
    if new_content[i] == word_to_replace:
        if (i + 1) % 2 == 0:
            new_content[i] = "pathetic"
        else:
            new_content[i] = "marvellous"

# Step 3: Write the modified content to result.txt
with open('result.txt', 'w') as file:
    file.write(" ".join(new_content))

# Display the total occurrences of "terrible"
print(f"Total occurrences of 'terrible': {occurrences}")

print("Replacements completed. Check result.txt for the modified text.")
