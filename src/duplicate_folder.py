import os
import shutil


def delete_destination(dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    else:
        print(f"Directory {dest} does not exist, skipping deletion.")

def recursive_copy(src,dest):
    os.mkdir(dest)
    children:list = os.listdir(src)
    for child in children:
        if os.path.isfile(os.path.join(src,child)):
            print(f"copying {child} to {dest}")
            shutil.copy(os.path.join(src,child),os.path.join(dest,child))
        else:
            recursive_copy(os.path.join(src,child),os.path.join(dest,child))

def copy_folder(src,dest):
    delete_destination(dest)
    recursive_copy(src,dest)


if __name__ == "__main__":

    origin = './static'
    destination = "./public"
    
    copy_folder(origin,destination)

