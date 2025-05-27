import sys

# Get arguments
command = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

# Function to validate the command type and number of arguments
def validate_arguments(command):
  if command not in ['reverse', 'copy', 'duplicate-contents', 'replace-string']:
     print('Error: Invalid command. Supported commands are: "reverse", "copy", "duplicate-contents", "replace-string"')
     sys.exit(1)
  if command in ['reverse', 'copy'] and len(sys.argv) != 4:
     print('Usage: python3 filemanipulatar.py <command> <input_file> <output_file>')
     sys.exit(1)
  elif command == 'duplicate-contents' and len(sys.argv) != 4:
     print('Usage: python3 filemanipulatar.py duplicate-contents <input_file> <n>')
     sys.exit(1)
  elif command == 'replace-string' and len(sys.argv) != 5:
     print('Usage: python3 filemanipulatar.py replace-string <input_file> <needle> <new_string>')
     sys.exit(1)

# Read content from the input file and write to the output file
def read_file(input_file):
  # Read the input file
  try:
      with open(input_file, 'r') as file:
          return file.read()
  except FileNotFoundError:
      print(f'Error: The file {input_file} does not exist.')
      sys.exit(1)

def write_file(output_file, content):
  # Write the content to the output file
  try:
      with open(output_file, 'w') as file:
            file.write(content)
  except Exception as e:
      print(f'Error writing to file {output_file}: {e}')
      sys.exit(1)

##############################################

# Validate input and store the input file into the variable content
validate_arguments(command)
content = read_file(input_file)

# Reverse the content
if command == 'reverse':
   reversed_content = content[::-1]
   write_file(output_file, reversed_content)
   print(f'Successfully reversed {input_file} to {output_file}.')

# Copy the content
elif command == 'copy':
   write_file(output_file, content)
   print(f'Successfully copied {input_file} to {output_file}.')

# Duplicate the content n times
elif command == 'duplicate-contents':
   try:
      n = int(sys.argv[3])
      if n <= 0:
         print('Error: n must be a positive integer.')
         sys.exit(1)
      duplicated_content = content * n
      write_file(input_file, duplicated_content)
      print(f'Successfully duplicated contents of {input_file} {n} times.')  
   except ValueError:
      print('Error: n must be an integer.') 
      sys.exit(1)

# Replace a string in the content
elif command == 'replace-string':
   needle = sys.argv[3]
   new_string = sys.argv[4] 
   
   new_content = content.replace(needle, new_string)
   write_file(input_file, new_content)
   print(f'Successfully replaced "{needle}" with "{new_string}" in {input_file}.')
   
   






