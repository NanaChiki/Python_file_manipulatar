# Python file manipulator

A simple Python script for manipulating text files from the command line.
Supports reversing, copying, duplicating, and replacing strings in files.

## Usage


python3 filemanipulatar.py <command> <input_file> <output_file or n or needle>

### Commands

- `reverse <input_file> <output_file>`
   Reverses the contents of `input_file` and writes to `output_file`.

- `copy <input_file> <output_file>`
  Copies the contents of `input_file` to `output_file`.

- `duplicate-contents <input_file> <n>`
  Duplicates the contents of `input_file` `n` times and overwrites `input_file`.

- `replace-string <input_file> <needle> <new_string>`
  Replaces all occurrences of `needle` with `new_string` in `input_file`.

### Examples

```base
python3 filemanipulator.py reverse test.txt reversed.txt
python3 filemanipulator.py copy test.txt copied.txt
python3 filemanipulator.py duplicate-contents test.txt 3
python3 filemanipulator.py replace-string test.txt "old" "new"
```

## Requirements

- Python 3.x

## Error Handling 

The script prints usage instructions and errors for invalid commands or arguments.
