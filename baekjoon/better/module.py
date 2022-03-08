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
    all_in = set()

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
        player.cur_bet += min(self.base_bet, player.money)

    def remove_bet(self, p_idx):
        player = self.player_arr[p_idx]
        player.cur_bet -= min(self.base_bet, player.cur_bet)

    def confirm_bet(self, p_idx):
        player = self.player_arr[p_idx]
        player.tot_bet += player.cur_bet
        player.money -= player.cur_bet
        if player.money == 0:
            self.all_in.add([p_idx, player.tot_bet])
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
