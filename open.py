#!/usr/bin/python3
"""
    This Python code demonstrates the following features:
    
    * opening, writing and closing a text file.
    
    """
import shutil, os, sys, datetime
from datetime import datetime
def create_backup(source_path, destination_dir):
    """
     Contains the code to mark a file and directory used to copy and make a backup of a file.

    """
    #used to ensure the source path is correct
    if not os.path.exists(source_path):
        print(f"Error: Source path",{source_path}," does not exist.")
        return
    os.makedirs(destination_dir, exist_ok=True)
    now = datetime.now()
    timestamp = now
    base_name = os.path.basename(os.path.normpath(source_path))

    if os.path.isdir(source_path):
        backup_name = f'{base_name}_backup_{timestamp}'
        target_path = os.path.join(destination_dir, backup_name)

        shutil.copytree(source_path, target_path)
        print(f"Successfully backed up to: ",{target_path})
        
    elif os.path.isfile(source_path):
        file_name, file_ext =os.path.splitext(base_name)  
        backup_name = f"{file_name}_{timestamp}{file_ext}"  
        target_path = os.path.join(destination_dir, backup_name)

        shutil.copy2(source_path, target_path)
        print(f'Successfully backed up file to: ',{target_path})

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a filename.")
        print("Usage: python script.py <filename>")
        sys.exit(1)
    target_file = sys.argv[1]
    print('Searching for: '+ target_file)
    Search_word = target_file
    with open("backupcfg.py", "r") as file:
        if Search_word in file.read():
            print(target_file + ' included within the Config File. Proceeding to backup.')
            Destination = "./backups"
            create_backup(target_file, Destination)            
        else:
            print('Error: '+ target_file + ' not included within the Config File. Ensure command line has full file name. Make sure to Type the full file name including its extension (.txt, .py)')
                 
if __name__ == "__main__":
    main()