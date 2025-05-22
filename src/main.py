import os
import sys

from duplicate_folder import copy_folder
from gencontent import generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


if __name__=='__main__':
    
    basepath  = sys.argv[1] if len(sys.argv) >= 2 else '/'
    print(f'basepath value is {basepath}')

    copy_folder(dir_path_static,dir_path_public)



    print("Generating page...")

    generate_pages_recursive(dir_path_content,template_path,dir_path_public, basepath)