class Player:
    money = 0
    tot_bet = 0
    cur_bet = 0
    is_alive = True

    def __init__(self, init_money):
        self.money = init_money

    def reset(self):
        self.tot_bet = self.cur_bet = 0
        if self.money != 0:
            self.is_alive = True


class Pool:
    max_bet = 0
    base_bet = 0
    total_bet = 0

    player_num = 0
    player_arr = []

    def __init__(self, n, init_money, base):
        self.base_bet = base
        self.total_bet = 0
        self.player_num = n
        for i in range(n):
            self.player_arr.append(Player(init_money))

    def start_game(self):
        for player in self.player_arr:
            self.total_bet += self.base_bet
            player.money -= self.base_bet

    def die(self, p_idx):
        player = self.player_arr[p_idx]
        player.is_alive = False

    def half(self, p_idx):
        player = self.player_arr[p_idx]
        temp = self.total_bet // 2
        temp -= temp % self.base_bet
        player.cur_bet += min(temp, player.money)

    def quarter(self, p_idx):
        player = self.player_arr[p_idx]
        temp = self.total_bet // 4
        temp -= temp % self.base_bet
        player.cur_bet += min(temp, player.money)

    def call(self, p_idx):
        player = self.player_arr[p_idx]
        player.cur_bet = min(self.max_bet - player.tot_bet, player.money)

    def reset_bet(self, p_idx):
        player = self.player_arr[p_idx]
        player.cur_bet = 0

    def add_bet(self, p_idx):
        player = self.player_arr[p_idx]
        temp = self.total_bet // 2
        temp -= temp % self.base_bet
        player.cur_bet += min(self.base_bet, player.money)
        player.cur_bet = min(player.cur_bet, temp)

    def remove_bet(self, p_idx):
        player = self.player_arr[p_idx]
        player.cur_bet -= min(self.base_bet, player.cur_bet)

    def confirm_bet(self, p_idx):
        player = self.player_arr[p_idx]
        player.tot_bet += player.cur_bet
        player.money -= player.cur_bet
        self.total_bet += player.cur_bet
        player.cur_bet = 0
        self.max_bet = max(self.max_bet, player.tot_bet)

    def turn_change(self):
        self.max_bet = 0
        for player in self.player_arr:
            player.tot_bet = player.cur_bet = 0

    def end_game(self, winner_list):
        for winner in winner_list:
            player = self.player_arr[winner]
            player.money += self.total_bet // len(winner_list)
        self.max_bet = self.total_bet = 0
        for player in self.player_arr:
            player.reset()
        self.start_game()


if __name__ == '__main__':
    p = Pool(3, 10000, 100)
    p.start_game()
    for player in p.player_arr:
        if player.is_alive:
            print(player.money, player.is_alive)
    print(p.total_bet)
    p.add_bet(1)
    p.confirm_bet(1)
    p.half(2)
    p.confirm_bet(2)
    p.call(0)
    p.confirm_bet(0)
    p.call(1)
    p.confirm_bet(1)
    for player in p.player_arr:
        if player.is_alive:
            print(player.money, player.is_alive)
    p.turn_change()
    print(p.total_bet)

    p.confirm_bet(2)
    p.add_bet(0)
    p.confirm_bet(0)
    p.call(1)
    p.confirm_bet(1)
    p.call(2)
    p.confirm_bet(2)
    for player in p.player_arr:
        if player.is_alive:
            print(player.money, player.is_alive)
    p.turn_change()
    print(p.total_bet)

    p.end_game([1])
    for player in p.player_arr:
        if player.is_alive:
            print(player.money, player.is_alive)
    print(p.total_bet)
