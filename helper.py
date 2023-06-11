from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
import regex as re
extract = URLExtract()
f = open('stop_hinglish.txt', 'r')
stop_words = f.read()
def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['User_name'] == selected_user]
    num_messages = df.shape[0]

    # fetch word
    word=[]
    for messages in df['Messages']:
        word.extend(messages.split())

    # fetch links
    num_media_messages = df[df['Messages'] ==' <Media omitted>'].shape[0]

    #fetch url
    links = []
    for message in df['Messages']:
        links.extend(extract.find_urls(message))

    return df.shape[0], len(word), num_media_messages, len(links)
def most_busy_users(df):
    x = df['User_name'].value_counts().head()
    df = round((df['User_name'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'User_name': 'percentage'})
    return x,df
def create_wordcloud(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['User_name'] == selected_user]
    df = df[df['Messages'] != ' <Media omitted>']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='black')
    df['Messages'] = df['Messages'].apply(remove_stop_words)
    df_wc = wc.generate(df['Messages'].str.cat(sep=" "))
    return df_wc

def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User_name'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['Messages'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline
def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User_name'] == selected_user]

    daily_timeline = df.groupby('Date').count()['Messages'].reset_index()

    return daily_timeline
def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User_name'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User_name'] == selected_user]

    return df['month'].value_counts()
def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['User_name'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='Messages', aggfunc='count').fillna(0)

    return user_heatmap
def user_basis(selected_user, df):
    if selected_user != 'Overall':
      df = df[df['User_name'] == selected_user]


    df = df.groupby('day_name').count()['Messages'].reset_index()
    return df
def most_common_words(selected_user,df):



    if selected_user != 'Overall':
        df = df[df['User_name'] == selected_user]


    temp = df[df['Messages'] != ' <Media omitted>']

    words = []

    for message in temp['Messages']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df
def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['User_name'] == selected_user]

    emoji_pattern = re.compile(r'\p{Emoji}')

    emojis = []
    for message in df['Messages']:
        emoji_list = emoji_pattern.findall(message)
        emojis.extend(emoji_list)

    emoji_counts = pd.DataFrame(emojis).value_counts().reset_index()


    return emoji_counts






