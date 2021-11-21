# Author: Gabriel Henderson
# Due Date: 22 August 2021
# Description: Calculate retirement age and what year and month that will end on

def main():
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    birth_year = input("Enter your year of birth or leave blank to exit: ")

    while birth_year:
        birth_month = int(input("Enter your month of birth: "))

        retirement_year, retirement_month = full_retirement_age_calc(int(birth_year))
        final_year, final_month = calculate_final_year(int(birth_year), birth_month, retirement_year, retirement_month)

        print(f"""Your full retirement age is {retirement_year} years and {retirement_month} months""")
        print(f"""This will be in {months[final_month]} of {final_year}\n""")

        birth_year = input("Enter your year of birth or leave blank to exit: ")

    exit(0)


def full_retirement_age_calc(birth_year: int):
    # Based on the retirement age chart at https://www.ssa.gov/benefits/retirement/planner/agereduction.html
    full_retirement_age_months = 0

    if birth_year <= 1937:
        full_retirement_age_months = 780
    elif 1937 < birth_year <= 1943:
        # each year after 1937 and before 1944 just adds 2 months each year
        full_retirement_age_months = 780 + ((birth_year - 1937) * 2)
    elif 1943 < birth_year <= 1954:
        full_retirement_age_months = 792
    elif 1954 < birth_year <= 1960:
        # each year after 1954 and before 1961 just adds 2 months each year
        full_retirement_age_months = 792 + ((birth_year - 1954) * 2)
    else:
        full_retirement_age_months = 804

    return int(full_retirement_age_months / 12), full_retirement_age_months % 12


def calculate_final_year(birth_year: int, birth_month: int, retirement_year: int, retirement_month: int):
    if birth_month + retirement_month > 12:
        final_year = birth_year + retirement_year + 1
        final_month = (birth_month + retirement_month) - 12
        return final_year, final_month

    final_year = birth_year + retirement_year
    final_month = (birth_month + retirement_month)
    return final_year, final_month


if __name__ == '__main__':
    main()
