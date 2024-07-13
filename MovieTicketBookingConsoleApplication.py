class Theater:
    def __init__(self, name, movies):
        self.name = name
        self.movies = movies
        self.rows = 10
        self.cols = 20
        self.seats = [["x" for _ in range(self.cols)] for _ in range(self.rows)]

    def display_seats(self):
        print("\nTheater Seating:")
        for row in range(self.rows):
            print(f"{row + 1:02d}", end=" ")
            for col in range(self.cols):
                print(self.seats[row][col], end=" ")
            print()

    def reserve_seat(self):
        while True:
            self.display_seats()
            row = int(input("\nEnter row number (or 0 to exit): "))
            if row == 0:
                break
            col = int(input("Enter column number: "))
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                if self.seats[row - 1][col - 1] == "👍":
                    print("Seat already reserved.")
                else:
                    self.seats[row - 1][col - 1] = "👍"
                    print("Seat reserved successfully.")
            else:
                print("Invalid seat location.")
        return True  # Always return True to indicate the process was completed

class Movie:
    def __init__(self, title, showtimes, price):
        self.title = title
        self.showtimes = showtimes
        self.price = price

    def display(self):
        for i, showtime in enumerate(self.showtimes, start=1):
            print(f"{i}. {self.title} - {showtime} - ₹{self.price:.2f}")

class Snack:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class SnackBar:
    def __init__(self):
        self.snacks = [
            Snack("Popcorn", 5.00),
            Snack("Soda", 2.50),
            Snack("Candy", 3.00)
        ]

    def display_snacks(self):
        print("\nAvailable Snacks:")
        for i, snack in enumerate(self.snacks, start=1):
            print(f"{i}. {snack.name} - ₹{snack.price:.2f}")

    def order_snacks(self):
        total = 0
        while True:
            self.display_snacks()
            choice = int(input("\nEnter snack number to order (or 0 to finish): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(self.snacks):
                total += self.snacks[choice - 1].price
                print(f"Added {self.snacks[choice - 1].name} to order. Total so far: ₹{total:.2f}")
            else:
                print("Invalid snack number.")
        print(f"\nTotal amount due for snacks: ₹{total:.2f}")
        return total

class District:
    def __init__(self, name, theaters):
        self.name = name
        self.theaters = theaters

    def display_theaters(self):
        for i, theater in enumerate(self.theaters, start=1):
            print(f"{i}. {theater.name}")

    def select_theater(self):
        self.display_theaters()
        user1 = int(input("Enter theater number: "))
        if 1 <= user1 <= len(self.theaters):
            selected_theater = self.theaters[user1 - 1]
            print(selected_theater.name)
            for movie in selected_theater.movies:
                movie.display()
            movie_choice = int(input("\nEnter movie number: "))
            if 1 <= movie_choice <= len(selected_theater.movies):
                selected_movie = selected_theater.movies[movie_choice - 1]
                selected_theater.reserve_seat()
                snack_bar = SnackBar()
                snack_total = snack_bar.order_snacks()
                total_bill = selected_movie.price + snack_total
                print(f"\nTotal amount due for movie and snacks: ₹{total_bill:.2f}")
            else:
                print("Invalid movie number.")
        else:
            print("Invalid theater number.")

# Data setup
districts = [
    District("Erode", [
        Theater("ARR", [Movie("Leo", ["9.00 to 10.30"], 150.00), Movie("Thunivu", ["11.00 to 1.00"], 120.00), Movie("Joe", ["2.00 to 3.30"], 100.00)]),
        Theater("SKM", [Movie("Leo", ["9.00 to 10.30"], 150.00), Movie("Thunivu", ["11.00 to 1.00"], 120.00), Movie("Joe", ["2.00 to 3.30"], 100.00)]),
        Theater("Ram", [Movie("Leo", ["9.00 to 10.30"], 150.00), Movie("Thunivu", ["11.00 to 1.00"], 120.00), Movie("Joe", ["2.00 to 3.30"], 100.00)])
    ]),
    District("Salem", [
        Theater("Raj", [Movie("Leo", ["9.00 to 10.30"], 150.00), Movie("Thunivu", ["11.00 to 1.00"], 120.00), Movie("Joe", ["2.00 to 3.30"], 100.00)]),
        Theater("Loki", [Movie("Leo", ["9.00 to 10.30"], 150.00), Movie("Thunivu", ["11.00 to 1.00"], 120.00), Movie("Joe", ["2.00 to 3.30"], 100.00)]),
        Theater("Nano", [Movie("Leo", ["9.00 to 10.30"], 150.00), Movie("Thunivu", ["11.00 to 1.00"], 120.00), Movie("Joe", ["2.00 to 3.30"], 100.00)])
    ]),
    District("Chennai", [
        Theater("PVR", [Movie("Leo", ["9.00 to 10.30"], 150.00), Movie("Thunivu", ["11.00 to 1.00"], 120.00), Movie("Joe", ["2.00 to 3.30"], 100.00)]),
        Theater("Golden", [Movie("Leo", ["9.00 to 10.30"], 150.00), Movie("Thunivu", ["11.00 to 1.00"], 120.00), Movie("Joe", ["2.00 to 3.30"], 100.00)]),
        Theater("Ega", [Movie("Leo", ["9.00 to 10.30"], 150.00), Movie("Thunivu", ["11.00 to 1.00"], 120.00), Movie("Joe", ["2.00 to 3.30"], 100.00)])
    ])
]

# Main logic
print("---------Welcome to TicketNew-----------")
print("Districts:")

for i, district in enumerate(districts, start=1):
    print(f"{i}. {district.name}")

user = int(input("Enter district number: "))
if 1 <= user <= len(districts):
    selected_district = districts[user - 1]
    selected_district.select_theater()
else:
    print("Invalid district number.")
