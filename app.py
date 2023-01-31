import sys, csv

def get_total_spend_points(arg):
    # Check if arg can be converted to integer. Otherwise throw exception.
    try: 
        total_points_to_spend = int(arg)
        return total_points_to_spend
    except ValueError as _:
        exit()

def read_csv(filename):
   #Reads the csv file. If not possible, throws IOError 
    transactions = []
    try: 
        with open(filename, newline='') as csvfile:
            separater = csv.reader(csvfile, delimiter=',')
            for i, rowVal in enumerate(separater):
                if i != 0: 
                    transactions.append(rowVal)

        transactions.sort(key=lambda x: x[2]) #Sort by the second value to get earliest date
        return transactions
    except IOError as error_message:
        print(error_message)
        exit()

def spend_point(total_points_to_spend, transactions):
    # This function calculates spending points based on the instruction spending rules.  
    if (not total_points_to_spend or not transactions):
        print("Check input again.")
        exit()

    accounts = {}
    curr_date = transactions[0][2][:10] #Gets the date using the timestamp column until the 10th char
    #Iterate through transctions that is sorted based on timestamp
    for transaction in transactions:
        payer, points, timestamp = transaction
        points = int(points)
        if payer not in accounts: accounts[payer] = points
        else: accounts[payer] += points
        #If date changed, apply spending rules 
        if curr_date != timestamp[:10]:
            #iterate through user accounts 
            for curr_payer, curr_balance in accounts.items():
                # If user's balance is less than total_points_to_spend, update balance and total_points_to_spend
                # Also handles when payer's point is negative
                if curr_balance < total_points_to_spend:
                    accounts[curr_payer] = 0
                    total_points_to_spend -= curr_balance
                #Otherwise, update balance and total_points
                else: 
                    accounts[curr_payer] = curr_balance - total_points_to_spend
                    total_points_to_spend = 0
        #Update curr_date 
        curr_date = timestamp[:10]

    return accounts

if __name__ == "__main__":
    arg = sys.argv[1]
    total_points_to_spend = get_total_spend_points(arg)
    transactions = read_csv('transaction.csv')
    accounts = spend_point(total_points_to_spend, transactions)
    print("Accounts are: ", accounts)
