with open("names.txt") as f:
    names = f.read().splitlines()

    print("Names in the file:")
    for i,name in enumerate(names):
        print(f"{i+1}: {name}")