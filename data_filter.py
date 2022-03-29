"""
This program was build to filter data using python
"""
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    menu_options = {
        1: 'Python devs filter',
        2: 'Platzi workers filter',
        3: 'Adults filter',
        4: 'Old people filter'
    }

    print("\n", menu_options, "\n")

    option = int(input("Select the filter you would like to use in the data: (1, 2, 3 or 4): "))
    """PYTHON DEVS FILTER"""
    if option == 1:
        #list comprehension (Method 1)
        all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"] #list comprehension
        #high order functions: filter and map (Method 2)
        """all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA)) 
        all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))"""
        for worker in all_python_devs:
            print(worker)
            
    elif option == 2:
        """PLATZI WORKERS FILTER"""
        #list comprehension (Method 1)
        all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]== "Platzi"]
        #high order functions: filter and map (Method 2)
        """all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA)) 
        all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))"""
        for worker in all_platzi_workers:
            print(worker)

    elif option == 3:
        """ADULTS FILTER"""
        #list comprehension (Method 1)
        adults = [worker["name"] for worker in DATA if worker["age"] > 18]
        #high order functions: filter and map (Method 2)
        """adults = list(filter(lambda worker: worker["age"] > 18, DATA))
        adults = list(map(lambda worker: worker["name"], adults))"""
        for worker in adults:
            print(worker)

    elif option == 4:
        old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
        """
        old_people only works in python 3.9 or new versions
        '|' allows you to add dicts
        """
        for worker in old_people:
            print(worker)

    else:
        print("Please enter a valid option")
        run()


if __name__ == "__main__":
    run()