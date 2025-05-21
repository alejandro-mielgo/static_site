from src.duplicate_folder import copy_folder


if __name__=='__main__':
    origin = './static'
    destination = "./public"
    copy_folder(origin,destination)