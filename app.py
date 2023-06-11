import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import emoji


st.set_page_config(page_title="Whatsapp Chat Analyzer", page_icon=":bar_chart:", layout="wide")
st.header("Welcome to my app!")
st.text("The below is default chat text. Please select Show analysis button to view the default chat analysis.")
st.text("Please provide the file by uploading it so that it can perform the desired chat text analysis for you.")

st.sidebar.title("whatsapp-chat-analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file (please upload whatsapp chat text)")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    # st.text(data)
    df = preprocessor.preprocess(data)
else:
    f= open('my_text.txt','r', encoding='utf-8')
    data=f.read()
    df = preprocessor.preprocess(data)
    df = df[df['User_name'].str.contains(r'^[A-Za-z\s]+$')]
    df=df[df['User_name']!="Puchii"]
    df = df[df['User_name'] != "piklu"]
st.dataframe(df)
user_list = df['User_name'].unique().tolist()
user_list.sort()
user_list.insert(0, "Overall")

selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

if st.sidebar.button("Show Analysis"):
        # Stats Area
        num_messages, words, media, links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total media")
            st.title(media)
        with col4:
            st.header("Total Links")
            st.title(links)

        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
            #wordcloud


        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)
        col1, col2 = st.columns(2)

        # most common words
        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots()

        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation='vertical')

        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")
        st.dataframe(emoji_df)






        st.title('Most commmon words')
        st.pyplot(fig)

        with col1:

      # monthly analysis
            st.title("Monthly Timeline")
            timeline = helper.monthly_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['Messages'], color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:

            #Daily timeline
            st.title("Daily Timeline")
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['Date'], daily_timeline['Messages'], color='black')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("weekly activity analysis")
        col1, col2= st.columns(2)

        with col1:

            user_heatmap = helper.activity_heatmap(selected_user, df)
            fig, ax = plt.subplots()
            ax = sns.heatmap(user_heatmap)
            st.pyplot(fig)
        with col2:

            temp = helper.user_basis(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(temp['day_name'], temp['Messages'], color='black')
            st.pyplot(fig)




