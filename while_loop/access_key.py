i = 1
sum_value = 0
old = 0
first_loop = 0
print("TechHackingProgram Build 91")
loop = int(input("Enter a user key storage number : "))
while i <= loop:
    sum_value = sum_value + i
    print("Got user key secret %d -> Current password %d" % (i, sum_value))
    i = i + 1
print("Successfully accessed to key storage. First key : %d" % (sum_value))
old = sum_value
first_loop = loop

sum_value = 0
i = 1
loop = int(input("Enter a second user key storage number : "))
while i <= loop:
    if i % 2 == 0:
        sum_value = sum_value + i
        print("Got user key secret: %d -> Current password %d" % (i, sum_value))
    i = i + 1

print("Successfully accessed to second key storage. Second key : %d" % (sum_value))

key_number = sum_value * (old - sum_value)
print("Successfully got key. Key number : %d" % (key_number))

print("WSSystem 5.1")
user_id_generated = first_loop + loop
user_id_input = 0
print("User id cache : 0")
while user_id_input != user_id_generated:
    print("No user found.")
    user_id_input = int(input("Enter user id : "))
user_psd_input = 0
print("User password cache : 0")
while user_psd_input != key_number:
    print("Password is wrong.")
    user_psd_input = int(input("Enter user password : "))
print("Welcome, Kim jung eun!")
print("Launching nuclear bomb...")
print("Success!")
