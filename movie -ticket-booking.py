movies={
    "1": {"name":"Alpha","price":250},
    "2": {"name":"Dhurandar","price":200},
    "3": {"name":"spiderman:brand new day","price":300}
}
while True:
    print("\n=====Movie Ticket Booking=====")
    print("1. Alpha-250")
    print("2.Dhurandar-200")
    print("3.Spiderman:brand new day-300")
    print("4.Exit")
    choice=input("Select movie: ")
    if choice =="4":
        print("Thank you! Visit again.")
        break
    if choice in movies:
        movie=movies[choice]
        print("You selected:",movie["name"])
        tickets = int(input("enter number of tickets:"))
        total=tickets*movie["price"]
        print("\n=====Booking Details=====")
        print("Movie:",movie["name"])
        print("Tickets:",tickets)
        print("Total price:rupees-",total)
        print("Booking scuessfull!")
    else: 
        print("Invaild Choice!")