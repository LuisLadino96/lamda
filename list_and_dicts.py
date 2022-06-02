def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Luis", "Lastname": "Ladino"}

    super_list= [
        {"firstname": "Luis", "Lastname": "Ladino"},
        {"firstname": "laura", "Lastname": "sosa"},
        {"firstname": "ximena", "Lastname": "garcia"},
        {"firstname": "katherine", "Lastname": "torres"},
        {"firstname": "martha", "Lastname": "Ladino"},
    ]

    super_dict= {
        "natural_nums":[1, 2, 3, 4, 5, 6],
        "Integer_nums":[-1, 2, 0, 6, 9],
        "floating_nums":[1.5, 2.0, 3.6, 9.0]
    }

    for key,value in super_dict.items():
        print(key,"-",value)

    for list_name in super_list:
        for key,value in list_name.items():
            print(f'{key}-{value}')




if __name__=='__main__':
    run()