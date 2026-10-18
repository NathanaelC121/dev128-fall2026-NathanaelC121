# Nathanael Cooper
# DEV 128 - Lab 2, Exercise 14-2
# October 16th, 2026
# DEV 128 - Exercise 14-2   

#Import the Movie class from objects. 
from objects import Movie

#Lists the movies. 
def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie.getStr()}")
    print()

#Adds a movie to the list of Movie objects.
def add(movie_list):
    # Keep prompting the user to enter a title.
    while True:
        name = input("Name: ").strip()
        if name != "":
            break
        print("Please enter a movie name.")

    #Stores the year as a positive number and not a float.
    while True:
        #Handles false inputs for year and makes sure the year is an int. 
        try:
            year = int(input("Year: "))
            if year > 0:
                break
            print("Please enter a year greater than zero.")
        except ValueError:
            print("Please enter the year as a whole number.")

    movie = Movie(name, year)
    movie_list.append(movie)
    print(f"{movie.name} was added.\n")

#Delete a movie from the list of movies
def delete(movie_list):
    if len(movie_list) == 0:
        print("There are no movies to delete.\n")
        return

    # Guards/Checks for non-number inputs before checking the movie number's range.
    try:
        number = int(input("Number: "))
    except ValueError:
        print("Please enter a whole number.\n")
        return

    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie.name} was deleted.\n")

#displays the menu  
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()

#Does the main function calls/ initializes the movie_list with movie objects
#instead of separate lists of movie details.
def main():
    # Stores Movie objects instead of separate lists of movie details.
    movie_list = [Movie("Monty Python and the Holy Grail", 1975),
                  Movie("On the Waterfront", 1954),
                  Movie("Cat on a Hot Tin Roof", 1958)]

    print("The Amazing Movie Program\n")
    display_menu()
 #Takes and checks for input for the commands
    while True:
        command = input("Command: ").strip().lower()
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")


if __name__ == "__main__":
    main()
