class Atm(object):
    def __init__(self, CashWithdrawl, BalanceEnquiry):
        self.CashWithdrawl = CashWithdrawl
        self.BalanceEnquiry = BalanceEnquiry 
    def Withdaw(self):
        print("Moneyz")
    
    def Enquiry(self):
        print("Questionz")

AnAtmKilledHerHusband = Atm("$200","$0.05")
print(AnAtmKilledHerHusband.BalanceEnquiry)
