#!/usr/bin/env python3

cost = input('enter cost in format x.x.x(yuan.jiao.fen)')
given_money = input('enter given money in format x.x.x(yuan.jiao.fen)')

def convert(money, mode):
    if mode == 1:
        money = money.split('.')
        return int(money[0]) * 100 + int(money[1]) * 10 + int(money[2])
    elif mode == 2:
        yuan = money // 100
        jiao = money % 100 // 10
        fen = money % 10
        return (yuan, jiao, fen)

cost = convert(cost, 1)
given_money = convert(given_money, 1)

change_return = given_money - cost
if change_return < 0:
    print('given money is not enough')
else:
    change_return = convert(change_return, 2)
    print('change return %d yuan %d jiao %d fen' % change_return)
