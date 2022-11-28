#Function to check string validity

def valid_bracket(s: str):

        #Dictionary of closing brackets with corresponding opening bracket
        bracket = {')':'(','}':'{',']':'['}
        #Initialising a stack
        stack = []
        
        #Checking each element in the string
        for i in s:

            #if the element is a opening bracket
            if i in bracket.values():

                #Insert the element into the stack
                stack.append(i)

            #If the element is a closing bracket
            else:

                #If the stack is empty
                if (not stack):
                    return False

                else:
                    #Top elemnt of the stack
                    ele = stack.pop()
                    #Check if the popped element is the corresponding opening bracket for the current closing bracket
                    if bracket[i] != ele:
                        return False
        #If stack has elements
        if(stack):
            return False
        else:
            return True

def main():
    string = input("Enter a string of brackets: ")
    print(valid_bracket(string))

  

if __name__ == "__main__":
    main()