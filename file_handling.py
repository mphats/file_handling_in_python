def modify_content(content):  
    # This is just a simple modification example:   
    # We'll convert all text to uppercase and add a line indicating it was modified.  
    modified_content = content.upper() + "\n\n-- This content was modified --\n"  
    return modified_content  

def main():  
    # Ask the user for the filename to read  
    input_filename = input("Enter the name of the file to read: ")  
    
    try:  
        # Open the input file for reading  
        with open(input_filename, 'r') as infile:  
            content = infile.read()  
            
        # Modify the content  
        modified_content = modify_content(content)  
        
        # Specify the output filename (you could ask the user for this as well)  
        output_filename = input("Enter the name of the file to write the modified content to: ")  
        
        # Open the output file for writing  
        with open(output_filename, 'w') as outfile:  
            outfile.write(modified_content)  
        
        print(f"Modified content has been written to '{output_filename}'.")  

    except FileNotFoundError:  
        print(f"Error: The file '{input_filename}' does not exist.")  
    except IOError:  
        print(f"Error: Could not read the file '{input_filename}' or write to the output file.")  
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")  

if __name__ == "__main__":  
    main()