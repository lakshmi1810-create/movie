from recommendation import *
from analysis import *
from visualization import *
def menu():
    df = load_data()
    while True:
        print("\n=========================================")
        print("       MOVIE RECOMMENDATION SYSTEM")
        print("=========================================")
        print("1. View all movies")
        print("2. Search movie")
        print("3. Recommended by type")
        print("4. Recommended by genre")
        print("5. Recommended by language")
        print("6. Recommended by platform")
        print("7. Recommended by actors")
        print("8. Analysis")
        print("9. Visualization")
        print("10. Exit")
        print("\n=========================================")

        try:
            choice = int(input("Enter your choice : "))
            if choice == 1:
                view_all_movies()
            elif choice == 2:
                search_movie()
            elif choice == 3:
                recommend_by_type()
            elif choice == 4:
                recommend_by_genre()
            elif choice == 5:
                recommend_by_language()
            elif choice == 6:
                recommend_by_platform()
            elif choice == 7:
                recommend_by_actors()
            elif choice == 8:
                analysis_menu(df)
            elif choice == 9:
                visualization_menu(df)
            elif choice == 10:
                print("Thanku for visiting.")
                break
            else:
                print("Invalid choice. Please select a valid choice.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

menu()

    