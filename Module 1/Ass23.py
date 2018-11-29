customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }
print(customer_details)
print(customer_details.keys())
print(customer_details.values())
print([value for (key, value) in sorted(customer_details.items())])
del(customer_details[1005])
print(customer_details)
customer_details[1003]="Mary"
print(customer_details)

if 1002 in customer_details.keys():
    print("Available")
else:
    print("Unavailable")