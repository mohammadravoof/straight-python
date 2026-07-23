# # Getting inputs from the user
# age = int(input("Enter your age: "))
# if age >= 18:
# print("You are eligible for voting")
# elif age < 18 and age > 14:
# print("You are not eligible for voting")
# else:
# print("Go to school kid!")

# # for statement
# animals = ['cat', 'dog', 'cow']
# for animal in animals:
# print(animal, len(animal))

# # Create a sample collection
# users = {'udhay': 'active', 'vinay': 'inactive', 'shyam': 'active'}

# # Strategy: Iterate over a copy
# for user, status in users.copy().items(): #if .copy() is removed RuntimeError: dictionary changed size during iteration
# if status == 'inactive':
# del users[user]
# print(users)
# print()

# # Strategy: Create a new collection
# active_users = {}
# for user, status in users.items():
# if status == 'active':
# active_users[user] = status
# print(active_users)

# # range() function
# for i in range(5):
# print(i)
# print()
# print(list(range(5,10)))
# print()
# print(list(range(0,10,2)))
# print()
# print(list(range(0,-10,-2)))
# print()

# poem = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(poem)):
# print(i, poem[i])

# print('sum(range(4)) --> 0+1+2+3= ',sum(range(4)))

# # The break statement breaks out of the innermost enclosing loop.
# for n in range(2, 10): # n = 2, 3, 4, 5, 6, 7, 8, 9
# for x in range(2, n):
# if n % x == 0:
# print(f"{n} equals {x} * {n//x}")
# break

# # First iteration: n = 2
# # The inner loop does not execute because range(2, 2) is empty.

# # Second iteration: n = 3
# # The inner loop runs once with x = 2.
# # Since 3 % 2 != 0, the if condition fails, so nothing is printed.

# # Third iteration: n = 4
# # The inner loop starts with x = 2.
# # Since 4 % 2 == 0, the condition is true.
# # It prints "4 equals 2 * 2" and break exits the inner loop.

# # Fourth iteration: n = 5
# # The inner loop runs with x = 2, 3, and 4.
# # None divide 5 evenly, so the if condition never succeeds.

# # Fifth iteration: n = 6
# # The inner loop starts with x = 2.
# # Since 6 % 2 == 0, it prints "6 equals 2 * 3"
# # and break exits the inner loop immediately.

# # Sixth iteration: n = 7
# # The inner loop runs with x = 2, 3, 4, 5, and 6.
# # None divide 7 evenly, so nothing is printed.

# # Seventh iteration: n = 8
# # The inner loop starts with x = 2.
# # Since 8 % 2 == 0, it prints "8 equals 2 * 4"
# # and break exits the inner loop.

# # Eighth iteration: n = 9
# # The inner loop checks x = 2 first (condition fails).
# # Then x = 3, where 9 % 3 == 0.
# # It prints "9 equals 3 * 3" and break exits the inner loop.

# # The else statement executes only when the loop completes without hitting the break statement.

# # The continue statement skips the remaining code in the current iteration
# # and moves to the next iteration of the loop.

# for num in range(2, 10): # num = 2, 3, 4, 5, 6, 7, 8, 9
# if num % 2 == 0:
# print(f"Found an even number {num}")
# continue
# print(f"Found an odd number {num}")

# # First iteration: num = 2
# # Since 2 % 2 == 0, the condition is true.
# # It prints "Found an even number 2".
# # continue skips the remaining code in the loop body,
# # so "Found an odd number 2" is not printed.

# # Second iteration: num = 3
# # Since 3 % 2 != 0, the condition is false.
# # The continue statement is not executed.
# # It prints "Found an odd number 3".

# # Third iteration: num = 4
# # Since 4 % 2 == 0, the condition is true.
# # It prints "Found an even number 4".
# # continue skips the remaining code in the loop body.

# # Fourth iteration: num = 5
# # Since 5 % 2 != 0, the condition is false.
# # The continue statement is not executed.
# # It prints "Found an odd number 5".

# # Fifth iteration: num = 6
# # Since 6 % 2 == 0, the condition is true.
# # It prints "Found an even number 6".
# # continue skips the remaining code in the loop body.

# # Sixth iteration: num = 7
# # Since 7 % 2 != 0, the condition is false.
# # The continue statement is not executed.
# # It prints "Found an odd number 7".

# # Seventh iteration: num = 8
# # Since 8 % 2 == 0, the condition is true.
# # It prints "Found an even number 8".
# # continue skips the remaining code in the loop body.

# # Eighth iteration: num = 9
# # Since 9 % 2 != 0, the condition is false.
# # The continue statement is not executed.
# # It prints "Found an odd number 9".

# # else clause
# # In a for or while loop the break statement may be paired with an else clause. If the loop finishes without executing the break, the else clause executes.

# for n in range(2, 10):
# for x in range(2, n):
# if n % x == 0:
# print(n, 'equals', x, '*', n//x)
# break
# else:
# # loop fell through without finding a factor
# print(n, 'is a prime number')

# # Difference between break and continue
# print('break')
# for i in range(10):
# if i == 2:
# print()
# break
# print(i)
# print()

# print('continue')
# for i in range(10):
# if i == 2:
# print()
# continue
# print(i)