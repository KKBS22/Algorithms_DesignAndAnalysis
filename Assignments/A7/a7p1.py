import sys

a = 4
cj = [1, 5, 10, 15, 25]
cl = [0, 0, 0, 0, 0]
coinum = [5, 5, 5, 0, 0]
denomination = [0]*5
Mtest = [None]*22
sp = [None]*22
MVal = [None]*22
cTest = [[0, 0, 0, 0, 0]]*22


def MinCoinsTuple(totalChange, coinArray):
    Output_test = [0]*(len(coinArray))
    coinsUsed = [0]*(totalChange+1)
    minCoin = [None]*(totalChange+1)

    for a in range(totalChange+1):
        if a == 0:
            minCoin[a] = 0
        else:
            minCoin[a] = 10000000000
            for j in range(len(coinArray)):
                if a >= coinArray[j]:
                    if minCoin[a] > 1 + minCoin[a - coinArray[j]]:
                        minCoin[a] = 1 + minCoin[a - coinArray[j]]
                        newCoin = j
            coinsUsed[a] = newCoin
            print(coinsUsed)

    n = totalChange
    while (n > 0):
        Output_test[coinsUsed[n]] = Output_test[coinsUsed[n]] + 1
        print(coinsUsed[n])
        n = n - coinArray[coinsUsed[n]]

    print(Output_test)


def max_change(coinArray, coinNumbers):
    maxValue = 0
    for a in range(len(coinArray)):
        maxValue = maxValue + coinArray[a] * coinNumbers[a]
    return maxValue


def min_coin_dp(totalChange, coinArray):
    for a in range(totalChange+1):
        if a == 0:
            Mtest[a] = 0
            # cTest[a].append([0,0,0,0])
        else:
            Mtest[a] = 10000000000
            if totalChange < max_change(coinArray, coinum):
                maxCoinsUsed = sum(coinum)
                actalUsedCoins = 0
                for j in range(len(coinArray)):
                    if (a >= coinArray[j]) and (coinum[j] >= 0):
                        #MC[j] = MC[j]+1
                        if Mtest[a] > 1 + Mtest[a - coinArray[j]]:
                            Mtest[a] = 1 + Mtest[a - coinArray[j]]
                            coin = j
                sp[a] = coin
            else:
                print("Not possible to make change")
    print(Mtest)
    print(sp)
    a = totalChange
    while a > 0:
        cl[sp[a]] = cl[sp[a]] + 1
        # print(cl)
        a = a - coinArray[sp[a]]
    print(cl)
    #findSolution(totalChange, coinArray, len(coinArray))
# Function to find the possible
# combination of coins to make
# the sum equal to X


def min_coins_res(totalChange, coinArray, changeList):
    for a in range(totalChange+1):
        if a == 0:
            Mtest[a] = 0
        else:
            Mtest[a] = 10000000
            for j in range(len(coinArray)):
                pass


def findSolution(n, coinArray, m):

    # Base Case
    if (n == 0):

        # Print Solutions
        print(denomination)

        return

    for i in range(m):

        # Try every coin that has
        # value smaller than n
        if (n - coinArray[i] >= 0 and
                Mtest[n - coinArray[i]] + 1 == Mtest[n]):

            # Add current denominations
            denomination[i] += 1

            findSolution(n - coinArray[i], coinArray, m)
            break


def main():
    min_coin_dp(a, cj)
    #MinCoinsTuple(a, cj)
    #findSolution(a, cj, 5)


if __name__ == "__main__":
    main()
