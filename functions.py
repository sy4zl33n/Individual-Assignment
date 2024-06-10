def calculate_chargeable_income(gross_income, tax_relief):
    # Calculate chargeable income ensuring it is non-negative
    a = max(0, gross_income - tax_relief)
    return a

def apply_tax_rates(a):
    categories = [
        (5000, 0, 0),         # Up to RM 5,000
        (20000, 150, 1),      # RM 5,001 to RM 20,000
        (35000, 600, 3),      # RM 20,001 to RM 35,000
        (50000, 1500, 6),     # RM 35,001 to RM 50,000
        (70000, 3700, 11),    # RM 50,001 to RM 70,000
        (100000, 9400, 19),   # RM 70,001 to RM 100,000
        (400000, 84000, 25),  # RM 100,001 to RM 400,000
        (600000, 184400, 26), # RM 400,001 to RM 600,000
        (2000000, 528400, 28),# RM 600,001 to RM 2,000,000
        (float('inf'), 528400, 30)  # Above RM 2,000,000
    ]

    tax_due = 0
    previous_limit = 0

    for limit, default_tax, rate in categories:
        if a > previous_limit:
            if a <= limit:
                tax_due += (a - previous_limit) * (rate / 100)
                break
            else:
                tax_due += (limit - previous_limit) * (rate / 100)
        previous_limit = limit

    return tax_due

def display_results(tax_payable, chargeable_income, tax_due):
    # Display the results
    print(f"Chargeable Income: RM {chargeable_income:.2f}")
    print(f"Tax Due: RM {tax_due:.2f}")
    print(f"Tax Payable: RM {tax_payable:.2f}")
