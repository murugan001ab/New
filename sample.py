player1=0
player2=0
total=0
value=[1,2,3,4,5,6,7,8,9,10]
def invaled_input_2():
    print("warnning! remmamber the rule !")
    player2 = int(input("player 2:"))
    if player2 in value:
        return player2
    else:
        invaled_input_2()
def invaled_input():
    print("warnning! remmamber the rule !")
    player1 = int(input("player 1:"))
    if player1 in value:
        return player1
    else:
        invaled_input()
while(total<100):
    player1=int(input("player 1:"))
    if player1 in value:
        total += player1
        player1 = total
        print("total:", total)
    else:
        invaled_input()
        total+=invaled_input()
        player1=total
        print("toal:",total)
    if total == 100:
        break
    player2 = int(input("player 2:"))
    if player2 in value:
        total += player2
        player2 = total
        print("total:", total)
        print("------------------------------------")
    else:
        invaled_input_2()
        total += invaled_input_2()
        player2 = total
        print("toal:", total)
        print("------------------------------------")
if player1==100:
    print("the winner is player 1")
else:
    print("the winner is player 2:")
