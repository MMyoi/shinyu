import streamlit as st

st.title("Quiz App")

questions = [
    "What is the capital of France?",
    "What is the currency of Japan?",
    "What is the largest ocean in the world?",
]

options = [
    ["Paris", "Rome", "London", "Berlin"],
    ["Yen", "Dollar", "Euro", "Pound"],
    ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
]

correct_answers = [0, 0, 0]

score = 0

for i in range(len(questions)):
    st.write(questions[i])
    user_answer = st.selectbox("Select an option", options[i])
    if user_answer == options[i][correct_answers[i]]:
        st.success("Correct!")
        score += 1
    else:
        st.error("Incorrect!")

st.write("Your score is:", score)
