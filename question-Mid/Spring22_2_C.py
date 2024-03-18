# # Get input list from the user
# user_input = input("Enter elements of the list separated by spaces: ").split()

# # Convert input elements to integers
# input_list = [int(x) for x in user_input]

# # Check if the list has enough elements to exclude the first and last
# if len(input_list) < 3:
#     print("Not possible")
# else:
#     # Create a new list excluding the first and last elements
#     new_list = input_list[1:-1]
#     print("New list excluding first and last elements:", new_list)

#spring-2022-02-c
userinput=input("enter the number ").split()


inputToiNT=[int(x) for x in userinput]

if len(inputToiNT) < 3:
    print("not possible ")
else:
    newlist=inputToiNT[1:-1]
    print("new list ",newlist)    
