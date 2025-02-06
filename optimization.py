import pulp

# Initialization of the model
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Define variables
Lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
Juice = pulp.LpVariable("Juice", lowBound=0, cat="Integer")

# Add target function
model += Lemonade + Juice, "Profit"

# Add limitations
model += 2 * Lemonade + Juice <= 100, "Water"
model += Lemonade <= 50, "Sugar"
model += Lemonade <= 30, "Lemon juice"
model += 2 * Juice <= 40, "Fruit"

# Solve model
model.solve()

# Print results
print(f"Amount of Lemonade: {Lemonade.varValue}")
print(F"Amount of Juice: {Juice.varValue}")