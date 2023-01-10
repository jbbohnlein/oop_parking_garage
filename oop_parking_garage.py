class ParkingGarage():

    # You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

    tickets = []
    parkingSpaces = []
    currentTicket = {
        'paid' = [True, False]
    }

    """
        The ParkingGarage class will have tickets, parking spaces, and current tickets.
        
        Attributes for the class: 
        - tickets: expected to be a list
        - parking spaces: expected to be a list
        - current tickets: expected to be a dictionary
    """

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets          # list
        self.parkingSpaces = parkingSpaces   # list
        self.currentTicket = currentTicket  # dictionary


    def takeTicket(self, tickets, parkingSpaces):
# - This should decrease the amount of tickets available by 1
        self.tickets = len(tickets) - 1         #Something with len() + or - 1??
# - This should decrease the amount of parkingSpaces available by 1 
        self.parkingSpaces = len(parkingSpaces) - 1


    def payForParking(self): 
    # - Display an input that waits for an amount from the user and store it in a variable             WHAT KIND OF INPUT??
    # INPUT COULD BE THEIR CREDIT CARD BEING 'INPUTTED'? 
        while self.currentTicket['paid'] == False:
            payment = input("Please insert your credit card, and then type 'done' ")
            if payment == 'done':
            # - This should update the "currentTicket" dictionary key "paid" to True 
                self.currentTicket['paid':] = self.currentTicket['paid': True]
            # - If the payment variable is not empty (meaning the ticket has been paid) -> 
#           display a message to the user that their ticket has been paid and they have 15mins to leave
#           
                print('Your ticket has been paid. You have 15 minutes to exit the garage.')
            else:
                print('Please try paying for your ticket again.') 


    def leaveGarage(self):
        # - If the ticket has been paid, display a message of "Thank You, have a nice day"

        # - Once paid, display message "Thank you, have a nice day!"
        if self.currentTicket['paid'] == True:
            print('Thank you. Have a nice day!')
        #This will match the syntax for takeTicket, but + 1
        # - Update tickets list to increase by 1 (meaning add to the tickets list)
            self.tickets = len(tickets) + 1   
        # - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
            self.parkingSpaces = len(parkingSpaces) + 1
        else:
        # - If the ticket has not been paid, display an input prompt for payment

        # - SHOULD THIS JUST CALL THE PREVIOUS METHOD (payForParking)??

new_ticket = ParkingGarage([], [], {})


# Do I need to create a function to run it? Yeah, probably
def run():
    while True:
        response = input('Welcome. Do you want to take a ticket or pay for your stay? Enter: take / pay')
        if response.lower() == "take":
            takeTicket()
            print("Your ticket is printing. Make sure to hold on to it to exit the garage.")
            break
        elif response.lower() == "pay":
            payForParking()
            leaveGarage()

run()