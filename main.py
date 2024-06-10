from functions import apply_tax_rates, calculate_chargeable_income, display_results

def main():
    print("Welcome to the Tax Input Program")
    try:
        gross_income = float(input("Enter Your Gross Income: "))
        if gross_income < 0:
            raise ValueError("Gross income cannot be negative.")
    except ValueError as e:
        print(f"Invalid input for gross income: {e}")
        return

    try:
        tax_relief = float(input("Enter Your Total Tax Relief: "))
        if tax_relief < 0:
            raise ValueError("Tax relief cannot be negative.")
    except ValueError as e:
        print(f"Invalid input for tax relief: {e}")
        return

    try:
        tax_rebate = float(input("Enter Applicable Tax Rebate: "))
        if tax_rebate < 0:
            raise ValueError("Tax rebate cannot be negative.")
    except ValueError as e:
        print(f"Invalid input for tax rebate: {e}")
        return

    chargeable_income = calculate_chargeable_income(gross_income, tax_relief)

    if chargeable_income < 0:
        print("Error: Chargeable Income cannot be negative. Please re-enter.")
        return

    tax_due = apply_tax_rates(chargeable_income)

    tax_payable = max(0, tax_due - tax_rebate)

    display_results(tax_payable, chargeable_income, tax_due)

if __name__ == "__main__":
    main()
