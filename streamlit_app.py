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
    Welcome to the WhatsApp Chat Analyzer! This powerful application allows you to gain valuable insights from your WhatsApp chat data. By simply uploading your chat file, you can unlock a wealth of information about your conversations, providing you with a deeper understanding of your communication patterns.

    With the WhatsApp Chat Analyzer, you can explore various aspects of your chat data. The app provides you with comprehensive statistics such as the total number of messages, words, media shared, and links exchanged. By visualizing this data, you can quickly grasp the overall activity and engagement within your chat.

    Furthermore, the app enables you to analyze your chat timeline on both monthly and daily scales. By plotting the number of messages over time, you can identify peak periods of communication and observe any trends or patterns that may emerge. This information can be invaluable for understanding the dynamics of your group or individual conversations.

    The WhatsApp Chat Analyzer also offers interactive visualizations, such as activity maps and word clouds. Activity maps help you visualize the busiest days and months, giving you insights into when the conversation is most active. Word clouds provide a visual representation of the most frequently used words, giving you a glimpse into the topics that dominate your chats.

    Additionally, the app allows you to explore emoji usage in your chats. By analyzing the frequency and variety of emojis used by different users, you can gain insights into the emotions and sentiments expressed during conversations.

    By leveraging the power of data analysis and visualization, the WhatsApp Chat Analyzer empowers you to uncover hidden trends, discover communication patterns, and gain a deeper understanding of your chat data. Whether you're analyzing group dynamics, evaluating your own communication habits, or simply curious about the insights hidden within your chats, this app provides a user-friendly and intuitive interface for exploring and interpreting your WhatsApp data.

    Furthermore, the ability to export and analyze user data has become increasingly valuable for businesses. By analyzing user behavior, preferences, and trends, companies can make informed decisions and tailor their products and services to meet customer needs. Data analysis enables businesses to identify opportunities for growth, optimize marketing strategies, and improve overall customer satisfaction. The insights gained from analyzing user data can ultimately drive monetization efforts by increasing customer engagement, loyalty, and revenue.

    With the WhatsApp Chat Analyzer and applications like it, users and businesses alike can harness the power of data analysis to extract valuable insights from user data. Start analyzing your WhatsApp chats today and unlock the power of data-driven insights!
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
