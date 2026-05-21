
employees = [
    {"name": "John", "salary": 90000, "department": "AI"},
    {"name": "Alice", "salary": 120000, "department": "Platform"},
    {"name": "Bob", "salary": 110000, "department": "AI"},
    {"name": "Sara", "salary": 95000, "department": "Platform"},
    {"name": "Mia", "salary": 105000, "department": "AI"},
]

api_response = {
    "status": "ok",
    "data": [
        {"product": "Laptop", "price": 1200, "stock": 5},
        {"product": "Mouse", "price": 25, "stock": 0},
        {"product": "Keyboard", "price": 80, "stock": 12},
        {"product": "Monitor", "price": 300, "stock": 3},
    ]
}
users_response = {
    "users": [
        {"name": "Ana", "roles": ["admin", "editor"], "active": True},
        {"name": "Ben", "roles": ["viewer"], "active": False},
        {"name": "Cara", "roles": ["admin", "viewer"], "active": True},
        {"name": "Dan", "roles": ["editor"], "active": True},
    ]
}

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

#Build a list of names for employees in the AI department only.
ai_employess = [e["name"] for e in employees if e["department"] == "AI"]
print(ai_employess)

#Build a list of all salaries.
salaries = [e["salary"] for e in employees]
print(salaries)

#Build a list of full employee records (dicts) where salary is greater than 100000.
employees_with_salary_greater_than_100000 = [e for e in employees if e["salary"] > 100000]
print(employees_with_salary_greater_than_100000)

#Which employee has the highest salary? Print their name.
highest_salary_employee = max(employees, key=lambda employee: employee["salary"])
print(highest_salary_employee["name"])

#Which employee has the lowest salary? Print their name.
lowest_salary_employee = min(employees, key=lambda employee: employee["salary"])
print(lowest_salary_employee["name"])

#Build a list of strings in the form "Name earns X" for every employee.
employee_strings = [f"{e['name']} earns {e['salary']}" for e in employees]
print(employee_strings)

#How many employees work in Platform?
platform_employees = [e for e in employees if e["department"] == "Platform"]
print(len(platform_employees))

#Sort employees from highest to lowest salary. Print only their names in that order.
sorted_employees = sorted(employees, key=lambda employee: employee["salary"], reverse=True)
print(sorted_employees)

numbers = [3, 7, 2, 9, 14, 5, 8, 1, 10, 6]

#Build a list of each number squared.
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

#Build a list of only even numbers.
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

#Build a list of numbers greater than 7.
odd_numbers = [n for n in numbers if n > 7]
print(odd_numbers)

#Sum of all numbers
sum_of_numbers = sum(numbers)
print(sum_of_numbers)

#What is the largest number in the list?
largest_number = max(numbers)
print(largest_number)

#What is the smallest number in the list?
smallest_number = min(numbers)
print(smallest_number)

#Build a list of numbers that are both even and greater than 5.
even_numbers_greater_than_5 = [n for n in numbers if n % 2 == 0 and n > 5]
print(even_numbers_greater_than_5)

#Sort the numbers from smallest to largest (do not change the original list unless you intend to).
sorted_numbers = sorted(numbers)
print(sorted_numbers)

#How many numbers are greater than 5?
numbers_greater_than_5 = [n for n in numbers if n > 5]
print(len(numbers_greater_than_5))

#Is any number in the list greater than 12? (Answer should be True or False.
any_number_greater_than_12 = any(n for n in numbers if n > 12)
print(any_number_greater_than_12)



#What is the total of all order amounts?
total_amount = sum(order["amount"] for order in orders)
print(total_amount)

#What is the total amount for paid orders only?
paid_total_amount = sum(order["amount"] for order in orders if order["paid"] is True)
print(paid_total_amount)

#Which customer placed the largest order? Print the customer name.
largest_order_customer_name = max(orders, key = lambda order: order["amount"])
print(largest_order_customer_name["customer"])

#Which customer placed the smallest order? Print the customer name.
smallest_order_customer_name = min(orders, key = lambda order: order["amount"])
print(smallest_order_customer_name["customer"])

#Build a list of customer names for orders with amount > 100.
customer_with_amount_more_than_100 = [order["customer"] for order in orders if order["amount"] > 100]
print(customer_with_amount_more_than_100);

#Build a list of order IDs that are not paid.
list_of_order_ids = [order["id"] for order in orders if order["paid"] is False]
print(list_of_order_ids)

#How many orders are unpaid?
unpaid_orders = len([order for order in orders if order["paid"] is False])
print(unpaid_orders)

#Sort orders by amount from low to high. Print customer names in that order.
sorted_orders_list = sorted(orders, key = lambda order: order["amount"], reverse = False)
names_of_sorted = [order["customer"] for order in sorted_orders_list]
print(names_of_sorted)

#What is the average order amount?
total_order_amount = sum(order["amount"] for order in orders)
avg_order_amount = total_order_amount / len(orders)
print(avg_order_amount)

#Are all orders paid? (True or False.)
print(all(order["paid"] for order in orders))



#List all Completed projects (full dicts).
completed_projects = [project for project in projects if project["status"] == "Completed"]
print(completed_projects)

#List names of projects that are In Progress.
projects_in_progress = [project["name"] for project in projects if project["status"] == "In Progress"]
print(projects_in_progress)

#What is the total bug count across all projects?
total_bug_count = sum(project["bugs"] for project in projects)
print(total_bug_count)

#Which project has the most bugs? Print its name.
most_bugs_project = max(projects, key = lambda project: project["bugs"])
print(most_bugs_project["name"])

#Which project has the fewest bugs? Print its name.
min_bugs_project = min(projects, key = lambda project: project["bugs"])
print(min_bugs_project["name"])

#List project names with bugs greater than 5.
projects_with_more_than_5_bugs = [project["name"] for project in projects if project["bugs"] > 5]
print(projects_with_more_than_5_bugs)

#Sort projects by priority (low number = higher priority). Print names in order.
sorted_projects = sorted(projects, key = lambda project: project["priority"])
sorted_project_names = [project["name"] for project in sorted_projects]
print(sorted_project_names)

#Sort projects by bugs from most to least. Print the top 3 names only.
sorted_dec_projects = sorted(projects, key = lambda project: project["bugs"], reverse = True)
sorted_project_names = [project["name"] for project in sorted_dec_projects[:3]]
print(sorted_project_names)

#How many projects are not Completed?
projects_not_completed = len([project for project in projects if project["status"] != "Completed"])
print(projects_not_completed)

#What is the average number of bugs for Completed projects only?
projects_completed = sum(project["bugs"] for project in projects if project["status"] == "Completed")
avg = projects_completed / len([project["bugs"] for project in projects if project["status"] == "Completed"])
print(avg)



#List all product names from api_response["data"].
names = [p["product"] for p in api_response["data"]]
print(names)

#otal inventory value (price × stock for each product, then sum).
total_inventory_value = sum(p["price"]* p["stock"] for p in api_response["data"])
print(total_inventory_value)

#Product name with the highest price.
high_price_product = max(api_response["data"], key = lambda p: p["price"])
print(high_price_product["product"])

#List product names that are out of stock (stock == 0).
out_of_stock = [p["product"] for p in api_response["data"] if p["stock"] == 0]
print(out_of_stock)

#List all user names.
user_names = [user["name"] for user in users_response["users"]]
print(user_names)

#List users who have "admin" in their roles (names only).
admin_users = [user["name"] for user in users_response["users"] if "admin" in user["roles"] ]
print(admin_users)

#Flat list of every role across all users (duplicates OK).
flat_list = [role for user in users_response["users"] for role in user["roles"]]
print(flat_list)

#Name of the user with the most roles.
most_roles_user = max(users_response["users"], key=lambda user: len(user["roles"]) )
print(most_roles_user["name"])

#Sort projects by bugs high → low; print top 3 names only.
sort_projects = sorted(projects, key = lambda project: project["bugs"], reverse = True)
sort_project_names = [project["name"] for project in sort_projects[:3]]
print(sort_project_names)

#Sort by priority (low number first), then name A→Z when priority ties. Print names only.
sort_projects_priority = sorted(projects, key = lambda project: (project["priority"], project["name"]))
sort_project_names = [project["name"] for project in sort_projects_priority]
print(sort_project_names)

#List all project names that tie for the most bugs (not just one from max).
highest = max(project["bugs"] for project in projects)
list_with_same_high_bugs = [project["name"] for project in projects if project["bugs"] == highest]
print(list_with_same_high_bugs)



#Customer with the largest unpaid order — print customer name.
highest_unpaid_order_customer_name = max([order for order in orders if not order["paid"]], key = lambda order: order["amount"])["customer"]
print(highest_unpaid_order_customer_name)

#Completed project with the most bugs — print project name.
completed_most_bugs_project = max([project for project in projects if project["status"] == "Completed"], key = lambda project: project["bugs"])["name"]
print(completed_most_bugs_project)

#How many projects are In Progress?
inprogress_projects = len([project for project in projects if project["status"] == "In Progress"])
print(inprogress_projects)

#Write def band(salary): — return "junior" if salary < 100k, "mid" if 100k–119999, "senior" if ≥ 120k. Using your employees list (add "years" only if you already have it; otherwise use the 5-person list from Section A), print a list like "Alice: senior" for everyone.
def band(salary):
    if salary < 100000:
        return "junior"
    elif salary in range(100000, 119999):
        return "mid"
    else:
        return "senior"


for employee in employees:
        print(employee["name"] ,band(employee["salary"]))
        
    
#Extract a field  [x["field"] for x in items]
#Filter [x for x in items if condition]
#Sum sum(x["amount"] for x in orders)
#Max/min by field max(items, key=lambda x: x["bugs"])
#Any / all any(...), all(...)
#Count len([x for x in items if ...])
#Flatten nested list [role for u in users for role in u["roles"]]