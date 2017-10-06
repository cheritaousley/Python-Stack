# keys= ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7']
names = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    dictionary= dict(zip(names, favorite_animal))
    print dictionary
make_dict(names,favorite_animal)
