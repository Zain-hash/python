def create_file():
    try:
       # create new file
       with open("new.txt.txt", "w") as file:
           #write 
           file.write("Hello, this is the beginning\n")
           file.write("420365")
           file.write("I'm learning python.\n")
    except(FileNotFoundError, PermissionError) as e:
        print("Error occured while creating file:", e)
    finally:
        print("File creation completed")
        
def read_and_display():
    try:
        #read and display file conents
        with open("neww.txt.txt", "r") as file:
            contents = file.read()
            print("Contents of new.txt.txt:")
            print(contents)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied to read the file.")
        
def append_to_file():
     try:
         #open file in append mode
         with open("new.txt.txt", "a") as file:
             #append additional lines
             file.write("Learmimg to append line 1.\n")
             file.write("011458\n")
             file.write("I have to understand.\n")
     except (FileNotFoundError, PermissionError) as e:
         print("Error occurred while appending to file:", e)
     finally:
         print("Appending to file completely.")
         
if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()
         