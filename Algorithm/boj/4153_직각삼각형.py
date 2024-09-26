
# banana**2 + apple**2 = melon**2 >> 피타고라스

while True:
    fruits = input().split(' ') # fruits[6, 8, 10]
    apple = int(fruits[0])
    banana = int(fruits[1])
    melon = int(fruits[2])

    if apple==0 and banana==0 and melon==0:
        break


    if not (melon > apple and melon > banana):
        small_melon = melon
        # apple > banana ==> apple과 melon을 스위치한다
        if apple > banana:
            melon = apple
            apple = small_melon
        elif banana > apple:
            melon = banana
            banana = small_melon

    if apple**2 + banana**2 == melon**2:
        print('right')
    else:
        print('wrong')

        # banana > apple ==> banana와 melon을 스위치한다
