row1 = ["🗳️","🗳️","🗳️"]
row2 = ["🗳️","🗳️","🗳️"]
row3 = ["🗳️","🗳️","🗳️"]

map = [row1, row2, row3]
print(f"{row1}\n {row2}\n {row3}\n")
selection = input("Where do you want to put treasure(31 = row 3 colum 1): ")

onebyone=selection.split()
print(onebyone)