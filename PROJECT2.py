import pickle

user_ids = []
user_passes = []
booked = []
dict_movie_time_screen = {
    "1": {"time": ["5","22","12","18"], "movie": ["DUNKI","MATRIX","KRISH 3","INTERSTELLAR"]},
    "2": {"time": [], "movie": []},
    "3": {"time": [], "movie": []},
    "4": {"time": [], "movie": []}}
booked_Seats = {"userid": {"booked seats": [], "movie": []}}
movies = ["DUNKI","MATRIX","KRISH 3","INTERSTELLAR"]
screens = ["1", "2", "3", "4"]
times = []
timeslots = []
dict_movie_seats = {"movie": {"time": "seats"}}

for i in range(6, 24, 3):
    timeslots.append(i)


class Movie:
    def __init__(self, movie):
        self.movie = movie


class Timeslot:
    def __init__(self, time):
        self.time = time


class Screen:
    def __init__(self, screen):
        self.screen = screen


class Seat(Movie):
    def __init__(self, movie, time, row, seat):
        self.book_seat = seat
        self.book_row = row
        super().__init__(movie)
        self.movie = movie.upper()
        self.time = time

        seats = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        self.seats = seats
        dict_movie_seats[self.movie] = {self.time: self.seats}


class BookingDetails:
    def __init__(self):
        print(booked_Seats)
        print(dict_movie_seats)


class Admin(Seat, Timeslot, Screen):
    def __init__(self, movie, time, screen, seat):
        super().__init__(movie, time, screen, seat)
        self.__adminid = "pankaj"
        self.__adminpass = "12345"

    def add_movie(self):
        print("1", "2", "3", "4")
        self.screen = input("Select the screen you want to use")
        self.movie = input("enter name of movie")
        self.movie = self.movie.upper()
        movies.append(self.movie)
        self.time = input("enter time")
        times.append(self.time)
        dict_movie_time_screen[self.screen]["time"].append(self.time)
        dict_movie_time_screen[self.screen]["movie"].append(self.movie)
        print(movies)
        print(dict_movie_time_screen)

    def remove_movie(self):
        print("1", "2", "3", "4")
        self.screen = input("Select the screen you want to use")
        self.movie = input("enter movie you want to remove")
        self.movie = self.movie.upper()
        z = movies.index(self.movie)
        movies.pop(z)
        self.time = input("enter time")
        times.pop(z)
        dict_movie_time_screen[self.screen]["time"].pop(z)
        dict_movie_time_screen[self.screen]["movie"].pop(z)
        print(movies)
        print(dict_movie_time_screen)


    def login_id(self):
        z = input("enter user id")
        p = input("enter admin password")
        if z == self.__adminid and p == self.__adminpass:
            print("admin access granted")
        else:
            print("admin access failed")

    def create_screen(self):
        self.screen = input("enter new screen number")
        dict_movie_time_screen[self.screen] = {"time": [], "movie": []}

    def save_data(self):
        with open("movies.pickle", "wb") as f:
            pickle.dump(movies, f)
        with open("screens.pickle", "wb") as f:
            pickle.dump(screens, f)
        with open("timeslots.pickle", "wb") as f:
            pickle.dump(times, f)

    def load_data(self):
        try:
            with open("movies.pickle", "rb") as f:
                self.movies = pickle.load(f)
            with open("screens.pickle", "rb") as f:
                self.screens = pickle.load(f)
            with open("timeslots.pickle", "rb") as f:
                self.times = pickle.load(f)
        except FileNotFoundError:
            pass  # No data files found, initialize empty structures


class User(Seat, Movie):
    def __init__(self, movie, time, row, seat, userid, userpass):
        super().__init__(movie, time, row, seat)
        self.userid = userid
        self.userpass = userpass

        if userid not in booked_Seats:
            booked_Seats[userid] = {"booked_seats": [], "movie": []}

    def set_id(self):
        self.userid = input("set user id")
        self.userpass = input("set users password")

        if self.userid not in booked_Seats:
            booked_Seats[self.userid] = {"booked_seats": [], "movie": []}

        user_ids.append(self.userid)
        user_passes.append(self.userpass)

        print("ID successfully set")

    def login_user(self):
        p = input("enter user id")
        o = input("enter users password")
        P = user_ids.index(p)
        O = user_passes.index(o)
        if P == O:
            print("user account logged in successfully")
        else:
            print("invalid login")

    def book_seat_func(self):
        print(dict_movie_time_screen)
        print(dict_movie_seats)
        self.movie = input("enter the name of movie")
        self.movie = self.movie.upper()
        self.time = input("choose your time")
        self.book_row = input("enter row number")
        z = int(self.book_row)
        self.book_seat = input("enter seat number")
        p = int(self.book_seat)
        book_row = z - 1
        book_seat = p - 1
        book = self.seats[book_row].pop(book_seat)

        # Use self.userid to access booked_Seats
        booked_Seats[self.userid]["booked_seats"].append(book)
        dict_movie_seats[self.movie] = {self.time: self.seats}
        for i in dict_movie_seats[self.movie][self.time]:
            print(i)


user1 = User("DUNKI", "5", 1, 2, "1", "1")

admin1 = Admin("g", "g", "t", "g")
while True:
    z = input("Welcome to cinema system, login as:\n1. User\n2. Admin\nType 'quit' to exit\n")

    if z == "1":
        l = input("Press 1 to set user id \nPress 2 to login existing id\n")
        if l == "1":
            user1.set_id()
            user1.login_user()
            user1.book_seat_func()
            while True:
                c = input("1 to book another seat\n2 to quit\n")
                if c == "1":
                    user1.book_seat_func()
                elif c == "2":
                    print("Thanks for booking")
                    break
                else:
                    print("Invalid input")

    elif z == "2":
        admin1.login_id()
        print("WELCOME TO CINEMA ADMIN. WHAT WOULD YOU LIKE TO BE DOING.")
        while True:
            z = input("\n1. Add a movie\n2. Remove a movie\n3. Add a screen\n4. Save data\n5. Load data\n6. Quit\n")
            if z == "1":
                admin1.add_movie()
            elif z == "2":
                admin1.remove_movie()
            elif z == "3":
                admin1.create_screen()
            elif z == "4":
                admin1.save_data()
            elif z == "5":
                admin1.load_data()
            elif z == "6":
                break
            else:
                print("Invalid input")

    elif z.lower() == "quit":
        print("Exiting the cinema system.")
        break

    else:
        print("Invalid input")

