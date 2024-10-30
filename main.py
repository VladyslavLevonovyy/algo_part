class Ticket:

    def __init__(self, country="Невідомо", duration=0, price=0, seats=1, plane_type="Business", days_travel=0):
        self.__country = country
        self.__duration = duration
        self.__price = price
        self.__days_travel = days_travel

        self.seats = seats
        self.plane_type = plane_type

    def get_country(self):
        return self.__country

    def get_duration(self):
        return self.__duration

    def get_price(self):
        return self.__price

    def get_days_travel(self):
        return self.__days_travel

    def set_country(self, country):
        self.__country = country

    def set_duration(self, duration):
        self.__duration = duration

    def set_price(self, price):
        self.__price = price

    def set_days_travel(self, days=1):
        self.__days_travel = (self.__days_travel - days)

    def __str__(self):
        return (f"Ticket to {self.__country}, for {self.__duration} days, "
                f"for {self.__price} USD, {self.seats} seats, {
                    self.plane_type} class, "
                f"{self.__days_travel} days until expiry")

    def __repr__(self):
        return (f"Ticket('{self.__country}', {self.__duration}, {self.__price}, "
                f"{self.seats}, '{self.plane_type}', {self.__days_travel})")

    def __del__(self):
        print(f"Ticket to {self.__country} was deleted")


def get_nearest_ticket(ticket_list):
    nearest_ticket = ticket_list[0]
    for ticket in ticket_list:
        if ticket.get_days_travel() < nearest_ticket.get_days_travel():
            nearest_ticket = ticket
    return nearest_ticket

    nearest_ticket = min(
        ticket_list, key=lambda ticket: ticket.get_days_travel())
    return nearest_ticket


def main():
    Ticket1 = Ticket("Egypt", 20, 2000, days_travel=5)
    Ticket2 = Ticket("Turkey", 15, 1500, days_travel=10)
    Ticket3 = Ticket("Spain", 7, 1000, days_travel=13)

    tickets = [Ticket1, Ticket2, Ticket3]

    nearest_ticket = get_nearest_ticket(tickets)
    print("\nNearest tickets:")
    print(nearest_ticket)


main()
