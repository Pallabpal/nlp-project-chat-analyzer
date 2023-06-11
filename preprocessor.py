import pandas as pd
import re
def preprocess(data):
    pattern1='(\d{1,2}\/\d{1,2}\/\d{1,2}, \d{1,2}:\d{1,2}[^ -]+) - ([\w+\s]+):([^\n]+)'



    dates = re.findall(pattern1, data)
    time_date = []
    message = []
    user_name = []

    for i in range(len(dates)):
        time_date.append(dates[i][0])
        user_name.append(dates[i][1])
        message.append(dates[i][2])

    df = pd.DataFrame({'Time_Date': time_date, 'User_name': user_name, 'Messages': message})
    df['Time_Date'] = pd.to_datetime(df['Time_Date'])

    df['year'] = df['Time_Date'].dt.year
    df['month_num'] = df['Time_Date'].dt.month
    df['month'] = df['Time_Date'].dt.month_name()
    df['day'] = df['Time_Date'].dt.day
    df['hour'] = df['Time_Date'].dt.hour
    df['minute'] = df['Time_Date'].dt.minute
    df['Date'] = df['Time_Date'].dt.date
    df['day_name'] = df['Time_Date'].dt.day_name()
    period = []
    for hour in df[['day', 'hour']]['hour']:
        if hour == 12:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df['period'] = period

    return df
