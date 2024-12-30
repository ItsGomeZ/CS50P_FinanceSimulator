# Finance Simulator

## Overview

The Finance Simulator project is designed to help users simulate different financial scenarios using basic concepts of compound interest and savings plans. This program allows users to input values such as principal amount, interest rate, time period, and number of compoundings per year to calculate various financial outcomes. The program includes the following functionalities:

1. **Calculate compound interest**: Given an initial amount, interest rate, time, and frequency of compounding, the program calculates the final amount and the interest earned.
2. **Create a savings plan**: The program helps users calculate how much they will accumulate over time by saving a fixed amount monthly, considering the interest rate.
3. **Simulate an investment**: The program simulates different investment scenarios using low and high interest rates to show how investments grow over time.

Each of these calculations provides the user with a clear idea of how their money will grow based on their inputs.

## Mathematical formulas

The formulas used in the program are detailed below.

### Calculate Compound Interest (calculate_compound_interest)

The compound interest formula is:

$$
A = P \times \left( 1 + \frac{r}{n} \right)^{nt}
$$

Where:
- $A$ is the final amount after $t$ years.
- $P$ is the principal (initial capital).
- $r$ is the annual interest rate (in decimal form).
- $n$ is the number of times the interest is compounded per year.
- $t$ is the time in years.

The interest earned is:

$$
I = A - P
$$

### Create a Savings Plan (create_savings_plan)

The formula for calculating the future value of a savings plan is:

$$
FV = P \times \frac{\left( 1 + \frac{r}{12} \right)^N - 1}{\frac{r}{12}}
$$

Where:
- $FV$ is the future value of the savings.
- $P$ is the monthly savings amount.
- $r$ is the annual interest rate (in decimal form).
- $N$ is the total number of months, calculated as $N = t \times 12$.

If the interest rate is zero, the formula simplifies to:

$$
FV = P \times N
$$

### Simulate an Investment (simulate_investment)

The formula for simulating an investment is:

$$
FV = P \times \left( 1 + r \right)^t
$$

Where:
- $FV$ is the future value of the investment.
- $P$ is the principal (initial capital).
- $r$ is the annual interest rate (in decimal form).
- $t$ is the time in years.

The investment can be simulated with both a low interest rate ($r_{low}$) and a high interest rate ($r_{high}$) to show different scenarios:

- With a low interest rate:

$$
FV_{low} = P \times \left( 1 + r_{low} \right)^t
$$

- With a high interest rate:

$$
FV_{high} = P \times \left( 1 + r_{high} \right)^t
$$


## Files

### `project.py`

This file contains the core logic of the program. It includes three main functions:

- **`main()`**: This is the entry point of the program. It prompts the user with options to calculate compound interest, create a savings plan, or simulate an investment. Based on the user’s choice, it calls the corresponding function.
- **`calculate_compound_interest(principal, rate, time, n)`**: This function calculates the compound interest based on the formula for compound interest. It returns the final amount and the interest earned.
- **`create_savings_plan(monthly_savings, rate, time)`**: This function calculates how much money you will accumulate based on monthly savings, an annual interest rate, and the time period. It uses a closed-form formula for future value.
- **`simulate_investment(principal, rate_low, rate_high, time)`**: This function simulates an investment by considering two different interest rates (low and high) over a specified time period. It calculates the future value for both scenarios.

The program provides an interactive experience for the user by continuously asking for input until the user decides to exit.

### `test_project.py`

This file contains unit tests for the functions in `project.py`. It uses the `pytest` framework to ensure that the functions return correct and expected results. The tests cover the following:

- **`test_calculate_compound_interest()`**: Tests the `calculate_compound_interest` function by providing sample values for principal, interest rate, time, and number of compoundings. It asserts that the returned results match the expected values.
- **`test_create_savings_plan()`**: Tests the `create_savings_plan` function with different values of monthly savings, interest rates, and time periods. It checks whether the returned future value is accurate.
- **`test_simulate_investment()`**: Tests the `simulate_investment` function by simulating investment scenarios with different interest rates and time periods. It checks that the future values are computed correctly for both low and high-interest rates.

These tests ensure that the core financial functions work as expected and produce the correct results based on the given input values.

## Design Choices

### Why Interactive Input?

The program is designed to be interactive, allowing users to input values and immediately see the results of their financial calculations. This provides a user-friendly experience, making the simulator easy to use and understand for individuals who may not be familiar with programming.

### Why Use Functions for Each Calculation?

Each financial calculation is encapsulated in a separate function. This modular approach makes the code easier to maintain and test. It also allows for greater flexibility in the future, should additional functionality need to be added (e.g., new types of simulations or calculations).

### Unit Testing

The program includes unit tests to verify that each of the financial functions behaves correctly. This helps ensure the reliability of the code and prevents bugs when changes are made. The tests cover a range of input scenarios, ensuring that edge cases and typical use cases are handled appropriately.

## Conclusion

The Finance Simulator project provides a simple yet powerful tool for understanding basic finance concepts. By simulating compound interest, savings plans, and investment scenarios, the user can make informed decisions about their personal finances. The code is structured for readability and maintainability, and the inclusion of unit tests ensures the accuracy of the calculations.
