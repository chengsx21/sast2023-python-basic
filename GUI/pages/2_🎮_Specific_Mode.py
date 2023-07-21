import json
import pyperclip
import re
import streamlit as st
import time  

def choose_article():
    st.session_state["chosen"] = True
    
def replay_game():
    for i in range(len(st.session_state["article"]["hints"])):
        st.session_state[f"input_{i}"] = ""

def restart_game():
    replay_game()
    st.session_state.pop("chosen", None)
    st.session_state.pop("first_time", None)

if __name__ == "__main__":
    st.set_page_config(page_title="Cloze Test", page_icon=":100:", layout="wide", initial_sidebar_state="auto")
    st.title("🎮 Specific Mode")
    st.info("You can specify a specific article for the game!", icon="🔥")
    st.sidebar.write("#### Game Buddy")
    st.sidebar.image("GUI/images/2.gif", caption="Kawaii Paimon", use_column_width=True)

    if "chosen" not in st.session_state:
        # article_lang = "English"

        c1, c2 = st.columns([1, 2])
        with c1:
            st.session_state["article_lang"] = st.radio("Choose the language:", ["English", "Chinese"], horizontal=True)
        with open("GUI/example.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                if item["language"] == "en":
                    en_articles = item["articles"]
                if item["language"] == "zh":
                    zh_articles = item["articles"]
        with c2:
            if st.session_state["article_lang"] == "English":
                st.session_state["articles"] = en_articles
                article_index = st.number_input(f"Choose an English article ({len(en_articles)} in total):", 1, len(en_articles))
            else:
                st.session_state["articles"] = zh_articles
                article_index = st.number_input(f"Choose an Chinese article ({len(zh_articles)} in total):", 1, len(zh_articles))
        st.write(f"### You Choose:\n*{st.session_state['articles'][article_index - 1]['title']}*")
        st.session_state["article"] = st.session_state['articles'][article_index - 1]
        st.button("Submit", use_container_width=True, on_click=choose_article)
    if "chosen" in st.session_state:
        with st.form(key="submit-form"):
            blanks = []
            article_with_blanks = ""
            if "first_time" not in st.session_state:
                with st.spinner("Loading..."):
                    time.sleep(1)
                st.session_state["article_with_blanks"] = ""
                st.session_state["first_time"] = True
            st.write(f"### Title\n*{st.session_state['article']['title']}*")
            st.write(f"### Article\n{st.session_state['article']['article']}")
            st.write("### Answer")
            hints = st.session_state["article"]["hints"]
            with st.expander("##### Choose words to fill in blanks:\nDo whatever you want!"):
                index = 0
                while index < len(st.session_state["article"]["hints"]):
                    index += 1
                    blank = st.text_input(f"##### Hint {index}\n{hints[index-1]}", key=f"input_{index-1}")
                    if blank:
                        blanks.append(blank)
            column4, column5, column6 = st.columns([1, 1, 1])
            placeholder1 = st.empty()

            placeholder2 = st.empty()
            c = placeholder2.container()
            c.markdown("---")
            c1, c2, c3 = c.columns([1, 1, 1])
            with c1:
                replay_button = st.form_submit_button("Replay", use_container_width=True, on_click=replay_game)
            with c2:
                restart_button = st.form_submit_button("Restart", use_container_width=True, on_click=restart_game)
            with c3:
                copy_button = st.form_submit_button("Copy", use_container_width=True)
                if copy_button:
                    if st.session_state["article_with_blanks"] == "":
                        st.warning("⚠️ Error! Submit first!")
                    else:
                        pyperclip.copy(st.session_state["article_with_blanks"])
                        st.session_state["article_with_blanks"] = ""

            with column5:
                button = st.empty()
                submit_button = button.form_submit_button("Submit", use_container_width=True)
                if submit_button:
                    if len(blanks) != len(st.session_state["article"]["hints"]):
                        placeholder1.empty()
                        st.error("Please fill in all blanks!")
                        st.stop()

                    article_with_blanks = st.session_state["article"]["article"]
                    for i, blank in enumerate(blanks):
                        pattern = re.compile(re.escape(f"{{{{{i+1}}}}}"))
                        article_with_blanks = pattern.sub(blank, article_with_blanks, count=1)
                    c = placeholder1.container()
                    c.write("### *Congratulations! You've finished the game!*")
                    c.success(article_with_blanks)
                    st.session_state["article_with_blanks"] = article_with_blanks
                    button.form_submit_button("Success", use_container_width=True, disabled=True)
