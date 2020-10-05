with open('a.lib', 'r', encoding = "Big5", errors='replace') as f:
    b_str = f.readlines()
    #print(b_str.decode('big-5'))
    #print(b_str)
    for l in b_str:
        print(l)