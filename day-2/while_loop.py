# Initialize a counter variable
counter = 1

# Use a while loop to print numbers from 1 to 5
while counter <= 5:
    print("Counter is:", counter)
    counter += 1

# Initialize a counter variable
counter = 1

# Use a while loop to print numbers from 1 to 5
# If counter equals 4, break the loop
while counter <= 5:
    if counter == 4:
        break # Break statement will be discussed in day 3
    print("Counter is:", counter)
    counter += 1


# Initialize a counter variable
counter = 0

# Use a while loop to print numbers from 1 to 5, skipping 3
# If counter equals 3, skip the current iteration
while counter < 5:
    counter += 1
    if counter == 3:
        continue
    print("Counter is:", counter)

# Use a while loop to print "Hello, world!" indefinitely
# Press Ctrl+C to stop the program
while True:
    print("Hello, world!")
