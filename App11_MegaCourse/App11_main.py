import pandas as pd

# Read the CSV files
df = pd.read_csv('hotels.csv', dtype={'id': str})
df2 = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        '''Book a hotel by changing the availability to No'''
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        return availability == 'yes'


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f'''
        Thank you for your reservation
        Here are your booking data
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        '''
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {
            'number': self.number,
            'expiration': expiration,
            'holder': holder,
            'cvc': cvc
        }
        if card_data in df2:
            return True


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = CreditCard(number='1234567890123456')
    if credit_card.validate(expiration='12/26', holder="JOHN SMITH", cvc="123"):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print("There was a problem with your card")
else:
    print('Sorry! Hotel is full')
