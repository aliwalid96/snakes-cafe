def welcoming():
    Wings=["Cookies"," Spring Rolls","Entrees"]
    Salmon=["Steak"," Meat Tornado "," A Literal Garden"]
    Desserts =["Ice Cream ","Cake","Pie"]
    Drinks=["Coffee","Tea","Unicorn Tears"]
    Cookies_counter=1
    Spring_Rolls_counter=1
    Entrees_counter=1
    Steak_counter=1
    Meat_Tornado_counter=1
    A_Literal_Garden_counter=1
    Ice_Cream_counter=1
    Cake_counter=1
    Pie_coonter=1
    coffe_counter=1
    Tea_counter=1
    Unicorn_Tears_counter=1




    print(" Welcome to the Snakes Cafe! \n Please see our menu below.\n To quit at any time, type \"quit\"")
    for item in Wings:
        print (item)
    print("------")
    for item in Salmon:
        print (item)
    print("------")

    for item in Desserts:
        print (item)
    print("------")
    for item in Drinks:
        print (item)
    
    
    
    print("\n *********************************** \n ")
    user_input=input("What would you like to order?")
  
    while user_input!="quit":

        if user_input in Wings:
            if user_input=="Cookies":
                Cookies_counter=Cookies_counter+1
                print( f"{Cookies_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")
           
            elif user_input=="Spring Rolls":
                Spring_Rolls_counter=Spring_Rolls_counter+1
                print( f"{Spring_Rolls_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")
            
            elif user_input=="Entrees":
                Entrees_counter=Entrees_counter+1
                print( f"{Entrees_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")

         

        elif user_input in Salmon:
            if user_input=="Steak":
                Steak_counter=Steak_counter+1
                print( f"{Steak_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")

            elif user_input=="Meat Tornado":
                Meat_Tornado_counter=Meat_Tornado_counter+1
                print( f"{Meat_Tornado_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")

            elif user_input=="A Literal Garden":
                A_Literal_Garden_counter=A_Literal_Garden_counter+1
                print( f"{A_Literal_Garden_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")
 
 
        

            

        
        elif user_input in Desserts:
            if user_input=="Ice Cream":
                Ice_Cream_counter=Ice_Cream_counter+1
                print( f"{Ice_Cream_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")

            elif user_input=="Cake":
                Cake_counter=Cake_counter+1
                print( f"{Cake_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")

            elif user_input=="Pie":
                Pie_coonter=Pie_coonter+1
                print( f"{Pie_coonter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")
         

        
        elif user_input in Drinks:

            if user_input=="Coffee":
                coffe_counter=coffe_counter+1
                print( f"{coffe_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")
            
            elif user_input=="Tea":
                Tea_counter=Tea_counter+1
                print( f"{Tea_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")
            
            elif user_input=="Unicorn Tears":
                Unicorn_Tears_counter=Unicorn_Tears_counter+1
                print( f"{Unicorn_Tears_counter} order of {user_input} have been added to your meal")
                user_input=input("What would you like to order?")
         
      

    
        
        elif user_input=="quit":
            break
    


    





print(welcoming())   

