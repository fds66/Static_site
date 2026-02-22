import os
import shutil


'''
suggested helpful library funcs

os.path.exists
os.listdir
os.path.join
os.path.isfile
os.mkdir
shutil.copy
shutil.rmtree


'''







def copy_source_dir_to_dest_dir(source_dir,dest_dir):

    try:
        print("running copy source to dest\n")

        
        if not os.path.exists(source_dir):
            raise Exception("source path does not exist")
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)
        
        
        
        
        
        #copies all files and subdirectories nested files etc
        #recursive function
        #recommends logging path of each file you copy so you can see what's happening as you run and debug your code

        
        
        # list the files in this directory
        if os.path.isdir(source_dir):
            contents = os.listdir(source_dir)
            #print(f"contents of {source_dir} is \n{contents}\n\n")
            for item in contents:
                #print(f"item is {item}\n")
                item_path = os.path.join(source_dir,item)
                copy_dest = os.path.join(dest_dir,item)
                if os.path.isdir(item_path):
                    #print(f"{item} is a directory\n")
                    
                    if not os.path.exists(copy_dest):
                        #print(f"make this directory {copy_dest}\n")
                        mkdir_result = os.mkdir(copy_dest)
                        #print(f"mkdir_result {mkdir_result}")   
                    
                    
                    copy_source_dir_to_dest_dir(item_path,copy_dest)
                    continue
                    
                
                elif os.path.isfile(item_path):
                    #print(f"{item} is a file")
                    #print(f"copy this item to {copy_dest}\n")
                    copy_result = shutil.copy(item_path,copy_dest)
                    #print(f"New file is   {copy_result}\n")
                    if not copy_result:
                        raise Exception("copy operation failed")
                    continue
                else:
                    print("not a file or directory")
                    break
















    except Exception as e:
        return f"Error: could complete the copying: {e}"

   

