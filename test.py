while True:
    print("Top Loop")
    test_list = list(range(4))
    for i in test_list:
        if i % 2 == 0:
            print(i)
        else:
            continue