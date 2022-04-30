import random
from enum import Enum

# 枚举 定义枚举类型


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)  # 用法


for suite in Suite:
    print(suite, ":", suite.value)


class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = ["黑桃", "红心", "梅花", "方块"]
        faces = [
            '', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',
            'K'
        ]
        # 根据牌的花色和点数取到对应的字符
        return '%s%s' % (suites[self.suite.value], faces[self.face]
                         )  # 枚举类型的值可以直接访问

    def __lt__(self, other):  # 魔法方法 算术运算
        # 花色相同比较点数的大小
        if self.suite == other.suite:
            return self.face < other.face
        # 花色不同比较花色对应的值
        return self.suite.value < other.suite.value


card1 = Card(Suite.SPADE, 5)  # 这应该相当于静态方法
print(card1)


class Poker:
    """扑克"""

    def __init__(self):
        # 通过列表的生成式语法创建一个装52张牌的列表
        self.cards = [
            Card(suite, face) for suite in Suite for face in range(1, 14)
        ]  # 用法
        # current属性表示发牌的位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        # 通过random模块的shuffle函数实现列表的随机乱序
        random.shuffle(self.cards)  #

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)


poker = Poker()
poker.shuffle()
print(poker.cards)


class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()


poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())  #
for player in players:
    player.arrange()
    print(player.name, ":", end='')
    print(player.cards)
