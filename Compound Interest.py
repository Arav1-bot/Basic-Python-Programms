def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

print("Compound Interest (P=1000, R=5%, T=2 years):", compound_interest(1000, 5, 2))
