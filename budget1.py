'''
This file determines the monthly expenses of a user
It breaks down the types of expenses: total, static and dynamic
It determines how much money should be left for the user to save

Will eventually provide advice for user as to how to save money using certain vehicles, such as:
Bank savings account
CDs
Mutual Funds
401K
Refiancing a house
stocks*
Real Estate
Life Insurance
'''


class GetUserInfo():
    def __init__(self, username, password, gender, DOB):
        self.username = username
        self.password = password
        self.gender = gender
        self.DOB = DOB

    def welcome_user(self):
        print "Welcome to InvestmentDNA, %s! " % self.username + \
              "Let's get started on your balanced budget so you can save money!"

    def user_password(self):
        print "Your user password is %s" % self.password

    def user_gender_DOB(self):
        print "Your gender and DOB are %s " % self.gender + "and %s" % self.DOB

#test case: Instance of user and user properties
Autumn = GetUserInfo("Bumpie", "BigBumps", "F", "06282016")

Autumn.welcome_user()

class Expenses():
    def __init__(self, mortgage, carNote, daycare, food, bills, medical,
                 car_insurance, memberships, cellphone, vonage, comcast):
        self.mortgage = mortgage
        self.carNote = carNote
        self.daycare = daycare
        self.food = food
        self.bills = bills
        self.medical = medical
        self.car_insurance = car_insurance
        self.memberships = memberships
        self.cellphone = cellphone
        self.vonage = vonage
        self.comcast = comcast

    #Total expense for the month
    def add_total_expenses(self):
        total = float(self.mortgage + self.carNote + self.daycare + self.food
             + self.bills + self.medical + self.car_insurance
             + self.memberships + self.cellphone
             + self.vonage + self.comcast)
        print "Here is the overall total of your monthly expenses: "
        print total

        #Savings: added error message to ensure values are floats
        while True:
                try:
                    paycheck = float(input("How much money do you receive after tax per month?: "))
                except ValueError:
                    print("Sorry, I didn't understand that. Please enter a numeric value.")
                    continue

                if paycheck < 0:
                    print("Please enter positive numbers only!")
                    continue
                else:
                    return paycheck

                    savings = (paycheck - total)
                    print "Here is the amount of money you've saved this month: "
                    return savings

    #Total of mortgage, carnote, daycare
    def add_static_expenses(self):
        static = (self.mortgage + self.carNote + self.daycare)
        print "Here is the total of your monthly static expenses: "
        print static

    #Total of everything else
    def add_dynamic_expenses(self):
        dynamic = (self.food + self.bills + self.medical + self.car_insurance + self.memberships
                   + self.cellphone + self.vonage + self.comcast)
        print "Here is the total of your monthly dynamic expenses: "
        print dynamic

    # Need a try/except statement to make sure a positive number has been entered;
    # and it nothing entered, assume amount is zero
    def get_non_negative_int(prompt):
        while True:
            try:
                value = float(raw_input(prompt))
            except ValueError:
                print("Sorry, I didn't understand that. Please enter a numeric value.")
                continue

            if value < 0:
                print("Please enter positive numbers only!")
                continue
            else:
                return value

    Autumn.mortgage = get_non_negative_int("Please enter the mortgage amount: ")
    Autumn.carNote = get_non_negative_int("Please enter the car note amount: ")
    Autumn.daycare = get_non_negative_int("Please enter the daycare amount: ")
    Autumn.food = get_non_negative_int("Please enter the food amount: ")
    Autumn.bills = get_non_negative_int("Please enter the bills amount: ")
    Autumn.medical = get_non_negative_int("Please enter the medical cost amount: ")
    Autumn.car_insurance = get_non_negative_int("Please enter the car insurance amount: ")
    Autumn.memberships = get_non_negative_int("Please enter the memberships amount: ")
    Autumn.cellphone = get_non_negative_int("Please enter the cellphone amount: ")
    Autumn.vonage = get_non_negative_int("Please enter the vonage amount: ")
    Autumn.comcast = get_non_negative_int("Please enter the comcast amount: ")


#test case: Calling the function 'Expenses' - Instance capturing user input.
Autumn = Expenses(Autumn.mortgage, Autumn.carNote, Autumn.daycare,
                    Autumn.food, Autumn.bills, Autumn.medical, Autumn.car_insurance,
                    Autumn.memberships, Autumn.cellphone, Autumn.vonage, Autumn.comcast)

#Returns totals
Autumn.add_total_expenses()
Autumn.add_static_expenses()
Autumn.add_dynamic_expenses()

#Playing with the savings
#class investMe():
 #   def
