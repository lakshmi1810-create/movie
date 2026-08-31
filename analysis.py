import numpy as np
import pandas as pd
from db import mydb
def load_data():
    query = "SELECT * FROM movies"
    df = pd.read_sql(query,mydb)
    return df

def total_content(df):
    total = len(df)
    return total

def type_analysis(df):
    result = df["type"].value_counts()
    return result

def genre_analysis(df):
    result = (
        df["genre"]
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
    )
    return result

def language_analysis(df):
    result = (
        df["language"]
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
    )
    return result

def platform_analysis(df):
    result = df["platform"].value_counts()
    return result

def release_year_analysis(df):
    years = np.array(df["release_year"].dropna(), dtype=int)
    latest = np.max(years)
    oldest = np.min(years)
    average = np.mean(years)
    return latest, oldest, average

def rating_analysis(df):
    rating = np.array(df["rating"].dropna(), dtype=float)
    highest = np.max(rating)
    lowest = np.min(rating)
    average = np.mean(rating)
    return highest, lowest, average

def analysis_menu(df):
    while True:
        print("\n================================")
        print("       MOVIE DATA ANALYSIS")
        print("================================")
        print("1. Total Content")
        print("2. Type Analysis")
        print("3. Genre Analysis")
        print("4. Language Analysis")
        print("5. Platform Analysis")
        print("6. Release Year Analysis")
        print("7. Rating Analysis")
        print("8. Back")
        print("================================")

        try:
            choice = int(input("Enter your choice : "))

            if choice == 1:
                print("Total Content : ",total_content(df))

            elif choice == 2:
                print("\nContent Type Analysis : ")
                print(type_analysis(df))

            elif choice == 3:
                print("\nContent Genre Analysis : ")
                print(genre_analysis(df))

            elif choice == 4:
                print("\nContent Language Analysis : ")
                print(language_analysis(df))

            elif choice == 5:
                print("\nContent Platform Analysis : ")
                print(platform_analysis(df))

            elif choice == 6:
                latest, oldest, average = release_year_analysis(df)
                print("Latest Year : ", latest)
                print("Oldest Year : ", oldest)
                print("Average Year : ", round(average,2))

            elif choice == 7:
                highest, lowest, average = rating_analysis(df)
                print("Highest Rating : ", highest)
                print("Lowest Rating : ", lowest)
                print("Average Rating : ", round(average,2))

            elif choice == 8:
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Enter numbers only!")

    
    
