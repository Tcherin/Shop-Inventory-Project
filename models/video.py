class Video:
    def __init__(self, title, genre, description, stock_quantity, buying_cost, selling_price, director, id=None):
        self.title = title
        self.genre = genre
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.director = director
        self.id = id