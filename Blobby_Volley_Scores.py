t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    alice = 0
    bob = 0
    server = 'A'  
    for point in s:
        if point == server:
            if server == 'A':
                alice += 1
            else:
                bob += 1
        else:  
            server = point          
    print(alice, bob)
