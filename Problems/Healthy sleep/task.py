norm_low = int(input())
norm_top = int(input())
you_sleep = int(input())

if norm_low <= you_sleep <= norm_top:
    print("Normal")
else:
    if you_sleep < norm_low:
        print("Deficiency")
    else:
        print("Excess")
