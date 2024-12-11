class Ticket:
    tickets = {}

    def __init__(self):
        self.tickets = self.tickets


class Admin:
    def __init__(self, ticket):
        self.ticket = ticket

    def add_ticket(self, ticket_number, departure_point, destination, date, time):
        self.ticket.tickets[ticket_number] = {
            'departure point': departure_point,
            'destination': destination,
            'date': date,
            'time': time
        }

    def del_ticket(self, ticket_number):
        if ticket_number in self.ticket.tickets:
            del self.ticket.tickets[ticket_number]

    def route_change(self, ticket_number, departure_point, destination):
        if ticket_number in self.ticket.tickets:
            self.ticket.tickets[ticket_number]['departure point'] = departure_point
            self.ticket.tickets[ticket_number]['destination'] = destination


class LoggedAdmin:
    ADMIN_PASS = 12345

    def __init__(self, password):
        self.password = password

    def login(self):
        if self.password == self.ADMIN_PASS:
            return True
        else:
            return False


class BookingSystem:
    def __init__(self, ticket, admin):
        self.logged_admin = admin
        self.ticket = ticket

    def search_tickets(self, departure_point, destination, date):
        result = []
        for ticket_number, flight_details in self.ticket.tickets.items():
            if (flight_details['departure point'] == departure_point and
                    flight_details['destination'] == destination and
                    flight_details['date'] == date):
                result.append((ticket_number, flight_details['departure point'], flight_details['destination'], flight_details['date'], flight_details['time']))

        if result:
            print('������ �������:', *result)
        else:
            print('����� �����������')

    def book_ticket(self, ticket_number):
        if ticket_number in self.ticket.tickets:
            print(f'����� {ticket_number} ������������ �������!')
            del self.ticket.tickets[ticket_number]
        else:
            print('����� �����������')


ticket = Ticket()
admin = Admin(ticket)
logged_admin = LoggedAdmin(12435)

if logged_admin.login():
    admin.add_ticket('123', '������', '�����', '2022-12-31', '10:00')
    admin.add_ticket('456', '�����������', '�����', '2022-12-31', '15:00')
    admin.del_ticket('123')
    admin.route_change('456', '������', '�����')
    booking_system = BookingSystem(ticket, admin)

    booking_system.ticket_listing()

    booking_system.search_tickets('������', '�����', '2022-12-31')
    booking_system.search_tickets('�����������', '�����', '2022-12-31')
    booking_system.search_tickets('������', '�����', '2022-12-31')

    booking_system.book_ticket('123')
    booking_system.book_ticket('456')
    booking_system.book_ticket('456')
    booking_system.book_ticket('999')
else:
    print("�������� ������")