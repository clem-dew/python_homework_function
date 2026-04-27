# SANS INPUT

def table(num):
    for n in range(1, 11):
        print(f"{num} x {n} = {n * num}")

table(11)

# AVEC INPUT

def user_table():
    user_numb = int(input("Quelle table de multiplication veux-tu voir afficher ? "))
    for n in range(1, 11):
        print(f"{user_numb} x {n} = {user_numb * n}")

user_table()