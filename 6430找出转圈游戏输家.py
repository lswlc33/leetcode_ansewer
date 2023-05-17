n = 4
k = 4

def circularGameLosers(n: int, k: int):
    player = [0] * n
    player[0] = 1

    i = 0
    times = 0

    while 2 not in player:
        times += 1
        i += times * k
        player[i%n] += 1

    loss = []
    for play in range(1,len(player)+1):
        if player[play-1] == 0:
            loss.append(play)
            
    return loss

circularGameLosers(n,k)