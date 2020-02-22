# About these files

These Python scripts are based on [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (second edition), chapter 9, by Al Sweigart. All of the code is explained in that chapter.

It is recommended that you **run the files** in the Terminal. Run them multiple times until you understand exactly what each line in the code does.

**Script:** *copy_into_new_file.py*

- Open a plain-text file, read its contents, and write them into a new file. Note that this script demonstrates the File object `.read()` and `.write()` methods. If you want to automate the process of copying a lot of files, [use the `shutil` module](https://docs.python.org/3/library/shutil.html) instead.

**Script:** *file_reading_examples.py*

- Run this file to see a demonstration of `.readlines()`, `.seek()`, `.strip()`, and `print( myfile.read() )` vs. just `myfile.read()`.

**Text file:** *jabberwocky.txt*

- This is a plain-text file used by other scripts in this folder.

**Script:** *pathlib_example.py*

- How to check whether a filename already exists in the current folder. See Sweigart pages 214–215, “Checking Path Validity,” for details.

**Script:** *pathlib_example2.py*

- How to create a new (empty) file in the current folder, after first checking whether the filename you want to use already exists. See Sweigart pages 214–215, “Checking Path Validity,” for details.

**Script:** *readlines_example.py*

- Use the `readlines()` method to create a Python list from a plain-text file, and then write specified extracts into a new text file.

**Text file:** *state_data.txt*

- This is a plain-text file used by *readlines_example.py*.

.
