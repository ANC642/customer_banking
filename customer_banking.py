# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
dahses = "*" * 40
print(dahses)
dash = "-" * 40
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("What is your total savings? $ "))
    savings_interest = float(input("Saving account interest rate? "))
    savings_maturity = int(input("How many months have you had your saving account? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(dash)
    print(f"Your updated savings for the month is: {updated_savings_balance: ,.2f}")
    print(f"Your total interested earned for the month is: {interest_earned: ,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print(dahses)
    cd_balance = float(input("Enter CD Account balance: $"))
    cd_interest = float(input("Enter CD Intereset rate: "))
    cd_maturity = int(input("Enter Maturity length for CD: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(dash)
    print(f"Your updated CD Account balance is:${updated_cd_balance: ,.2f}, and Interested earned for the month is ${interest_earned: ,.2f}")
if __name__ == "__main__":
    # Call the main function.
    main()
