class Product(object):
    def __init__(self,price, item_name, weight, brand,cost):
        print "We have products!"
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.cost=cost
        self.status="for sale"
        if price == 0:
            self.status = "sold"
        if cost == str("return"):
            self.status="return"
            self.price= 0
        if cost == str("returning with box"):
            self.status ="like new"
        if cost <=str("returning open box"):
            self.price = (self.price -(self.price*2))
    def display_all(self):
        print "This", self.brand, self.item_name, "costs", self.price, "dollars and is", self.status
        return self
    # def sell_status(self):
    #     if self.price>0:
    #         self.status="sold"
    #     print self.status
    #     return self
    def add_tax(self, tax):
        self.tax=tax
        self.price= (1+tax) * self.price
        print self.price
        return self
    # def product_return(self, reason_for_return, changes):
    #     self.reason_for_return=reason_for_return
    #     self.changes=changes
first_product=Product(2,"soap", 1, "Dove","returning with box")
first_product.display_all().add_tax(0.12)
