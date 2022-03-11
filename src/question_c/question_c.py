def get_bonus_pay_amount(sales):
    if ((sales >= 0) and (sales < 500)):
        return sales * .05
    elif ((sales >= 500) and (sales < 1000)):
        return sales * .06
    elif ((sales >= 1000) and (sales < 1500)):
        return sales * .07
    elif ((sales >= 1500) and (sales < 2000)):
        return sales * .08
    else:
        return 'Invalid argument'