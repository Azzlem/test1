class Transaction():
    def __init__(self, id_, state, date, amount, name, code, description,  to_, from_=""):
        self.id = id_
        self.state = state
        self.date = date
        self.amount = amount
        self.name = name
        self.code = code
        self.description = description
        self.to_ = to_
        self.from_ = from_
