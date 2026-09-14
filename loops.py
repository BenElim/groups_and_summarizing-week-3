# For Loop Example
hubs =["Nenap", "Nguvu tech", "Garissa", " kalobeyei", " lodwar technical"]

for hub in hubs:
    print(hub)


    # range loop
    #i =" lodwar technical"
    for i in range(5):
        print(i)
        # while loop
        password = ""
        while password != "secret123":
            password = input("Enter your password: ")
            if password == "python":
                print("Access granted")
            else:
                print("Access denied")