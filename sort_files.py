
import os
import shutil

def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s

base="/home/germain/backup"

#to do: create from this script destination directories : base/html, base/latex, base/pdf

wb_downloader_base="/home/germain/websites"
nb_files={}

for root, dirs, files in os.walk(wb_downloader_base):
    for file in files:
        if file.endswith(".html"):
#            print(root, files)
            if root.endswith("pdf"):
                new_string=rchop(root,"/pdf")
                ext=".pdf"
            elif root.endswith("latex"):
                new_string=rchop(root,"/latex")
                ext=".tex"
            else:
                new_string=root
                ext=".html"

            base_filename=new_string.rsplit('/',1)[1]

            filename_with_ext=base_filename+ext
 
            if filename_with_ext in nb_files:
                nb_files[filename_with_ext]=nb_files[filename_with_ext]+1
                new_filename=base_filename+"-"+str(nb_files[filename_with_ext])
            else:
                nb_files[filename_with_ext]=1 
                new_filename=base_filename

            new_filename=new_filename + ext
            

#            print("file_name", new_filename,"\n")
            source=root+"/"+file


            print("source:",source,"\n")          
            
            if ext==".pdf":
                dest = base +"/pdf/" 
            elif ext==".tex":
                dest = base+"/latex/"
            else:
                dest = base+"/html/"
            dest=dest+new_filename
            print("destination:",dest,"\n") 
            shutil.copyfile(source,dest)
