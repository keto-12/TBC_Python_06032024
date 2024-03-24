#Task3
# 3.	დაწერეთ პროგრამა რომელიც მიიღებს თარიღს.
# Პროგრამამ თარიღი უნდა გადაიყვანოს განსხვავებულ ფორმატში და დაბეჭდოს ეკრანზე.
# Შემომავალი და გამომავალი თარიღების ფორმატები იხილეთ მაგალითებში. Შემომავალი სტრიქონის ფორმატის განმარტება:
#  მაგალითი 1.
# 	Input: 2024-03-22T19:17:42.956376+00:00
# 	Output: 22-03-2024 7:17:42 +0
# მაგალითი 2.
# 	Input: 2024-03-04T11:17:42.000123+04:00
# 	Output: 04-03-2024 11:17:42 +4
# მაგალითი 3.
# 	Input: 2024-11-14T15:17:42.123000-03:00

import datetime

offset = datetime.timedelta(hours=0)
datetime.timedelta(seconds=3600)

time_now = datetime.datetime.now(datetime.timezone(offset))
#print(time_now)

input_format=datetime.datetime.isoformat(time_now)
print(input_format)

output_format = datetime.datetime.strptime(input_format[:],"%d-%m-%Y ' ' %H-%M-%S")# აქ დავიბენი :)

print(output_format)
