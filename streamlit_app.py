import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
# Create tabs
st.sidebar.image("images2.png")
tabs = ["Chat Analyzer", "About", "Instructions", "Contact"]
selected_tab = st.sidebar.radio("Navigation", tabs)

# Display content based on selected tab
if selected_tab == "Chat Analyzer":
    # Code for the main Chat Analyzer page
    st.title("WhatsApp Chat Analyzer")
    st.markdown('''
    <style>
    #about-text {
      font-family: Arial, sans-serif;
      font-size: 16px;
      line-height: 1.5;
    }
    </style>

    <div id="about-text">
   The WhatsApp Chat Analyzer is a valuable tool that allows users to gain insights from their WhatsApp chat data. 📊 By analyzing various aspects of the chat, such as message count, word count, media shared, and links exchanged, users can understand their communication patterns and overall engagement. 📈 This information can be visualized through interactive charts and graphs, making it easier to grasp the dynamics of the conversations. 📊📈

The app also offers features to analyze the chat timeline, allowing users to identify peak periods of communication and detect any emerging trends or patterns. ⏰ Additionally, the analysis of emoji usage provides insights into the emotions and sentiments expressed during conversations. 🎭 By examining the frequency and variety of emojis used by different users, users can gain a deeper understanding of the emotional dynamics within the chats. 😄❤️

For businesses, the ability to export and analyze user data can be highly valuable. 🔍📈 By analyzing user behavior, preferences, and trends, companies can make informed decisions and tailor their products and services to better meet customer needs. 💼 Data analysis enables businesses to identify growth opportunities, optimize marketing strategies, and enhance overall customer satisfaction. 💡📈 Ultimately, the insights gained from analyzing user data can drive customer engagement, loyalty, and revenue generation. 💪💰

Overall, the WhatsApp Chat Analyzer is a user-friendly and powerful tool that empowers both individuals and businesses to uncover hidden trends, discover communication patterns, and gain valuable insights from WhatsApp chat data. 💻📊 Start analyzing your WhatsApp chats today and unlock the power of data-driven insights! 🔓💡
    </div>
    ''', unsafe_allow_html=True)
    # Rest of the code for the Chat Analyzer page
elif selected_tab == "About":
    st.title("About")
    st.write("why did I make this application?")
    st.write(
        "In today's digital age, data analysis has become crucial for businesses to make informed decisions and drive growth. By analyzing user data, companies can gain valuable insights into customer behavior, preferences, and trends.")
    st.write(
        "With the help of applications like this, you can extract useful information from your WhatsApp chats, such as message statistics, media sharing patterns, activity timelines, and even sentiment analysis. This data can provide valuable insights into your communication patterns, helping you understand your interactions better.")
    st.write(
        "From a business perspective, the analysis of user data can be instrumental in monetizing a company. By understanding customer preferences and behavior, companies can optimize their marketing strategies, personalize their offerings, and improve customer satisfaction. This, in turn, can lead to increased customer loyalty, retention, and ultimately, revenue.")
    st.write(
        "Whether you are an individual looking to gain insights from your personal WhatsApp chats or a business seeking to leverage user data for growth, the WhatsApp Chat Analyzer can assist you in unlocking valuable information.")

    # Rest of the code for the About page
elif selected_tab == "Instructions":
    # Code for the Instructions page
    st.title("Instructions")
    st.write("Here are the instructions on how to use this app:")
    st.write("1. Export the chat from WhatsApp:")
    st.write("        a. Open the WhatsApp chat you want to analyze.")
    st.write("        b. Tap the three-dot menu on the top-right corner.")
    st.write("        c. Select 'More' and then 'Export chat'.")
    st.write("        d. Choose exclude media.")
    st.write("        e. Select the sharing method (e.g., email, cloud storage).")
    st.write("        f. Share the exported chat file to your computer or device.")
    st.write("2. Upload the exported chat file using the file uploader on the sidebar.")
    st.write("3. Select the user you want to analyze.")
    st.write("4. Click on 'Show Analysis' to generate insights.")

elif selected_tab == "Contact":
    st.title("Contact")
    st.write("For any inquiries or support, please feel free to contact me:")
    st.write("Linkedin: https://www.linkedin.com/in/muhammed-usman-224188134/")
    st.write("Phone: 0123103231")
    st.write("Email: uthmanalfaris@gmail.com")
    # Additional contact information or form can be added here
st.sidebar.image("1658587266245.jpg")
st.sidebar.markdown('<p style="font-family: Arial; color: #DAA520;">Muhammad Usman</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="font-family: Arial; color: #DAA520;">Univeristy Malaya</p>', unsafe_allow_html=True)
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        plt.title("Monthly Timeline", fontdict={'family': 'Arial', 'size': 16})
        plt.xlabel("Time", fontdict={'family': 'Arial', 'size': 14})
        plt.ylabel("Number of Messages", fontdict={'family': 'Arial', 'size': 14})
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        ax.grid(True)
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        plt.title("Daily Timeline", fontdict={'family': 'Arial', 'size': 16})
        plt.xlabel("Date", fontdict={'family': 'Arial', 'size': 14})
        plt.ylabel("Number of Messages", fontdict={'family': 'Arial', 'size': 14})
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        ax.grid(True)
        st.pyplot(fig)

        # activity map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation='vertical')
            plt.title("Most Busy Day", fontdict={'family': 'Arial', 'size': 16})
            plt.xlabel("Day", fontdict={'family': 'Arial', 'size': 14})
            plt.ylabel("Number of Messages", fontdict={'family': 'Arial', 'size': 14})
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            ax.grid(True)
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            plt.title("Most Busy Month", fontdict={'family': 'Arial', 'size': 16})
            plt.xlabel("Month", fontdict={'family': 'Arial', 'size': 14})
            plt.ylabel("Number of Messages", fontdict={'family': 'Arial', 'size': 14})
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            ax.grid(True)
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax = sns.heatmap(user_heatmap)
        plt.title("Weekly Activity Map", fontdict={'family': 'Arial', 'size': 16})
        plt.xlabel("Weekday", fontdict={'family': 'Arial', 'size': 14})
        plt.ylabel("Hour of Day", fontdict={'family': 'Arial', 'size': 14})
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        st.pyplot(fig)

        # finding the busiest users in the group (Group level)
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots(figsize=(10, 6))

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                plt.title("Most Busy Users", fontdict={'family': 'Arial', 'size': 16})
                plt.xlabel("User", fontdict={'family': 'Arial', 'size': 14})
                plt.ylabel("Number of Messages", fontdict={'family': 'Arial', 'size': 14})
                plt.xticks(fontsize=12)
                plt.yticks(fontsize=12)
                ax.grid(True)
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # WordCloud
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(df_wc)
        plt.title("Wordcloud", fontdict={'family': 'Arial', 'size': 16})
        plt.axis('off')
        st.pyplot(fig)

        # most common words
        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation='vertical')
        plt.title('Most Common Words', fontdict={'family': 'Arial', 'size': 16})
        plt.xlabel("Frequency", fontdict={'family': 'Arial', 'size': 14})
        plt.ylabel("Word", fontdict={'family': 'Arial', 'size': 14})
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        ax.grid(True)
        st.pyplot(fig)

        # emoji analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
            plt.title("Top Emojis", fontdict={'family': 'Arial', 'size': 16})
            st.pyplot(fig)
