

class Wallet:

    def __init__(self, dollars):
        self.dollars = dollars 

    def __add__(self, other):
        if isinstance(other, Wallet):
            total_dollars = self.dollars + other.dollars 
        if isinstance(other, int):
            total_dollars = self.dollars + other
        return Wallet(total_dollars)

    def __str__(self):
        return f"${self.dollars}"


if __name__ == "__main__":
    wallet_1 = Wallet(10)
    wallet_2 = Wallet(20)
    wallet_3 = 30

    all_wallets = wallet_1 + wallet_2 + wallet_3

    print(all_wallets)
