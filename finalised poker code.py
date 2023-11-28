class Player:
    def __init__(self, name, buyin, cashout):
        self.name = name
        self.buyin = round(buyin, 2)
        self.cashout = round(cashout, 2)
        self.profit = cashout - buyin

        if self.profit < 0:
            self.loss = abs(self.profit)
        else:
            self.loss = 0


def total_buyin_equal_total_cashout(participants):
    tb, tc = 0, 0

    for player in participants:
        tb += player.buyin
        tc += player.cashout

    if tb == tc and tb != 0:
        return True
    else:
        print("Make total buyin equal to total cashout")
        return False


def calculate_payouts(participants):
    if total_buyin_equal_total_cashout(participants):

        out = []

        participants.sort(key=lambda x: x.profit, reverse=True)

        receiver = participants[0]
        giver = participants[-1]

        while participants and receiver != giver and receiver.profit and giver.loss:
            if receiver.profit == giver.loss:
                out.append(giver.name + " pays " + receiver.name + " " + str(round(giver.loss, 2)))
                participants.remove(giver)
                participants.remove(receiver)

                if participants:
                    receiver = participants[0]
                    giver = participants[-1]

            elif receiver.profit > giver.loss:
                out.append(giver.name + " pays " + receiver.name + " " + str(round(giver.loss, 2)))
                receiver.profit -= giver.loss
                participants.remove(giver)

                receiver = participants[0]
                giver = participants[-1]

            elif receiver.profit < giver.loss:
                out.append(giver.name + " pays " + receiver.name + " " + str(round(receiver.profit, 2)))
                giver.loss -= receiver.profit
                participants.remove(receiver)

                receiver = participants[0]
                giver = participants[-1]

        return out


Ethan = Player('Ethan', buyin=10, cashout=15)
Aidan = Player('Aidan', buyin=10, cashout=5)
Jon = Player('Jon', buyin=10, cashout=15)
Theo = Player('Theo', buyin=5, cashout=5)

participants = [Ethan, Aidan, Jon, Theo]

payouts = calculate_payouts(participants)
if payouts:
    print('Payouts:')
    for p in payouts:
        print(p)