def genericPostCodes(kod1, kod2):
    kod1l= kod1.split('-')
    kod2l = kod2.split('-')


    kod1l = [int(item) for item in kod1l]
    kod2l = [int(item) for item in kod2l]
    

    while not kod1l == kod2l:
        if kod1l[1] < 999:
            kod1l[1] += 1
            if kod1l[1] < 10:
                print("{}-00{}".format(kod1l[0], kod1l[1]))
            elif kod1l[1] < 100:
               print("{}-0{}".format(kod1l[0], kod1l[1]))
            else:
                print("{}-{}".format(kod1l[0], kod1l[1]))

        else:
            kod1l[0] += 1
            kod1l[1] = 0
            print("{}-00{}".format(kod1l[0], kod1l[1]))


