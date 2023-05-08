from IPython.display import clear_output
bids={}
bidding_finished=False
def find_highest(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of {highest_bid} ")
            
while not bidding_finished:
    name=input("What is your Name?: ")
    price=int(input("What is your bid?: $"))
    bids[name]=price
    should_continue=input("Enter 'Yes' or 'No':")
    if should_continue=="no" or should_continue=="No":
        bidding_finished=True
        find_highest(bids)
    elif should_continue=="yes":
        clear_output()
        
    
