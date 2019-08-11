import os
import csv

csvpath = 'Resources/election_data.csv'

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    total_votes = 0
    count_khan = 0
    count_correy = 0
    count_li = 0
    count_otooley = 0
    candidates = []

    for row in csvreader:
        total_votes+=1
        
        if row[2] not in candidates: 
            candidates.append(row[2]) 
        #print(candidates)

        if row[2] == "Khan":
            count_khan+=1
        if row[2] == "Correy" :
            count_correy+=1
        if row[2] == "Li":
            count_li+=1
        if row[2] == "O'Tooley":
            count_otooley+=1

        percentage_khan = (count_khan/total_votes) *100
        percentage_correy = (count_correy/total_votes) *100
        percentage_li = (count_li/total_votes) *100
        percentage_otooley = (count_otooley/total_votes) *100
    
    print(f'Khan: {percentage_khan: .3f}% ({count_khan})')
    print(f'Correy: {percentage_correy: .3f}% ({count_correy})')
    print(f'Li: {percentage_li: .3f}% ({count_li})')
    print(f"O'Tooley: {percentage_otooley: .3f}% ({count_otooley})")
        

    if count_khan > count_correy and count_li and count_otooley:
        print(f'Winner: Khan')
    elif count_correy > count_khan and count_li and count_otooley:
        print(f'Winner: Correy')
    elif count_li > count_khan and count_correy and count_otooley:
        print(f'Winner: Li')
    else:
        print(f"Winner; O'Tooley")

                    
            







    
    



    

    





