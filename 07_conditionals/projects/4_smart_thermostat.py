device_status = "active"
temperature = 20

if device_status == "active":
    if temperature > 35:
        print("Warn: High temperature alert!")
    else:
        print("Temperature normal")
else:
    print("Device is offline")
