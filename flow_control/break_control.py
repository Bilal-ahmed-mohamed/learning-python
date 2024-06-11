# Python break and continue

# In programming, the break and continue statements are used to alter the flow of loops:

# Example: break Statement with for Loop
# We can use the break statement with the for loop to terminate the loop when a certain condition is met. For example,

for i in range(5):
    if i == 4:
        break
    print(i)



# Python continue Statement
# The continue statement skips the current iteration of the loop and the control flow of the program goes to the next iteration.  

for i in range(6):
    if i == 4:
        continue
    print(i)  