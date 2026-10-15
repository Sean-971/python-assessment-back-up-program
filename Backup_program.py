
"""

This program is designed to create a back up from a test file and to upload the backup to a new text file.
This program was created Sean Hosking, and was created on the 30/09/2026 12:40

"""
import sys, shutil, os
 
target_file = sys.argv[1]

 
locating_target_file = True
while locating_target_file == True:
    with open('config.txt')as f:
            for x in f:
                if x == target_file:
                    print(x)
            locating_target_file = False
                
    
    

    
    
    
    
    
    locating_target_file = False



 


