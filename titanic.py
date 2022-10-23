import csv

from passenger import Passenger

from cs50 import get_string



def get_passengers():
    with open('titanic.csv', mode='r') as csv_file:
        next (csv_file)
        csv_reader = csv.reader(csv_file)
        passengers = []
        for row in csv_reader:
            
            p = Passenger(row[2], row[3], row[4])
            passengers.append(p)
            
        return passengers

def print_passengers(passengers, count=20):
    i = 0
    for p in passengers:
        i += 1
        print(p)
        if i > count:
            break
            
def proccess_query(query):
    token_list = query.upper().split()
    if len(token_list) < 2:
        print("Invalid command")
        return
    
    if token_list[0] not in ['LIST', 'COUNT']:
        print("Invalid command")
        return
    
    if token_list[1] not in ['PASSENGERS']:
        print("Invalid command")
        return
    
    if token_list[0] == 'LIST' and token_list[1] == 'PASSENGERS':
        print_passengers(passengers)
        
    elif token_list[0] == 'COUNT' and token_list[1] == 'PASSENGERS':
        print(f"Total {len(passengers)} passengers")
        
def main():
    #this is your main program that interacts with the user.
    welcomeMessage = """Welcome to Titanic Info Database.\nWhat would you like to know about the Titanic passengers?
    You can use my Titanic++ language to query against the dataset.
    For ex: 'List Passengers' would list all the passengers.
    'Count Passengers' would display the count of passengers.
    """
    print(welcomeMessage)
    
    global passengers
    passengers = get_passengers()
    
main()          
        
while True:        
    query = get_string("Titanic++>")
    if query == "exit":
        print("Thank you for using Titanic++.")
        break
    
    proccess_query(query)
    print()