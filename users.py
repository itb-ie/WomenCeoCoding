import pandas
from matplotlib import pylab as plt

'''
users = [{"ceo":"mtbarra", "company":"GM"},
         {"ceo":"Corie_Barry", "company":"BestBuy"},
         {"ceo":"BethFordLOL", "company":"LandOLakesKtchn"},
         {"ceo":"poppepk", "company":"ConsumersEnergy"},
         {"ceo":"LisaSu", "company":"AMD"}]

'''

# need to define new users loaded from excel
path = "C:/personal projects/women ceos/Women-CEO-Companies-Twitter.xlsx"

df = pandas.read_excel(path)
#users = df["Company Twitter"]
users = df["Competitor Company Twitter"]
if __name__ == "__main__":
    for user in users:
        if user is plt.np.nan:
            print("Asta e teapa")
        else:
            print(type(user), user)

