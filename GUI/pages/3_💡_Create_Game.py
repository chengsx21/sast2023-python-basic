import json
import re
import streamlit as st

if __name__ == "__main__":
    st.set_page_config(page_title="Cloze Test", page_icon=":100:", layout="wide", initial_sidebar_state="auto")
    st.title("💡 Create Game")
    st.sidebar.write("#### Game Buddy")
    st.sidebar.image("images/3.gif", caption="Kawaii Paimon", use_column_width=True)


    c1, c2 = st.columns(2)
    with c1:
        st.info("Note that the word to be removed will be the first matched word!", icon="🔥")
    with c2:
        st.warning("Make sure that the chosen word is unique!", icon="🚨")

    st.write("##### Step 1")
    c1, c2 = st.columns([2, 1], gap="large")
    with c1:
        article_title = st.text_input("Input the title:")
    with c2:
        article_lang = st.radio("Choose the language:", ["English", "Chinese"], horizontal=True)
    article = st.text_area("Input your article here:", height=200)

    blanks = []
    hints = []

    column1, column2 = st.columns([1, 2])
    with column1:
        num_words = st.slider("##### Step 2\nPick a number for words to be remove:" , min_value=3, max_value=8)
    with column2:
        with st.expander("##### Step 3\nChoose words and add unique hints:"):
            index = 0
            while index < num_words:
                index += 1
                c1, c2 = st.columns(2)
                with c1:
                    blank = st.text_input(f"Word {index}")
                    if blank:
                        blanks.append(blank)
                with c2:
                    hint = st.text_input(f"Hint {index}")
                    if hint:
                        hints.append(hint)

    column4, column5, column6 = st.columns([1, 2, 1])
    placeholder = st.empty()

    with column5:
        button = st.empty()
        submit_button = button.button("Submit", use_container_width=True)
        if submit_button:
            if not article_title:
                placeholder.empty()
                st.error("Please input your title!")
                st.stop()
            if not article:
                placeholder.empty()
                st.error("Please input your article!")
                st.stop()
            if len(blanks) != num_words or len(hints) != num_words:
                placeholder.empty()
                st.error("Please fill in all blanks and hints!")
                st.stop()

            article_with_blanks = article
            article_copied = article
            for i, blank in enumerate(blanks):
                pattern = re.compile(re.escape(blank), re.IGNORECASE)
                article_with_blanks = pattern.sub(f"{{{{{i+1}}}}}", article_copied, count=1)
                if article_with_blanks == article_copied:
                    placeholder.empty()
                    st.error(f"Word \"{blank}\" not found!")
                    st.stop()
                article_copied = article_with_blanks
            c = placeholder.container()
            c.write("##### Step 4\nThe article with blanks:")
            c.success(article_with_blanks)
            for i, hint in enumerate(hints):
                c.write(f"Hint {i+1}. {hint}")
            button.button("Success", use_container_width=True, disabled=True)

            with open("example.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                new_article = {
                    "title": article_title,
                    "article": article_with_blanks,
                    "hints": hints
                }
                for item in data:
                    if item["language"] == "en" and article_lang == "English":
                        item["articles"].append(new_article)
                    if item["language"] == "zh" and article_lang == "Chinese":
                        item["articles"].append(new_article)

            with open("example.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
