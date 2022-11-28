
def max_knapsack(max_weight: int,arrayOfItems: list,n: int):
    #dynamic programming 
    #table to calculate values
    arr=[[0 for i in range(max_weight+1)] for i in range(n+1) ]
   
    for i in range(n+1):
         for j in range(max_weight+1):
             if (i == 0  or  j == 0):
                 arr[i][j] = 0
             elif (arrayOfItems[i-1]['weight'] <= j):
                 #maximum value between previous value and with the current addition
                 arr[i][j] = max(arrayOfItems[i-1]['value']+ arr[i-1][j-arrayOfItems[i-1]['weight']],arr[i-1][j])
             else:
                #considering previous value
                 arr[i][j] = arr[i-1][j]
    #Last element in the matrix would give the maximum value
    return arr[n][max_weight]

def main():
    n=int(input("Enter number of items: "))
    arrayOfItems=[]
    for i in range(n):
        d={}
        d['name']=input("Enter name of item {} : ".format(i+1))
        d['weight']=int(input("Enter weight of item {} : ".format(i+1)))
        d['value']=int(input("Enter value of item {} : ".format(i+1)))
        arrayOfItems.append(d)
    max_weight=int(input("Enter maximum weight of knapsack"))
    #list of items
    #var= [{ 'name':'map', 'weight':9, 'value':150 }, { 'name':'compass', 'weight':13, 'value':35 }, { 'name':'water', 'weight':153, 'value':200 }, { 'name':'sandwich', 'weight':50, 'value':160 }, { 'name':'glucose', 'weight':15, 'value':60 }, { 'name':'tin', 'weight':68, 'value':45 }, { 'name':'banana', 'weight':27, 'value':60 }, { 'name':'apple', 'weight':39, 'value':40 }] 
    #maximum weight of knapsack
    #max_weight=100
    print(max_knapsack(max_weight,arrayOfItems,n))
    
if __name__ == "__main__":
    main()
