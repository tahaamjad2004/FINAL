##TASK 2 

class Property:
    def __init__(self, property_id, name, location, description, price_per_night):
        self.property_id = property_id
        self.name = name
        self.location = location
        self.description = description
        self.price_per_night = price_per_night
        self.availability_status = True

    def update_availability_status(self, status):
        self.availability_status = status

class User:
    def __init__(self, user_id, name, contact_details):
        self.user_id = user_id
        self.name = name
        self.contact_details = contact_details

class Host(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.properties = []

    def list_property(self, property):
        self.properties.append(property)

class Guest(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.bookings = []

    def book_property(self, property, check_in_date, check_out_date):
        booking = Booking(property, self, check_in_date, check_out_date)
        self.bookings.append(booking)
        property.update_availability_status(False)
        return booking

class Booking:
    def __init__(self, property, guest, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.property = property
        self.guest = guest
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.booking_status = "confirmed"  

    def cancel_booking(self):
        self.booking_status = "canceled"
        self.property.update_availability_status(True)
 






    

    