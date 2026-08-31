import matplotlib.pyplot as plt
import seaborn as sns
import analysis
sns.set_style("darkgrid")

def plot_type(df):
    result = analysis.type_analysis(df)
    plt.figure(figsize=(6,4))
    sns.barplot(x=result.index, y=result.values, palette="Set2")
    plt.title("Movies vs Series")
    plt.xlabel("Content Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_genre(df):
    result = analysis.genre_analysis(df)
    result = result.head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=result.values, y=result.index, palette="viridis")
    plt.title("Top 10 Genres")
    plt.xlabel("Count")
    plt.ylabel("Genre")
    plt.tight_layout()
    plt.show()

def plot_language(df):
    result = analysis.language_analysis(df)
    plt.figure(figsize=(10,6))
    sns.barplot(
        x=result.values,
        y=result.index,
        palette="magma"
    )
    plt.title("Language Distribution")
    plt.xlabel("Count")
    plt.ylabel("Language")
    plt.tight_layout()
    plt.show()

def plot_platform(df):
    result = analysis.platform_analysis(df)
    plt.figure(figsize=(8,5))
    sns.barplot(x=result.index, y=result.values,palette="coolwarm")
    plt.title("Platform Distribution")
    plt.xlabel("Platform")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_release_year(df):
    year_count = df["release_year"].value_counts().sort_index()
    plt.figure(figsize=(10,5))
    sns.lineplot(x=year_count.index, y=year_count.values, marker='*')
    plt.title("Content Release Trend")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Releases")
    plt.tight_layout()
    plt.show()

def plot_rating(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["rating"].dropna(),bins=10, kde=True, color="purple")
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies/Series")
    plt.tight_layout()
    plt.show()

def visualization_menu(df):
    while True:
        print("\n================================")
        print("       VISUALIZATION MENU")
        print("================================")
        print("1. Type Graph")
        print("2. Genre Graph")
        print("3. Language Graph")
        print("4. Platform Graph")
        print("5. Release Year Graph")
        print("6. Rating Graph")
        print("7. Back")
        print("================================")
        try:
            choice = int(input("Enter your choice : "))
            if choice == 1:
                plot_type(df)
            elif choice == 2:
                plot_genre(df)          
            elif choice == 3:
                plot_language(df)                                  
            elif choice == 4:
                plot_platform(df)                            
            elif choice == 5:
                plot_release_year(df)          
            elif choice == 6:
                plot_rating(df)                                               
            elif choice == 7:
                break           
            else:
                print("Invalid choice!")
            
        except ValueError:
            print("Enter numbers only!")
            
                
                
            
        
        
        


