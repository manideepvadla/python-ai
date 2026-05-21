employees = [
    {"name": "John", "salary": 90000, "department": "AI"},
    {"name": "Alice", "salary": 120000, "department": "Platform"},
    {"name": "Bob", "salary": 110000, "department": "AI"},
    {"name": "Sara", "salary": 95000, "department": "Platform"},
    {"name": "Mia", "salary": 105000, "department": "AI"},
]

projects = [
    {"name": "AI Dashboard", "status": "Completed", "bugs": 4, "priority": 2},
    {"name": "RAG Chatbot", "status": "In Progress", "bugs": 9, "priority": 1},
    {"name": "Metrics API", "status": "Completed", "bugs": 2, "priority": 3},
    {"name": "Auth Service", "status": "In Progress", "bugs": 9, "priority": 1},
    {"name": "Billing UI", "status": "Blocked", "bugs": 1, "priority": 2},
]

orders = [
    {"id": 101, "customer": "Acme", "amount": 250, "paid": True},
    {"id": 102, "customer": "Beta", "amount": 80, "paid": False},
    {"id": 103, "customer": "Gamma", "amount": 420, "paid": True},
    {"id": 104, "customer": "Delta", "amount": 150, "paid": True},
    {"id": 105, "customer": "Echo", "amount": 95, "paid": False},
]


#1 Print every employee’s name, one per line.
names = [e["name"] for e in employees]
for name in names:
    print(name)

#Build a list of names for employees in one department of your choice (you pick the department string).
platform_employees = [e["name"] for e in employees if e["department"] == "Platform"]
print(platform_employees)

#Build a list of employees whose salary is above a threshold you choose. Print that list.
salary_above_threshold = [e for e in employees if e["salary"] > 100000]
print(salary_above_threshold)

#Print the name of the employee with the highest salary (use max and key).
max_salary_employee = max(employees, key= lambda employee: employee["salary"])
print(max_salary_employee["name"])

#Print names sorted by salary, highest first (do not mutate the original list).
sorted_employees = sorted(employees, key= lambda employee: employee["salary"], reverse=True)
print([employee["name"] for employee in sorted_employees])

#Write def employee_names(employees): that returns a list of all names (no printing inside the function). Call it and print the result.
def employee_names(employees):
    return [e["name"] for e in employees]

print(employee_names(employees))


#Write def in_department(employees, dept): that returns a list of names in that department. Test with two different department strings.
def in_department(employees, dept):
    return [e["name"] for e in employees if e["department"] == dept]

print(in_department(employees, "AI"))
print(in_department(employees, "Platform"))

#Write def highest_paid(employees): that returns the name (string) of the highest-paid employee.
def highest_paid(employees):
    return max(employees, key = lambda employee: employee["salary"])["name"]

print(highest_paid(employees))

#Write def salary_band(salary): that returns "junior", "mid", or "senior" using your own salary cutoffs (document the cutoffs in a comment). Loop your employees and print "Name: band" for each.
def salary_band(salary):
    if(salary<100000):
        return "junior"
    elif(salary<120000):
        return "mid"
    else:
        return "senior"

for employee in employees:
    print(f"{employee["name"]}: {salary_band(employee["salary"])}")


#Without a function: print total amount of all orders.
total_amount = sum(order['amount'] for order in orders)
print(total_amount)

#Write def total_paid(orders): that returns the sum of amount only for orders where paid is True.
def total_paid(orders):
    return sum(order["amount"] for order in orders if order["paid"])

print(total_paid(orders))

#Write def unpaid_ids(orders): that returns a list of order ids where paid is False.
def unpaid_ids(orders):
    return [order["id"] for order in orders if not order["paid"]]

print(unpaid_ids(orders))

def largest_order_customer(orders):
    return max(orders, key=lambda order:order["amount"])["customer"]

print(largest_order_customer(orders))


#def top_n_by_salary(employees, n=3): — return list of names for top n salaries (highest first). Call with default n, then with n=2.
def top_n_by_salary(employees, n=3):
    sorted_employee_list= sorted(employees, key = lambda employee: employee["salary"], reverse=True)
    return [employee["name"] for employee in sorted_employee_list][:n]

print(top_n_by_salary(employees))
print(top_n_by_salary(employees, 2))


def order_summary(orders):
       return {"total": sum(order["amount"] for order in orders), "paid_total": sum(order["amount"] for order in orders if order["paid"]), "unpaid_count": len([order for order in orders if not order["paid"]]) } 

print(order_summary(orders))


def highest_paid_safe(employees):
       if len(employees) == 0:
           return None
       else:
            return max(employees, key =lambda employee: employee["salary"])["name"]

print(highest_paid_safe(employees))
print(highest_paid_safe([]))