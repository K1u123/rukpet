class Ticket:
    tickets = {}

    def __init__(self):
        self.tickets = self.tickets


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
            print('Билеты найдены:', *result)
        else:
            print('Билет отсутствует')

    def book_ticket(self, ticket_number):
        if ticket_number in self.ticket.tickets:
            print(f'Билет {ticket_number} забронирован успешно!')
            del self.ticket.tickets[ticket_number]
        else:
            print('Билет отсутствует')


ticket = Ticket()
admin = Admin(ticket)
logged_admin = LoggedAdmin(1235)

if logged_admin.login():
    admin.add_ticket('123', 'Москва', 'Пекин', '2022-12-31', '10:00')
    admin.add_ticket('456', 'Новосибирск', 'Ханой', '2022-12-31', '15:00')
    admin.del_ticket('123')
    admin.route_change('456', 'Москва', 'Ханой')
    booking_system = BookingSystem(ticket, admin)

    booking_system.ticket_listing()

    booking_system.search_tickets('Москва', 'Пекин', '2022-12-31')
    booking_system.search_tickets('Новосибирск', 'Ханой', '2022-12-31')
    booking_system.search_tickets('Москва', 'Ханой', '2022-12-31')

    booking_system.book_ticket('123')
    booking_system.book_ticket('456')
    booking_system.book_ticket('456')
    booking_system.book_ticket('999')
else:
    print("Неверный пароль")