# "Break" statement terminates loop

# The "continue" statement is used to skip the remaining code inside a loop for the current iteration only.

for num in range(0,10):
    if num == 5:
        continue
    print(f'Iteration: {num}')


# "pass" statement allows the remaining code to execute only if the condition is true.
# whereas "continue" statmenet will skip the remaining code when the condition is true.
for num in range(0,10):
    if num == 5:
        pass
    print(f'Iteration: {num}')