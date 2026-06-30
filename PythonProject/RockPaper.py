# import random

# def game():
#     system_choice = ["rock", "paper", "scissor"]
#     system = random.choice(system_choice)
#     user_choice = input("Enter rock, paper or scissor: ").lower()
#     print("Computer chose:", system)
#     if user_choice == system:
#         print("TIE")

#     elif user_choice == "rock" and system == "scissor":
#         print("You win")

#     elif user_choice == "paper" and system == "rock":
#         print("You win")

#     elif user_choice == "scissor" and system == "paper":
#         print("You win")

#     elif user_choice in system_choice:
#         print("Computer wins")

#     else:
#         print("Invalid input")
# print("🎮 You are playing Round 1")
# game()
# print("\n🎮 You are playing Round 2")
# game()
# print("\n🎮 You are playing Round 3")
# game()



# python -m streamlit run Rockpaper.py


import streamlit as st
import random

# Session State
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "round" not in st.session_state:
    st.session_state.round = 1

# Title
st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮")
st.title("🎮 Rock Paper Scissors Game")
st.write("### Play against the Computer!")

# Game Function
def game(user_choice):
    system_choice = ["rock", "paper", "scissor"]
    computer = random.choice(system_choice)

    st.write(f"🤖 **Computer chose:** {computer.capitalize()}")

    if user_choice == computer:
        st.info("🤝 It's a Tie!")

    elif (
        (user_choice == "rock" and computer == "scissor") or
        (user_choice == "paper" and computer == "rock") or
        (user_choice == "scissor" and computer == "paper")
    ):
        st.success("🎉 You Win this Round!")
        st.session_state.user_score += 1

    else:
        st.error("💻 Computer Wins this Round!")
        st.session_state.computer_score += 1

# Round Display
st.subheader(f"🎯 Round {st.session_state.round}")

# Choice
choice = st.radio(
    "Choose one:",
    ["rock", "paper", "scissor"],
    horizontal=True
)   

# Play Button
if st.button("🎮 PLAY NOW 🎮", use_container_width=True):
    game(choice)

    st.markdown("---")
    st.subheader("🏆 Score Board")
    st.write(f"🙋 User: **{st.session_state.user_score}**")
    st.write(f"🤖 Computer: **{st.session_state.computer_score}**")

    if st.session_state.round < 3:
        st.session_state.round += 1
    else:
        st.markdown("---")
        st.header("🎮 Game Over")

        if st.session_state.user_score > st.session_state.computer_score:
            st.balloons()
            st.success("🏆 Congratulations! You Won the Game!")

        elif st.session_state.computer_score > st.session_state.user_score:
            st.error("🤖 Computer Won the Game!")

        else:
            st.warning("🤝 Match Draw!")
    game(choice)

    st.markdown("---")
    st.subheader("🏆 Score Board")
    st.write(f"🙋 User: **{st.session_state.user_score}**")
    st.write(f"🤖 Computer: **{st.session_state.computer_score}**")

    if st.session_state.round < 3:
        st.session_state.round += 1
    else:
        st.markdown("---")
        st.header("🎮 Game Over")

        if st.session_state.user_score > st.session_state.computer_score:
            st.balloons()
            st.success("🎉 Congratulations! You Won the Game!")

        elif st.session_state.computer_score > st.session_state.user_score:
            st.error("🤖 Computer Won the Game!")

        else:
            st.warning("🤝 The Game is Draw!")

# Restart Button
if st.button("🔄 Restart Game"):    
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.round = 1
    st.rerun()