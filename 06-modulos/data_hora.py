from datetime import datetime
from pytz import timezone
# data = datetime(2022, 4, 20, 7, 49, 23)
# print(data)
#  2022-04-20 07:49:23

data_str_data = '2022-04-20 07:49:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'
data_br = '15/01/2024'
# data_str_fmt_br = '%d/%m/%Y'

# data = datetime.strptime(data_str_data, data_str_fmt)
# print(data)

data_br = datetime.strptime(data_br, data_str_fmt_br)
# print(data_br)

print(datetime.now())

print(datetime.now(timezone('America/Sao_Paulo')))

from datetime import datetime
from dateutil.relativedelta import relativedelta

print(datetime.now() + relativedelta(seconds=60))


print(data_str_data.strftime('%d%m%Y'))
