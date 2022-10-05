numbers = "0123456789"

with open("./6digit-wordlist.txt", "w") as file:
    for k in range(len(numbers)):
        for l in range(len(numbers)):
            for m in range(len(numbers)):
                for n in range(len(numbers)):
                    for o in range(len(numbers)):
                        for p in range(len(numbers)):
                            file.write(numbers[k]+numbers[l]+numbers[m]+numbers[n]+numbers[o]+numbers[p]+"\n")

file.close()