#Nathanael Cooper
#Dev 128-Lab 2, Exercise 14-2
#October 16th, 2026
#Stores movie details and formats them for display.
#Is Imported into movie.py for Movie objects.

#Imports dataclass so it auto self initializes.
from dataclasses import dataclass

@dataclass
class Movie:
#Initializes the attributes for every new movie.
    name: str=""
    year: int = 1975
#Returns the movie object's details with the name first, then the year.
    def getStr(self):
        return(f"{self.name} ({self.year})")
