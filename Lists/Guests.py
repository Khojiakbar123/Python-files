guests = ['frank', 'edward', 'john']
guests[0] = "khojiakbar"

guests.insert(0, "xoja")
guests.insert(3, "lola")
guests.append("munis")

print(guests)
print("We are sorry, we can only invite two people.")
guests.pop()


print(f"Hello, {guests[0].title()} I would like to invite you to dinner.")
print(f"Hello, {guests[1].title()} I would like to invite you to dinner.")
print(f"Hello, {guests[2].title()} I would like to invite you to dinner.")
print(f"Hello, {guests[3].title()} I would like to invite you to dinner.")
print(f"Hello, {guests[4].title()} I would like to invite you to dinner.")

print("We are very sorry, we can only invite two people.")

uninvited_list = 