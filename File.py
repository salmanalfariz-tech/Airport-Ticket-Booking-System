import tkinter as tk

# Backend Classes and Functions
class Flight:
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_date, departure_time, total_seats, available_seats):
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.total_seats = total_seats
        self.available_seats = available_seats


class Passenger:
    def __init__(self, name, passport_number, seat_number, flight=None):
        self.name = name
        self.passport_number = passport_number
        self.seat_number = seat_number
        self.flight = flight


def book_ticket():
    name = name_entry.get()
    passport_number = passport_entry.get()

    try:
        flight_number = int(flight_entry.get())
        seat_number = int(seat_entry.get())

        for flight in flights:
            if flight.flight_number == flight_number:
                if flight.available_seats > 0:
                    flight.available_seats -= 1
                    passenger = Passenger(name, passport_number, seat_number, flight)

                    ticket_info.set("Ticket booked successfully!\n"
                                    f"Passenger name: {passenger.name}\n"
                                    f"Passport number: {passenger.passport_number}\n"
                                    f"Flight number: {passenger.flight.flight_number}\n"
                                    f"Departure airport: {passenger.flight.departure_airport}\n"
                                    f"Arrival airport: {passenger.flight.arrival_airport}\n"
                                    f"Departure date: {passenger.flight.departure_date}\n"
                                    f"Departure time: {passenger.flight.departure_time}\n"
                                    f"Seat number: {passenger.seat_number}")
                    return

        ticket_info.set("Flight is full. Please try another flight.")
    except ValueError:
        ticket_info.set("Please enter valid flight number and seat number.")


# Frontend (Tkinter GUI)
root = tk.Tk()
root.title("Flight Booking")
root.geometry('500x400+250+300')  # Set window size and position
root.configure(bg='lightgray')  # Set background color

# Sample flights
flights = [
    Flight(1, "MAA", "DEL", "2023-10-14", "10:00", 100, 100),
    Flight(2, "DEL", "BOM", "2023-10-15", "12:00", 100, 100),
    Flight(3, "BOM", "MAA", "2023-10-16", "14:00", 100, 100),
]

# Labels and Entry Fields
tk.Label(root, text="Enter your name:", bg='lightgray').pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Enter your passport number:", bg='lightgray').pack()
passport_entry = tk.Entry(root)
passport_entry.pack()

tk.Label(root, text="Enter the flight number:", bg='lightgray').pack()
flight_entry = tk.Entry(root)
flight_entry.pack()

tk.Label(root, text="Enter the seat number:", bg='lightgray').pack()
seat_entry = tk.Entry(root)
seat_entry.pack()

# Book Ticket Button
book_button = tk.Button(root, text="Book Ticket", command=book_ticket)
book_button.pack(pady=10)

# Display Ticket Information
ticket_info = tk.StringVar()
ticket_info_label = tk.Label(root, textvariable=ticket_info, bg='lightgray')
ticket_info_label.pack()

# Start the Tkinter event loop
root.mainloop()