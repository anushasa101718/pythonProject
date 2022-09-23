atm = [100,500,2000]
denomination = int(input("Enter amount to withdraw:"))
for money in atm:
    if denomination not in atm:
        print("Selected denomination {} not available" . format(denomination))
        break
    else:
        print("withdrawl is successful {}" .format(denomination))


 #### break

atm = [500, 2000]
denomination = int(input("Enter amount to withdraw:"))
for money in atm:
    if denomination not in atm:
        print("Selected denomination {} not available".format(denomination))
        break
    else:
        print("withdrawl is successful {}".format(denomination))
        break