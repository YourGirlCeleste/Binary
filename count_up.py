binary = "0"
deciaml = 0
infinite = True

while True:
    deciaml += 1
    remainder = first = True
    new_num = []
    for x in reversed(binary):

        if first or remainder:
            if x == "0":
                x = "1"
                remainder = False 
            else:
                x = "0"
                if not remainder:
                    remainder = True
            first = False     

        new_num.append(x)

    if remainder:

        if infinite:
            new_num.append("1")

        else:
            break

    binary = ""
    for x in reversed(new_num):
        binary += x

    with open('file.txt', 'a') as file:
        file.write(f" {deciaml} : {binary}\n")
