from random import choices

def name_generator():
    with open ("names.txt","r") as file:
        names = file.readlines()
        name = choices(names)
        return name[0].strip()

if __name__ == '__main__':
    print(name_generator())