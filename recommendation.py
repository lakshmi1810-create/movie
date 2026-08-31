from db import mycursor
def view_all_movies():
    data = "SELECT * FROM movies"
    mycursor.execute(data)
    result = mycursor.fetchall()
    for x in result:
        print(x)

def search_movie():
    num = input("Enter Movie Name You Want to search : ")
    data = "SELECT * FROM movies WHERE title LIKE %s"
    values = ("%" + num + "%",)
    mycursor.execute(data, values)
    result = mycursor.fetchall()
    if result:
        for x in result:
            print("\n" + "="*50)
            print(f"Title         : {x[1]}")
            print(f"Type          : {x[2]}")
            print(f"Genre         : {x[3]}")
            print(f"Language      : {x[4]}")
            print(f"Platform      : {x[5]}")
            print(f"Actors        : {x[6]}")
            print(f"Release Year  : {x[7]}")
            print(f"Rating        : {x[8]}")
            print("="*50)
    else:
        print("Movie Not Found")

def recommend_by_type():
    print("What do you want to watch?")
    print("1. Movie")
    print("2. Series")
    try:
        num = int(input("Enter Your preferred type : "))
        if num == 1:
            type_name = "Movie"
        elif num == 2:
            type_name = "Series"
        else:
            print("Invalid choice. Please select a valid type.")
            return
        data = "SELECT * FROM movies WHERE type = %s"
        values = (type_name,)
        mycursor.execute(data, values)

        result = mycursor.fetchall()
        if result:
            for x in result:
                print(x)
        else:
            print("No Movies/Series Found")
    except ValueError:
        print("Invalid input! Please enter only 1 or 2.")

def recommend_by_genre():
    num = (input("Enter your preferred genre : "))
    data = "SELECT * FROM movies WHERE genre LIKE %s"
    values = ("%" + num + "%",)
    mycursor.execute(data, values)
    result = mycursor.fetchall()
    if result:
        for x in result:
            print(x)
    else:
        print("No recommendations found for the selected genre.")

def recommend_by_language():
    num = (input("Enter your preferred language : "))
    data = "SELECT * FROM movies WHERE language LIKE %s"
    values = ("%" + num + "%",)
    mycursor.execute(data, values)
    result = mycursor.fetchall()
    if result:
        for x in result:
            print(x)
    else:
        print("No recommendations found for the selected language.")

def recommend_by_platform():
    num = (input("Enter your preferred platform : "))
    data = "SELECT * FROM movies WHERE platform LIKE %s"
    values = ("%" + num + "%",)
    mycursor.execute(data, values)
    result = mycursor.fetchall()
    if result:
        for x in result:
            print(x)
    else:
        print("No recommendations found for the selected platform.")

def recommend_by_actors():
    num = (input("Enter your preferred actor or actress : "))
    data = "SELECT * FROM movies WHERE actors LIKE %s"
    values = ("%" + num + "%",)
    mycursor.execute(data, values)
    result = mycursor.fetchall()
    if result:
        for x in result:
            print(x)
    else:
        print("No recommendations found for the selected actors.")


        
