import math

while True:
    print("\nChoose the math Operation.\n\n0.Addition \n1.Subraction \n2.Division\n3.Multiplication\n4.Modulos")

    oper = input("\n Your option from the menu")

    if oper == "0":
        val1 =float(input("\nFirst Number"))
        val2 = float(input("\nSecond Number"))

        print("\n The result is:"+ str(val1+val2)+"\n")

        back = input("\n Go Back to the  main menu?(y/n)")

        if back =='y':
            continue
        else:
            break

    if oper == "1":
        val1 =float(input("\nFirst Number"))
        val2 = float(input("\nSecond Number"))

        print("\n The result is:"+ str(val1-val2)+"\n")

        back = input("\n Go Back to the  main menu?(y/n)")

        if back =='y':
            continue
        else:
            break

    if oper == "2":
        val1 =float(input("\nFirst Number"))
        val2 = float(input("\nSecond Number"))

        print("\n The result is:"+ str(val1/val2*100)+"\n")

        back = input("\n Go Back to the  main menu?(y/n)")

        if back =='y':
            continue
        else:
            break

    if oper == "3":
        val1 =float(input("\nFirst Number"))
        val2 = float(input("\nSecond Number"))

        print("\n The result is:"+ str(val1*val2)+"\n")

        back = input("\n Go Back to the  main menu?(y/n)")

        if back =='y':
            continue
        else:
            break
