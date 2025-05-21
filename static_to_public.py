import os
import shutil


def delete_public():
    shutil.rmtree("./public")

if __name__ == "__main__":
    delete_public()

