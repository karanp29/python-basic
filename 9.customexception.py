class CustomError(Exception):
    ...
    pass

#---
try:
   ...

except CustomError:
    ...

# -----------------------------------------------
    # define CustomError
class InsufficientBalanceError (Exception):
    ...
    pass

# use custom error
main_balance = 1000
try:
    withdraw_amt = int(input('Enter amount to withdraw'))
    if withdraw_amt > main_balance:
        raise InsufficientBalanceError
    else:
        print('withdrawing money')
except InsufficientBalanceError:
    print("balance not sufficient")