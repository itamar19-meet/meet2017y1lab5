def draw_with():
    num = input("how many stars in each line?")
    lines = input("how many lines do you want?")
    print("*" * int(num))
    for i in range(int(lines) - 1):
        print("*" * int(num))
    return
        
