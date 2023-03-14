import os
import shutil
import schedule
import time
import logging

logging.basicConfig(filename="log.txt", level=logging.INFO,format="%(asctime)s %(message)s", filemode="w")
#this line logs a message on an INFO level in a file named "log.txt" with the time and the date of the message.
def synchronize():
    source_folder = r'C:\Users\Ahmed\OneDrive\Desktop\Source Folder' #r refers to raw string.
    replica_folder = r'C:\Users\Ahmed\OneDrive\Desktop\Replica folder' 
    source_files = os.listdir(source_folder) #returns a list of every file in source folder.
    replica_files = os.listdir(replica_folder) #return a list of every file in replica folder.
    # compare filenames between replica folder and source folder using for loop.
    for replica_file_name in replica_files:
        # store file path in replica_file_path variable.
        replica_file_path = os.path.join(replica_folder, replica_file_name)
    
        found = False #indicates that a file was not yet found.
        for source_file_name in source_files:           
            if replica_file_name == source_file_name:
                found = True
                break
        if not found:
            os.remove(replica_file_path)
            print("file is deleted from replica folder")
            logging.info("file is deleted from replica folder")
        

    # compare filenames between source folder and replica folder using for loop
    for source_file_name in source_files:
        # store file path in source_file_path variable
        source_file_path = os.path.join(source_folder, source_file_name)

        found = False
        for replica_file_name  in replica_files:            
            if source_file_name == replica_file_name:
               found = True
               break
        if not found:
            shutil.copy2(source_file_path, os.path.join(replica_folder, source_file_name))
            print("file is copied from source folder to replica folder")
            logging.info("file is copied from source folder to replica folder")
       
synchronize()        
schedule.every(1).minutes.do(synchronize) #the task is scheduled to run every minute.

while True: #a loop to check any scheduled tasks.
    schedule.run_pending() #execute any scheduling tasks.
    time.sleep(1) #pause the loop for one second.
