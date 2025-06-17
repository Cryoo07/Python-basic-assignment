from animals import Lion, Elephant, Parrot
from enclosure import Enclosure

if __name__ == "__main__":
    big_cats = Enclosure("Big Cats")
    birds = Enclosure("Birds")

    simba = Lion("Simba", 5)
    simba.set_feeding_time("12:00 PM")
    
    dumbo = Elephant("Dumbo", 10)
    dumbo.set_feeding_time("1:00 PM")

    polly = Parrot("Polly", 2)
    polly.set_feeding_time("11:00 AM")

    big_cats.add_animal(simba)
    big_cats.add_animal(dumbo)
    birds.add_animal(polly)

    print("== Big Cats Enclosure ==")
    big_cats.list_animals()
    big_cats.make_all_sounds()

    print("\n== Birds Enclosure ==")
    birds.list_animals()
    birds.make_all_sounds()

    print("\n== Feeding Animals ==")
    big_cats.feed_all()
    birds.feed_all()
