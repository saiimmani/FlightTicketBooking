class FlightTicketBookingSystem:
    available_seats = {
        'E': 50,
        'B': 20,
        'FC': 10
    }

    prices = {
        'E': 300,
        'B': 600,
        'FC': 1000
    }

    booked_seats = {
        'E': 0,
        'B': 0,
        'FC': 0
    }

    destinations = {
        'New York': 'NYC',
        'Los Angeles': 'LAX',
        'Chicago': 'ORD',
        'Miami': 'MIA'
    }

    payment_methods = ['CC', 'DC', 'PP']

    def start(self):
        while True:
            print("\nMenu:")
            print("1. Display Available Seats")
            print("2. Display Destinations")
            print("3. Display Payment Methods")
            print("4. Book Ticket")
            print("5. Cancel Ticket")
            print("6. Quit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.display_available_seats()
            elif choice == '2':
                self.display_destinations()
            elif choice == '3':
                self.display_payment_methods()
            elif choice == '4':
                self.book_ticket()
            elif choice == '5':
                self.cancel_ticket()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def display_available_seats(self):
        print("\nAvailable Seats:")
        for class_name, seats in self.available_seats.items():
            print(f"{class_name}: {seats} seats")

    def display_destinations(self):
        print("\nAvailable Destinations:")
        for city, code in self.destinations.items():
            print(f"{city} ({code})")

    def display_payment_methods(self):
        print("\nAvailable Payment Methods:")
        for method in self.payment_methods:
            print(method)

    def book_ticket(self):
        class_name = input("Enter class (E for Economy, B for Business, FC for First Class): ").strip().upper()
        num_tickets = int(input("Enter the number of tickets to book: "))
        destination = input("Enter destination (NYC/LAX/ORD/MIA): ").strip().upper()
        payment_method = input("Enter payment method (CC for Credit Card, DC for Debit Card, PP for PayPal): ").strip().upper()

        if class_name in self.available_seats and destination in self.destinations.values():
            if payment_method in self.payment_methods:
                if num_tickets > 0 and num_tickets <= self.available_seats[class_name]:
                    self.available_seats[class_name] -= num_tickets
                    self.booked_seats[class_name] += num_tickets
                    total_price = self.prices[class_name] * num_tickets
                    print(f"Booking successful! {num_tickets} {class_name} ticket(s) to {destination}. Total Price: ${total_price}")
                    print(f"Payment successful using {payment_method}.")
                else:
                    print(f"Sorry, there are not enough available {class_name} seats.")
            else:
                print("Invalid payment method.")
        else:
            print("Invalid class or destination.")

    def cancel_ticket(self):
        class_name = input("Enter class (E for Economy, B for Business, FC for First Class): ").strip().upper()
        num_tickets = int(input("Enter the number of tickets to cancel: "))
        destination = input("Enter destination (NYC/LAX/ORD/MIA): ").strip().upper()
        payment_method = input("Enter payment method for refund (CC/DC/PP): ").strip().upper()

        if class_name in self.booked_seats and destination in self.destinations.values():
            if payment_method in self.payment_methods:
                if num_tickets > 0 and num_tickets <= self.booked_seats[class_name]:
                    self.available_seats[class_name] += num_tickets
                    self.booked_seats[class_name] -= num_tickets
                    total_refund = self.prices[class_name] * num_tickets
                    print(f"Cancellation successful! {num_tickets} {class_name} ticket(s) to {destination} cancelled. Total Refund: ${total_refund}")
                    print(f"Refund processed to your {payment_method}.")
                else:
                    print("Invalid number of tickets to cancel.")
            else:
                print("Invalid payment method.")
        else:
            print("Invalid class or destination.")

# Create an instance of the system and start it
flight_system = FlightTicketBookingSystem()
flight_system.start()
