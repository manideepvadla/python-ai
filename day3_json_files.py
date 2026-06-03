"""
Day 3 — JSON + files practice

Run from the repo root:
  python day3_json_files.py

Data lives in practice_data/ (JSON + one text log).
Use: import json, then open(...) with encoding="utf-8".
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "practice_data"


# --- A. Load JSON into Python ---

# 1. Load employees.json into a variable `employees`. Print how many records you got.
employees = json.load(open(DATA_DIR / "employees.json", encoding="utf-8"))
print(len(employees))

# 2. Load orders.json. Print the customer name for order id 103.
orders = json.load(open(DATA_DIR / "orders.json", encoding="utf-8"))
print([order["customer"] for order in orders if order["id"] == 103][0])
# 3. Load projects.json. Print names of all projects with status "In Progress".
projects = json.load(open(DATA_DIR / "projects.json", encoding="utf-8"))
print([project["name"] for project in projects if project["status"] == "In Progress"])
# 4. Load inventory.json. Print total inventory value (sum of price * stock for each item in ["data"]).
inventory = json.load(open(DATA_DIR / "inventory.json", encoding="utf-8"))
print(sum(item["price"] * item["stock"] for item in inventory["data"]))
# 5. Load users.json. Print names of users where "active" is true.
users = json.load(open(DATA_DIR / "users.json", encoding="utf-8"))["users"]
print([user["name"] for user in users if user["active"] == True ])

# --- B. Same logic as Day 1/2, but data comes from files ---

# 6. From employees.json: print the name of the highest-paid employee (max + key).
print(max(employees, key=lambda employee: employee["salary"])["name"])
# 7. From orders.json: print total amount for paid orders only.
print(sum(order["amount"] for order in orders if order["paid"]))
# 8. From projects.json: print project names sorted by bugs, highest first (top 3 only).
print(sorted(projects, key=lambda project: project["bugs"], reverse=True)[:3])  
# 9. From users.json: build a flat list of every role (nested comprehension over users).
print([role for user in users for role in user["roles"]])
# 10. Write `def load_json(path):` that opens a path, uses json.load, and returns the parsed object.
#     Use it to load employees and orders; print both type() results.
def load_json(path):
    return json.load(open(path, encoding="utf-8"))
print(type(load_json(DATA_DIR / "employees.json")))
print(type(load_json(DATA_DIR / "orders.json")))

# --- C. Write JSON back to disk ---

# 11. Build a dict: {"total_orders": <count>, "total_amount": <sum of all amounts>}.
#     Write it to practice_data/order_summary.json (create/overwrite) with json.dump and indent=2.
order_summary = {"total_orders": len(orders), "total_amount": sum(order["amount"] for order in orders)}
json.dump(order_summary, open(DATA_DIR / "order_summary.json", "w", encoding="utf-8"), indent=2)
# 12. Filter employees with salary > 100000. Write that list to practice_data/high_earners.json.
high_earners = [employee for employee in employees if employee["salary"] > 100000]
json.dump(high_earners, open(DATA_DIR / "high_earners.json", "w", encoding="utf-8"), indent=2)
# 13. From projects.json, build a list of only {"name", "bugs"} for projects with bugs > 5.
#     Write to practice_data/buggy_projects.json.
buggy_projects = [{"name": project["name"], "bugs": project["bugs"]} for project in projects if project["bugs"] > 5]
json.dump(buggy_projects, open(DATA_DIR / "buggy_projects.json", "w", encoding="utf-8"), indent=2)

# --- D. Text files (not JSON) ---

# 14. Read practice_data/activity.log line by line. Print lines that contain the word "error".
error_lines = [line for line in open(DATA_DIR/"activity.log", encoding="utf-8") if "error" in line]
print(error_lines)

# 15. Count how many lines in activity.log contain "login" (case-sensitive is fine).
login_lines = len([line for line in open(DATA_DIR / "activity.log", encoding="utf-8") if "login" in line])
print(login_lines)

# 16. Append one new line to activity.log: "2026-05-21 practice user=you".
#     Re-read the file and print the last line to confirm.
with open(DATA_DIR / "activity.log", "a", encoding="utf-8") as file:
    file.write("2026-05-21 practice user=you\n")
with open(DATA_DIR / "activity.log", "r", encoding="utf-8") as file:
    print(file.readlines()[-1])


# --- E. Small functions (file in, result out) ---

# 17. `def employee_names_from_file(path):` — load JSON list of employee dicts, return list of names.

def employee_names_from_file(path):
  employees = json.load(open(path, encoding="utf-8"))
  return [employee["name"] for employee in employees]

print(employee_names_from_file(DATA_DIR / "employees.json"))


# 18. `def unpaid_order_ids_from_file(path):` — load orders JSON, return ids where paid is false.

def unpaid_order_ids_from_file(path):
  orders = json.load(open(path, encoding="utf-8"))
  return [order["id"] for order in orders if not order["paid"]]

print(unpaid_order_ids_from_file(DATA_DIR/"orders.json"))

# 19. `def write_report(path, rows):` — `rows` is a list of dicts; write JSON array to `path` with indent=2.
#     Test by writing a 2-row sample to practice_data/sample_report.json.

def write_report(path, rows):
  json.dump(rows, open(path, "w", encoding="utf-8"), indent=2)

write_report(DATA_DIR / "sample_report.json", [{"name": "John", "amount": 100}, {"name": "Jane", "amount": 200}]) 
print(open(DATA_DIR / "sample_report.json", encoding="utf-8").read())

# --- F. Combine read → transform → write ---

# 20. Load orders.json. Build a list of strings "customer: amount" for unpaid orders only.
#     Write one string per line to practice_data/unpaid_orders.txt (text file, not JSON).
orders = json.load(open(DATA_DIR/"orders.json", encoding="utf-8"))
unpaid_orders_amount = [f'{order["customer"]} : {order["amount"]}' for order in orders if not order["paid"]]
write_report(DATA_DIR / "unpaid_orders.txt", unpaid_orders_amount)
print(open(DATA_DIR / "unpaid_orders.txt", encoding="utf-8").read())

# 21. Load employees.json. Add a new key "band" to each dict ("junior" < 100k, "mid" < 120k, else "senior").
#     Write the full updated list to practice_data/employees_with_band.json.
employees = json.load(open(DATA_DIR/"employees.json", encoding="utf-8"))

def salary_band(salary):
    if(salary<100000):
        return "junior"
    elif(salary<120000):
        return "mid"
    else:
        return "senior"
  
employees_with_band = [{**employee, "band": salary_band(employee["salary"])} for employee in employees]
write_report(DATA_DIR / "employees_with_band.json", employees_with_band)

# 22. Load inventory.json. Write a new file practice_data/in_stock.json containing only products with stock > 0
#     (same shape as original items: product, price, stock).

inventory = json.load(open(DATA_DIR/"inventory.json", encoding="utf-8"))
in_stock_products = [{"product": product["product"], "price": product["price"], "stock": product["stock"]} for product in inventory["data"] if product["stock"] > 0]
write_report(DATA_DIR / "in_stock.json", in_stock_products)


# --- G. Optional stretch ---

# 23. Load employees and orders in one script. Print one line: "N employees, M orders".

employees_and_orders = json.load(open(DATA_DIR / "employees.json", encoding="utf-8")) + json.load(open(DATA_DIR/"orders.json", encoding="utf-8"))
print(f"{len(employees_and_orders)} employees, {len(orders)} orders")

# 24. If a JSON file is missing, print a friendly message instead of crashing (try/except FileNotFoundError).

try:
    json.load(open(DATA_DIR / "employees.json", encoding="utf-8"))
except FileNotFoundError:
    print("employees.json file not found")
try:
    json.load(open(DATA_DIR/"orders.json", encoding="utf-8"))
except FileNotFoundError:
    print("orders.json file not found") 
# 25. Use Path: list all .json files in practice_data/ and print each filename.

for file in DATA_DIR.glob("*.json"):
    print(file.name)