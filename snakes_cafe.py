menu = {
     "Appetizers":["Wings","Cookies","Spring Rolls"],
     "Entrees": ["Salmon","Steak","Meat Tornado","A Literal Garden"],
     "Desserts":["Ice Cream","Cake","Pie"],
     "Drinks":["Coffee","Tea","Unicorn Tears"]
     }

all_items = [element for sublist in menu.values() for element in sublist]

def intro():
    print(
     """
     **************************************
     **    Welcome to the Snakes Cafe!   **
     **    Please see our menu below.    **
     **
     ** To quit at any time, type "quit" **
     **************************************
     """
    )

def items(key):
    for ele in menu.get(key):
        print(ele)



def print_menu():
        
    for key in menu.keys():
        print(f"""
        {key}
        ----------
        """
        )
        items(key)
        
          
def user_insert():
    user_input=input(">")
    formated_userinput=user_input.capitalize()   
    return  formated_userinput
               

def user_input_handleer():
    i=1
    user_input_obj={}
    user_input = user_insert()
    while(user_input.lower() != "quit"):
            
            if user_input in all_items:
                if  user_input in  user_input_obj: i = i+1
                else: i = 1
                user_input_obj[user_input] = i
                print(user_input_obj)

                for key in user_input_obj.keys():
                    print(f"** {key} order of {user_input_obj[key]} has been added to your meal **")
                
               
            else:
                print(f"sorry we dont have {user_input} !")
                
            user_input = user_insert()    

    end_application()


def end_application():
    print("thanks for using snakes cafe application !")          



intro()
print_menu()
user_input_handleer()


