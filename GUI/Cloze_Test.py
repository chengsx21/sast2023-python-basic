import json
import streamlit as st

def read_articles(filename):
    """
    Read the articles from the file.

    :param filename: The file name of the articles.

    :return: A dict containing the articles.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data

def get_inputs(hints):
    """
    Get the user input.

    :param hints: Hints for the user input.

    :return: A list of user inputs.
    """
    keys = []
    for hint in hints:
        print(f"请输入{hint}:")
        keys.append(input())
    return keys

def replace(article, keys):
    """
    Replace the words in the article. 

    :param article: The article to be replaced.
    :param keys: The words to replace.

    :return: The article after replacement.

    """
    for i, key in enumerate(keys):
        article = article.replace(f"{{{{{i+1}}}}}", key)
    return article

if __name__ == "__main__":
    st.set_page_config(page_title="Cloze Test", page_icon=":100:", layout="wide", initial_sidebar_state="auto")
    st.markdown (""" <style> body { background-color: #ADD8E6; } </style> """, unsafe_allow_html=True)
    st.title("🏁 Cloze Test")
    st.image("https://s2.loli.net/2023/07/13/X4FbTBCtYmjscKr.jpg", use_column_width=True)
    st.subheader("""What is a "Cloze Test"?""")
    st.markdown(
        """
        **"Cloze Test"** is a simple little game. Specifically, the **question setter** prepares an article in
        advance and removes some words from it. For the **removed words**, the question setter provides
        certain **hints**, such as the word's part of *speech*, *connotation*, *type*, etc.
        """
    )
    st.subheader("""How to complete a "Cloze Test"?""")
    st.markdown(
        """
        The participants **cannot** see the **original article** and can only choose words **based on the
        provided hints**. Finally, the participants **fill in the blanks** with the chosen words, often
        achieving **humorous effects**. You can **compete with others** to see who can fill in the most 
        normal or absurd article. Additionally, this can also serve as a way to **learn foreign languages**
        and **expand vocabulary**.
        """
    )
    st.markdown("---")

    column1, column2, column3 = st.columns(3)
    with column1:
        st.info('**Idea: [@Monitoring Tool](https://cross-chain-monitoring.streamlit.app/)**', icon="💡")
    with column2:
        st.info('**GitHub: [@chengsx21](https://github.com/chengsx21)**', icon="💻")
    with column3:
        st.info('**Mail: [@chengsx21](mailto:chengsx21@gmail.com)**', icon="📮")

    st.sidebar.write("#### Game Buddy")
    st.sidebar.image("images/4.gif", caption="Kamisato Ayaka", use_column_width=True)
