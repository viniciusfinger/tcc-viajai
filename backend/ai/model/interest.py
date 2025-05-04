from enum import Enum

class Interest(Enum):
    MUSIC = "music"
    MOVIES = "movies"
    HISTORICAL_PLACES = "historical places"
    SPORTS = "sports"
    FOOD = "food"
    BEAUTY = "beauty"
    TECHNOLOGY = "technology"
    SCIENCE = "science"
    ART = "art"
    ARCHITECTURE = "architecture"
    NATURE = "nature"
    ANIMALS = "animals"
    SHOPPING = "shopping"
    

    def __str__(self):
        return self.value
    
