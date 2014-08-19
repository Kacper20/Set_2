for _ in range (input()):
    name = raw_input().split()
    name = name[0]
    print name
    if (len(name)) %2 == 1:
        print -1
        continue
    else:
        name_a = name[0:len(name)/2]
        name_b = name[len(name)/2::1]
        difference = 0
        for i in range (len(name_a)):
            if name_a[i-1] is not name_b[i]:  # name_a bedzie sprawdzane odwrotnie.
                difference += 1
        print difference