#Coded by Evan Kale and Ben Onderick


print("Undergraduate Student Loan App ~ Enter loan information.")

# Loan Limit Lists
subLoanLimit = [3500, 4500, 5500, 5500, 5500, 5500]

indepLoanLimit = [9500, 10500, 12500, 12500, 12500, 12500]

depLoanLimit = [5500, 6500, 7500, 7500, 7500, 7500, 7500]

# Debt Payoff Dictionary
debtDict = {
    7499: 10,
    9999: 12,
    19999: 15,
    39999: 20,
    59999: 25,
    float('inf'): 30
}

#Lists tracking different years' numbers
typeStud_list = []
loan_list = []
subRate_list = []
unsubRate_list = []
yearsBool = True
years = 0


#PartA - Gathering loan information
while yearsBool == True:
    years += 1
    typeStud = input("Enter I for Independent or D for Dependent student for this school year: ")
    while typeStud not in ['I', 'D']:
        print("Invalid input. Enter I for Independent or D for Dependent student for this school year: ")

    if typeStud == 'I':
        loanLimit = indepLoanLimit[years-1]
    elif typeStud == 'D':
        loanLimit = depLoanLimit[years-1]
        
    loan = int(input("What is the total loan amount for this school year: "))
    if loan <= 0:
        loan = input("Invalid input. What is the total loan amount for this school year: ")
    if loan > loanLimit:
        loan = ("Invalid input. What is the total loan amount for this school year: ")
        
    subRate = input("What is the subsidized loan interest rate: ")
    while not subRate.isdigit():
        subRate = input("Invalid input. What is the subsidized loan interest rate: ")

    unsubRate = input("What is the unsubsidized loan interest rate: ")
    while not unsubRate.isdigit():
        unsubRate = input("Invalid input. What is the unsubsidized loan interest rate: ")
    
    #adds years info to lists
    loan_list.append(int(loan))
    typeStud_list.append(typeStud)
    subRate_list.append(int(subRate))
    unsubRate_list.append(int(unsubRate))
    
    

    more_years = input("Are you attending another year of undergraduate college Y or N: ")
    while more_years not in ['Y', 'N']:
        more_years = input("Invalid input. Are you attending another year of undergraduate college Y or N: ")

    if more_years == 'N':
        yearsBool == False
        break
    



#Part B - Calculating total owed 6 months after leaving school
loan_interest_list = []
total_loan_amount = 0 
for year in range(years):
    
    #loan_interest = (subLoanLimit[year] * (subRate_list[year] / 100)) + ((loan_list[year] - subLoanLimit[year]) * (unsubRate_list[year] / 100))
    loan_interest = float(((loan_list[year] - subLoanLimit[year]) * (unsubRate_list[year] / 100)))
    loan_interest_list.append(loan_interest)    
    total_loan_amount += sum(loan_interest_list)


total_loan_amount_plus_six = total_loan_amount + (sum(loan_interest_list) / 2) + sum(loan_list) 
total_owed_format = "${:,.2f}".format(total_loan_amount_plus_six)
print("Total owed after 6 months of leaving college is " + total_owed_format)               


#Part C

#Finding weighted interest rates
sum_subRate_times_loan = 0
sum_unsubRate_times_loan = 0
for year in range(years):
    sum_subRate_times_loan += ((subRate_list[year] / 100) * loan_list[year])
    sum_unsubRate_times_loan += ((unsubRate_list[year] / 100) * loan_list[year])
    sub_weighted = sum_subRate_times_loan / sum(loan_list)
    unsub_weighted = sum_unsubRate_times_loan / sum(loan_list)

#Finding consolidated interest rate
Consolidated_Interest_Rate_Two = ((sub_weighted + unsub_weighted) / 2) * 100
#print("consol2:", Consolidated_Interest_Rate_Two)


#Finding total loan term using debDict
for loanBracket, payoffYears in debtDict.items():
    if total_loan_amount_plus_six <= loanBracket:
        years_to_payoff = payoffYears
        break

#Calculating monthly payment
monthly_payment = float((total_loan_amount_plus_six / years_to_payoff) / 12)
r = Consolidated_Interest_Rate_Two / (12 * 100)
n = years_to_payoff * 12
monthly_payment = (r * total_loan_amount_plus_six) / (1 - (1 + r) ** (-n))

#Calculating total amount paid and total interest paid
total_paid_real = (monthly_payment * (payoffYears * 12))
total_paid_interest = total_paid_real - total_loan_amount_plus_six

#Print statements
print("Consolidated interest rate: {:.2f}%".format(Consolidated_Interest_Rate_Two))
print("Monthly payment after consolidation: $" + str(round(monthly_payment, 2)))
print("Loan payments continue for this many years:", years_to_payoff)
print("Total interest paid on school loans: $" + str(round(total_paid_interest, 2)))
print("Total paid loans plus interest: $" + str(round(total_paid_real, 2)))




#Writing results to file named "results.txt"
with open("results.txt", "w") as file:
    file.write("Total owed after 6 months of leaving college is " + total_owed_format + "\n")
    file.write("Consolidated interest rate: {:.2f}%\n".format(Consolidated_Interest_Rate_Two))
    file.write("Monthly payment after consolidation: $" + str(round(monthly_payment, 2)) + "\n")
    file.write("Loan payments continue for this many years: " + str(years_to_payoff) + "\n")
    file.write("Total interest paid on school loans: $" + str(round(total_paid_interest, 2)) + "\n")
    file.write("Total paid loans plus interest: $" + str(round(total_paid_real, 2)) + "\n")
    




        



