from otree.api import *
import time
import random

doc = """
Blindbox Auction
"""



class C(BaseConstants):
    NAME_IN_URL = 'Blindbox_auction'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 3
    products = [
        "Product A：这里是商品描述",
        "Product B",
        "Product C",
        "Product D",
        "Product E",
        "Product F：（盲盒商品）",
    ]  # 商品列表
    products2 = [
        "Product A：这里是商品描述",
        "Product B",
        "Product C",
        "Product D",
        "Product E",
        "Product F：（盲盒商品)",
    ]
    random.shuffle(products)
    random.shuffle(products2)
    products.extend(products2)
    print(products)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    auction_end = models.FloatField()
    # start with player 1 by default
    highest_bidder = models.IntegerField(initial=1)
    highest_bid = models.CurrencyField(initial=0)


class Player(BasePlayer):
    is_winner = models.BooleanField(initial=False)
    bid = models.CurrencyField(initial=0)
    # payoff = 120


# PAGES
class WaitToStart(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        group.auction_end = time.time() + 10  # 每轮拍卖时间


class Bidding(Page):
    @staticmethod
    def live_method(player: Player, data):
        group = player.group
        my_id = player.id_in_group
        is_new_high_bid = False

        if 'bid' in data:
            bid = data['bid']
            if bid <= 120:
                if bid > group.highest_bid:
                    player.bid = bid
                    group.highest_bid = bid
                    group.highest_bidder = my_id
                    is_new_high_bid = True

        return {
            0: dict(
                is_new_high_bid=is_new_high_bid,
                highest_bid=group.highest_bid,
                highest_bidder=group.highest_bidder,
            )
        }

    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)

    @staticmethod
    def get_timeout_seconds(player: Player):
        import time

        group = player.group
        return group.auction_end - time.time()

    @staticmethod
    def vars_for_template(player: Player):
        constants = C()
        products = constants.products
        product = products[player.round_number - 1]
        return {"product": product}


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        winner = group.get_player_by_id(group.highest_bidder)
        winner.is_winner = True
        winner.payoff = -group.highest_bid


class Results(Page):
    pass


class Survey(Page):
    pass


page_sequence = [WaitToStart, Bidding, ResultsWaitPage, Results]
