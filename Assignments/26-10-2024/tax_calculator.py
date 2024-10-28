counter = 1
while counter < 4:
    earning = float(input("Enter citizen " + str(counter) + " earning: "))

    if earning <= 30000:
        tax = earning * 0.15
        print("Citizen", counter, "tax is", round(tax, 1))
    else:
        tax = earning * 0.2
        print("Citizen", counter, "tax is", round(tax, 1))      

    counter += 1