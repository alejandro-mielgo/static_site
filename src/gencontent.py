import re
import os

from blocks_markdown import markdown_to_html_node

def extract_title(markdown:str)->str:
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            if line [2:]!="":
                return line[2:]
    raise ValueError('# title not found in markdown ')


def generate_page(from_path:str, template_path:str, dest_path:str, basepath:str)->None:

    print(f'Generating page from {from_path} to {dest_path} using {template_path}.')

    markdown_f = open(from_path)
    markdown_content = markdown_f.read()
    markdown_f.close()

    template_f = open(template_path)
    template = template_f.read()
    template_f.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)  

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
 

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath):
    items = os.listdir(dir_path_content)
    for item in items:
        
        src_path = os.path.join(dir_path_content,item)
        dest_path = os.path.join(dest_dir_path,item)
        print('source path',src_path)
        print('dest path',dest_path)
    
        if os.path.isfile(src_path) and src_path[-3:]=='.md':
            generate_page(src_path, template_path, dest_path[:-2]+"html", basepath)

        else:
            generate_pages_recursive(src_path, template_path, dest_path, basepath)


