amount_of_guests = int(input('Enter a real amount of guests:\t'))
if amount_of_guests > 50:
    print('A restaurant')
elif 20 <= amount_of_guests <= 50:
    print('Cafe')
elif amount_of_guests < 20:
    print('Sweet home')
