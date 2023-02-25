motorcycles=[]


def motorcycleList():
    number_of_motorcycles=int(input("how many motorcycles do you own\n"))
    for motorcycle in range(0,number_of_motorcycles):
        motorcycle_name=input("enter the name of your motorcycle:\t")
        motorcycle_displacement=input("enter the displacement of your motorcycle:\t")
        motorcycle_bhp=input("enter the estimated horsepower/bhp/ps of the motorcycle:\t")
        motorcycle_year=input("enter the year of manufacturing/purchase:\t")
        motorcycles.append({
            'name':motorcycle_name,
            'displacement':motorcycle_displacement,
            'horsepower':motorcycle_bhp,
            'production':motorcycle_year
        })
    print("your list is updated")

def show_motorcycles():
    for motorcycle in motorcycles:
        print_motorcycles(motorcycle)


def print_motorcycles(motorcycle):
    print("your motorcycle/s is/are")
    print(
        f"""motorcycle: {motorcycle['name']}\t
        displacement: {motorcycle['displacement']}\t
        horsepower:{motorcycle['horsepower']}
        manufacture year: {motorcycle['production']}""")

def find():
    print("""the features you can search for are:\n 
    'name' for motorcycle name,
    \n'displacement',
    \nhorsepower',
    and \n'production'for production/manufactureyear""")
    find_by= input("what feature of the motorcycle are you looking for:\t")
    if find_by=='name':
        looking_for=input("enter the motorcycle name:\t")
    elif find_by=='displacement':
        looking_for=input("enter motorcycle displacement:\t")
    elif find_by=='horsepower':
        looking_for=input("enter the horsepower of the motorcycle:\t")
    else:
        looking_for=input("enter the year of purchase/manufacture:\t")

    searching=lambda search:search[find_by]
    found_motorcycle=finding_individual(motorcycles,looking_for,searching)
    print(found_motorcycle)


def finding_individual(items,searched,finder):
    found=[]
    for i in items:
        if finder(i)==searched:
            found.append(i)

    return found




MENU="""enter what you would like to do:\n
        to add motorcycles to your list click '+'\n
        to view your list click '>'\n
        to find motorcycle click '@'\n
        to quit click 'q'\n"""

option={
    '+':motorcycleList,
    '>':show_motorcycles,
    '@':find,
}
def menu():
    selection=input(MENU)
    while selection.lower() != "q":
        if selection in option:
            selected_function=option[selection]
            selected_function()
        else:
            print("you have entered an invalid operator")
        selection = input(MENU)

menu()



