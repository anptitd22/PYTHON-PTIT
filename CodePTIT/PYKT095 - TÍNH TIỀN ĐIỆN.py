class Bill:
    def __init__(self,id,name,expense):
        self.id='KH'+format(id,'02d')
        a=name.split()
        self.name=' '.join(a).title()
        self.type,self.findex,self.lindex=expense.split()
        self.findex=int(self.findex)
        self.lindex=int(self.lindex)
        self.price_range=0
        self.price_outrange=0
        self.price=0
        self.vat=0
        if self.type=='A':
            res=self.lindex-self.findex
            if res <=100:
                self.price_range=self.price=res*450
            else:
                self.price_range=100*450
                self.price_outrange=tmp=(res-100)*1000
                self.price= tmp + tmp//20 + 100*450
                self.vat=tmp//20
        elif self.type=='B':
            res=self.lindex-self.findex
            if res <=500:
                self.price_range=self.price=res*450
            else:
                self.price_range=500*450
                self.price_outrange= tmp=(res-500)*1000
                self.price= tmp + tmp//20 + 500*450
                self.vat=tmp//20
        else:
            res=self.lindex-self.findex
            if res <=200:
                self.price_range=self.price=res*450
            else:
                self.price_range=200*450
                self.price_outrange=tmp=(res-200)*1000
                self.price= tmp + tmp//20 + 200*450
                self.vat=tmp//20
    def __str__(self):
        return self.id+' '+self.name+' '+f'{self.price_range} {self.price_outrange} {self.vat} {self.price}'
a=[]
for i in range(int(input())):
    a.append(Bill(i+1,input().strip(),input()))
a.sort(key=lambda x: -x.price)
for x in a:
    print(x)     