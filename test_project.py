from project import calculate_compound_interest, create_savings_plan, simulate_investment

# Test for calculate_compound_interest()
def test_calculate_compound_interest():
    # Initial principal 1000€, interest rate 5%, 3 years, capitalization 4 times/year
    amount, interest = calculate_compound_interest(1000, 0.05, 3, 4)
    assert round(amount, 2) == 1160.75
    assert round(interest, 2) == 160.75

    # Initial principal 1000€, interest rate 5%, 3 years, capitalization 4 times/year
    amount, interest = calculate_compound_interest(2000, 0.03, 5, 12)
    assert round(amount, 2) == 2323.23
    assert round(interest, 2) == 323.23

# Test for create_savings_plan()
def test_create_savings_plan():
    assert round(create_savings_plan(100, 0.06, 2), 2) == 2543.20  # Monthly savings 100€, interest rate 6%, 2 years
    assert round(create_savings_plan(200, 0.05, 5), 2) == 13601.22  # Monthly savings 200€, interest rate 5%, 5 years
    assert round(create_savings_plan(150, 0, 3), 2) == 5400.00  # Monthly savings 150€, interest rate 0%, 3 years (interest-free)

# Test for simulate_investment()
def test_simulate_investment():
    # Initial principal 5000€, low interest rate 3%, high interest rate 7%, 5 years
    low_result, high_result = simulate_investment(5000, 0.03, 0.07, 5)
    assert round(low_result, 2) == 5796.37
    assert round(high_result, 2) == 7012.76

    # Initial principal 1000€, low interest rate 2%, high interest rate 5%, 10 years
    low_result, high_result = simulate_investment(1000, 0.02, 0.05, 10)
    assert round(low_result, 2) == 1218.99
    assert round(high_result, 2) == 1628.89
