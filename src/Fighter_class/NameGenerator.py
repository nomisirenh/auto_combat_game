from random import choices

def name_generator():
    with open ("Fighter_class/names.txt","r") as file:
        names = file.readlines()
        name = choices(names)
        return name[0].strip()
