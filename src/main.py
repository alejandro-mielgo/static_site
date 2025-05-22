import os

from duplicate_folder import copy_folder
from gencontent import generate_page, generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


if __name__=='__main__':

    copy_folder(dir_path_static,dir_path_public)


    print("Generating page...")

    generate_pages_recursive(dir_path_content,template_path,dir_path_public)