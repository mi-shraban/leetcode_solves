class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.size = len(balance)

    def transfer(self, a1: int, a2: int, money: int) -> bool:
        if a1-1 >= self.size or a2-1 >= self.size or self.balance[a1-1] < money:
            return False
        self.balance[a1-1] -= money
        self.balance[a2-1] += money
        return True

    def deposit(self, a: int, money: int) -> bool:
        if a-1 >= self.size:
            return False
        self.balance[a-1] += money
        return True

    def withdraw(self, a: int, money: int) -> bool:
        if a-1 >= self.size or self.balance[a-1] < money:
            return False
        self.balance[a-1] -= money
        return True