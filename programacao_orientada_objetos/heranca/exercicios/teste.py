from datetime import date

# data1 = date(year=2023, month=2, day=9)
# print(data1, sep='/')

data_atual = date.today()
data_brasileira = data_atual.strftime('%x')
print(data_brasileira)