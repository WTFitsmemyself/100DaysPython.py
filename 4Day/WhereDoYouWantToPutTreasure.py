row1 = ["🗳️","🗳️","🗳️"]
row2 = ["🗳️","🗳️","🗳️"]
row3 = ["🗳️","🗳️","🗳️"]

map = [row1, row2, row3]
print(f" {row1}\n {row2}\n {row3}\n")
selection = input("Where do you want to put treasure(3 1 = row 3 colum 1): ")

onebyone=selection.split()
int_row = int(onebyone[0]) - 1
int_col = int(onebyone[1]) - 1

map[int_col][int_row] = "x"

print(f" {row1}\n {row2}\n {row3}\n")