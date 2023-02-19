print()
def main():
    start_miles = int(input('Enter the first odometer reading (in miles): '))
    end_miles = int(input('Enter the second odometer reading (in miles): '))
    amount_in_gallons = float(input('Enter the amount of fuel used (in gallons): '))
    mpg = miles_per_gallon(start_miles, end_miles, amount_in_gallons)
    fn_lp100k = lp100k_from_mpg(mpg)
    mpg = round(mpg, 1)
    fn_lp100k = round(fn_lp100k, 2)
    print(f"{mpg} miles per gallon\n{fn_lp100k} litres per 100 km")

def miles_per_gallon(start_miles, end_miles, amount_in_gallons):
    gallon = (end_miles - start_miles) / amount_in_gallons
    return gallon

def lp100k_from_mpg(mpg):
    km = 235.215 / mpg
    return km

main()
print()