#Import os module
import os

# Ask User inputs for directory, file type and string to search.
search_dir_path = input("Enter the directory in which you want to search for string/word, for e.g. /tmp etc.: ")
file_type_to_search_to_search = input("Enter the File Type in which you want to search for string for e.g. .log or .txt etc.: ")
search_str_word_word = input("Enter the search string : ")

# Append a directory separator if not already present
if not (search_dir_path.endswith("/") or search_dir_path.endswith("\\") ): 
        search_dir_path = search_dir_path + "/"
                                                          
# If path does not exist, set search path to current directory from which script is being executed.
if not os.path.exists(search_dir_path):
        search_dir_path ="."

# Repeat for each file in the directory  
for fname in os.listdir(path=search_dir_path):

   # Apply file type filter   
   if fname.endswith(file_type_to_search):

        # Open file for reading
        fo = open(search_dir_path + fname)

        # Read the first line from the file
        line = fo.readline()

        # Initialize counter for line number
        line_no = 1

        # Loop until EOF
        while line != '' :
                # Search for string in line
                index = line.find(search_str_word)
                if ( index != -1) :
                    print(fname, "[", line_no, ",", index, "] ", line, sep="")

                # Read next line
                line = fo.readline()  

                # Increment line counter
                line_no += 1
        # Close the files
        fo.close()