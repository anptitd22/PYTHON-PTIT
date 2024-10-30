class Bill:
    def __init__(self,id,name,quantity,unit_price,vat):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.unit_price=unit_price
        self.vat=vat
        self.price=self.unit_price*self.quantity-self.vat
    def __str__(self):
        return self.id+' '+self.name+' '+f'{self.quantity} {self.unit_price} {self.vat} {self.price}'
a=[]
for i in range(int(input())):
    a.append(Bill(input(),input(),int(input()),int(input()),int(input())))
a.sort(key=lambda x: -x.price)
for x in a:
    print(x)         