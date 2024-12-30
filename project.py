def main():
    print("\nWelcome to the Finance Simulator\n")
    while True:
        print("Options:")
        print("1. Calculate compound interest")
        print("2. Create a savings plan")
        print("3. Simulate an investment")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == "1":
            principal = float(input("Initial principal (in euros): "))
            rate = float(input("Annual interest rate (in %): ")) / 100
            time = int(input("Time (in years): "))
            n = int(input("Number of times interest is compounded per year: "))
            amount, interest = calculate_compound_interest(principal, rate, time, n)

            print(f"\nFinal amount after {time} years: {amount:.2f} euros")
            print(f"Interest earned: {interest:.2f} euros\n")
        elif choice == "2":
            monthly_savings = float(input("Monthly savings (in euros): "))
            rate = float(input("Annual interest rate (in %): ")) / 100
            time = int(input("Time (in years): "))
            future_value = create_savings_plan(monthly_savings, rate, time)

            print(f"\nFuture value after {time} years: {future_value:.2f} euros\n")
        elif choice == "3":
            principal = float(input("Initial principal (in euros): "))
            rate_low = float(input("Minimum annual interest rate (in %): ")) / 100
            rate_high = float(input("Maximum annual interest rate (in %): ")) / 100
            time = int(input("Time (in years): "))
            low_result, high_result = simulate_investment(principal, rate_low, rate_high, time)

            print("\nResults of the simulation:")
            print(f"At a low rate of {rate_low * 100:.2f}%: {low_result:.2f} euros")
            print(f"At a low rate of {rate_high * 100:.2f}%: {high_result:.2f} euros\n")
        elif choice == "4":
            print("\nThank you for using the Finance Simulator, see you soon!")
            break
        else:
            print("Invalid option. Try again.\n")

def calculate_compound_interest(principal, rate, time, n):
    """Calculates compound interest based on initial principal, rate, and time."""
    amount = principal * (1 + rate / n) ** (n * time)
    interest = amount - principal
    return amount, interest  # Devuelve los valores calculados

def create_savings_plan(monthly_savings, rate, time):
    """Calculates how much you will save with regular contributions using a closed formula."""
    total_months = time * 12
    monthly_rate = rate / 12

    if monthly_rate > 0:
        future_value = monthly_savings * ((1 + monthly_rate) ** total_months - 1) / monthly_rate
    else:
        # Special case: interest-free
        future_value = monthly_savings * total_months

    return future_value

def simulate_investment(principal, rate_low, rate_high, time):
    """Simulates an investment with different scenarios."""
    low_result = principal * (1 + rate_low) ** time
    high_result = principal * (1 + rate_high) ** time
    return low_result, high_result

if __name__ == "__main__":
    main()
