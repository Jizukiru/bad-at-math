def main():

    OpList = {
        "Horner": "Factors a polynomial using Horner's method, needs 1 known root of the polynomial",
        "Quadratic Equation": "Solves a quadratic equation",
        "exit": "Exits the program"
    }

    def QuadraticCalculator():
        print("Equation must be in the form 'a*x^2 + b*x + c = 0'\na,b,c ∈ IZ")
        def f(a, b, c):
            if a == 0:
                if b == 0:
                    print("Expression is not a valid equation (c = 0x or 0x = 0)")
                    print("Returning to Operation Selection Screen")
                    SelectOperation()
                else:
                    print("Equation is not Quadratic (a = 0 <=> a*x^2 = 0)")
                    print(f"x = {(-c)/b}")
                    SelectOperation()
                    exit()

            
            discriminant = b ** 2 - 4 * a * c


            if discriminant < 0:
                print(f"Equation is impossible in IR with a discriminant of {discriminant}")
                SelectOperation()
            sol = [(-b - discriminant ** (1/2)) / (2 * a), (-b + discriminant ** (1/2)) / (2 * a)]
            if sol[0] == sol[1]:
                print(f"x = {sol[0]}")
            else:
                print(f"x1 = {sol[0]}\nx2 = {sol[1]}\ndiscriminant = {discriminant}")
        try:
            a = int(input("input a: "))
            b = int(input("input b: "))
            c = int(input("input c: "))
        except ValueError:
            print("Program only accepts integer modifiers.")
            QuadraticCalculator()
        f(a, b, c)
        print("Result found. Returning to Operation Selection. Input \"exit\" to close program")
        SelectOperation()

    def Horner(): #Start
        #Find Order to learn necessary loop length
        try:
            PolyOrder = int(input("Input the order of the dividend: "))
        except ValueError:
            print("Polynomial order must be an integer")
            Horner() #Goes to start
        ModList = []
        for i in range(1,PolyOrder+2):
            modifier = int(input(f"Input modifier #{i}, starting from x^{PolyOrder}. If a modifier is not in P(x), input 0.\nInput modifier: "))
            ModList.append(modifier)
        try:
            root = int(input("Input the root (r) of P(x). It can be found in the divisor: (x-r): "))
        except ValueError:
            print("Root must be an integer")
            exit()
            SelectOperation()
        temp_mod = ModList[0]
        FactMods = [ModList[0]]
        for i in range(1, PolyOrder+1):
            temp_mod = temp_mod * root + ModList[i]
            FactMods.append(temp_mod)
        if root > 0:
            FactEq = f"P(x) = (x-{root})("
        elif root < 0:
            FactEq = f"P(x) = (x+{root})("
        else:
            FactEq = 'P(x) = x('
        for i in range(len(FactMods)): #IndexError when i starts from 0
            if FactMods[i] == 0:
                continue
            else:
                if FactMods[i] > 0 and i != 0:
                    if i == PolyOrder-1:
                        FactEq += "+" + str(FactMods[i])
                    else:
                        FactEq += "+" + str(FactMods[i]) + f"x^{PolyOrder-i-1}"
                else:
                    if i == PolyOrder-1:
                        FactEq += str(FactMods[i])
                    else:
                        FactEq += str(FactMods[i]) + f"x^{PolyOrder-i-1}"
        FactEq += ")"
        print("Factored polynomial described by the formula:")
        print(FactEq)
        print("Returning to Operation Selection. Input \"help\" for list of operations")
        SelectOperation()

    def SelectOperation():
        #Send back to this step if operation is invalid
        operation = input("Select Operation: ")
        if operation == "Quadratic Equation":
            QuadraticCalculator()
        elif operation == "Horner" or operation == "Horner's method":
            Horner()
        elif operation == "exit":
            exit()
        elif operation == "help":
            ComHelp = input("Enter command to show its function, or \"all\" to show all commands and their functions: ")
            if ComHelp == "all":
                for key, value in OpList.items():
                    print(f'{key}: {value}')
                SelectOperation()
            else:
                while ComHelp not in OpList.keys():
                    ComHelp = input("Invalid Operation Key. Enter valid key: ")
                print(OpList[ComHelp])
                SelectOperation()
        else:
            print("Invalid Operation. Input \"help\" for commands list")
            SelectOperation()

    SelectOperation()


if __name__ == '__main__':
    main()


