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
        #print(f"inputs {source_dir},{dest_dir}\n")
        source_path = os.path.abspath(source_dir)
        if not os.path.exists(source_path):
            raise Exception("source path does not exist")
        
        dest_path = os.path.abspath(dest_dir)
        if not os.path.exists(dest_path):
            raise Exception("Destination path does not exist")
        
        print(f" full paths source_path,dest_path\n{source_path}\n{dest_path}\n\n")
    
        #first remove everything in the destination directory
        #dest_results = os.listdir(dest_path)
        #print(f"destination results are {dest_results}\n")
        

        #copies all files and subdirectories nested files etc
        #recursive function
        #recommends logging path of each file you copy so you can see what's happening as you run and debug your code

        
        if not os.path.isdir(dest_path):
            raise Exception ("Destination directory is not a directory")
        # list the files in this directory
        if os.path.isdir(source_path):
            
            contents = os.listdir(source_path)
            #print(f"contents of {source_path} is \n{contents}\n\n")
            for item in contents:
                #print(f"item is {item}\n")
                item_path = os.path.join(source_path,item)
                copy_dest = os.path.join(dest_path,item)
                if os.path.isdir(item_path):
                    #print(f"{item} is a directory\n")
                    #print(f"check if it exists, result {os.path.exists(copy_dest)}")
                    if os.path.exists(copy_dest):
                        item_contents = os.listdir(copy_dest)
                        #print(f"copy destination directory exists and has content {item_contents}")
                        
                        #print("delete")
                        rmtree_result = shutil.rmtree(copy_dest)
                        #print(f"rmtree result {rmtree_result}")
                    
                    #print(f"make this directory {copy_dest}\n")
                    mkdir_result = os.mkdir(copy_dest)
                    #print(f"mkdir_result {mkdir_result}")
                    
                    
                    
                    if not mkdir_result:
                        print("mkdir failed")
                    new_source = os.path.join(source_dir,item)
                    new_dest = os.path.join(dest_dir,item)
                    copy_source_dir_to_dest_dir(new_source,new_dest)
                    continue
                    
                
                elif os.path.isfile(item_path):
                    #print(f"{item} is a file")
                    #print(f"copy this item to {copy_dest}\n")
                    copy_result = shutil.copy(item_path,dest_path)
                    #print(f"New file is   {copy_result}\n")
                    if not copy_result:
                        raise Exception("copy operation failed")
                    continue
                else:
                    print("not a file or directory")
                    break
















    except Exception as e:
        return f"Error: could complete the copying: {e}"

   

