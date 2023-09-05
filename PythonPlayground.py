#Problem Solving With Python

import csv

def read_stonks(stockfile):
    with open(stockfile, "r"):
        lines = csv.read(stockfile)
        microlist = []
        applelist = []
        ibmlist = []
        masterlist = []
        for name, price, date in lines:
            masterlist.append((int(price), date)) 
            if name == "MSFT":
                microlist.append((int(price), date))
            elif name == "APPL":
                applelist.append((int(price), date))
            elif name == "IBM":
                ibmlist.append((int(price), date))
            else:
                pass
    return (microlist, applelist, ibmlist, masterlist)

def find_info(mylist):
    maxi = None 
    maxidate = None
    mini = None
    minidate = None
    total = 0
    count = 0
    for datatup in mylist:
         price, date = datatup
         if price > maxi:
               maxi = price
               maxidate = date
         if price < mini:
              mini = price
              minidate = date
         count += 1
         total += price
    average = total/count
    return [maxi, maxidate, mini, minidate, average] 

def determine_winner(data):
    micro_data, apple_data, ibm_data, master_data = data

    microsoft_stats = find_info(microlist)
    apple_stats = find_info(applelist)
    ibm_stats = find_info(ibmlist) 
    everyone_stats = find_info(masterlist)

    #block to determine winner
    max_winner = None
    min_winner = None
    
    if everyone_stats[0] in microsoft_stats:
        max_winner = "Microsoft"
    elif everyone_stats[0] in apple_stats:
        max_winner = "Apple"
    elif everyone_stats[0] in ibm_stats:
       max_winner = "IBM"
    else:
        pass

    if everyone_stats[2] in microsoft_stats:
        min_winner = "Microsoft"
    elif everyone_stats[2] in apple_stats:
        min_winner = "Apple"
    elif everyone_stats[2] in ibm_stats:
       min_winner = "IBM"
    else:
        pass
    
    total_winners = [max_winner, everyone_stats[0], everyone_stats[1]]
    total_losers = [min_winner, everyone_stats[2], everyone_stats[3]]
    
    return (microsoft_stats, apple_stats, ibm_stats, total_winners, total_losers)

#block to write to the new file
def write_conclusion(winners, output_file):
    mstat, astat, istat, weiners, loosers = winners
    with open(output_file, "w"):
        output_file.write(f"""Here are the results of the stocks: 

Microsoft's highest price was {mstat[0]}, which occurred on {mstat[1]}. 
Their lowest was {mstat[2]}, which occurred on {mstat[3]}. 
Their average price is {mstat[4]}. 

Apple's highest price was {astat[0]}, which occurred on {astat[1]}. 
Their lowest was {astat[2]}, which occurred on {astat[3]}. 
Their average price is {astat[4]}. 

IBM's highest price was {istat[0]}, which occurred on {istat[1]}. 
Their lowest was {istat[2]}, which occurred on {istat[3]}. 
Their average price is {istat[4]}. 

The company with the highest price was {wieners[0]}, with a price of {wieners[1]} on {wieners[2]}.
The company with the lowest price was {loosers[0]},  with a price of {loosers[1]} on {loosers[2]}.
""")

write_conclusion(determine_winner(read_stonks("_.csv")), "stock_summary.txt")
