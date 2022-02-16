magicians = ["   david  ", "    dough", "Siegfied", "roy  ", "lance", "Ricky"]
last_names = ["Copperfield", "Henning", "Buyenlarge", "Burton", "Jay "]


# It is always a good practice to use strip method when manipulating text
for magician in magicians:
    print(f"{magician.title().strip()}, that was a great trick!!!!")
    print(f"I can't wait to see your next trick, {magician.title().strip()}\n")
print("Thank you everyone, that was a great magic show!!!")