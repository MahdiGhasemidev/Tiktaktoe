import streamlit as st 
from main import TikTakToe
import random

st.write('Welcome to TikTakToe :video_game:')


if 'game' not in st.session_state:
    st.session_state.game = TikTakToe()

game = st.session_state.game


if game.player_choice is None:
    choice = st.radio("Choose your marker:", ['X', 'O'])
    if st.button("Start Game"):
        game.player_choice = choice
        game.computer_choice = 'O' if choice == 'X' else 'X'
        game.current_turn = 'player' if random.randint(0, 1) == 0 else 'computer'
        st.experimental_rerun()

if game.player_choice is not None:
    st.write(f"Your marker: {game.player_choice}")
    st.write(f"Computer marker: {game.computer_choice}")
    st.write(f"Current turn: {game.current_turn}")

    #* create board with for loop and using mod
    cols = st.columns(3)
    for i in range(1, 10):
        with cols[(i-1) % 3]:
            #* using empty square except numbers 1-9
            text = game.board[i] if game.board[i] and game.board[i] != ' ' else ''
            if st.button(text, key=i):
                #* player's turn
                if game.current_turn == 'player':
                    if game.fix_spot(i, game.player_choice):
                        winner = game.has_player_won()
                        if winner:
                            st.success(f"{winner.capitalize()} won!")
                            st.session_state.clear() #* Restarts the game
                        elif game.is_board_full():
                            st.warning("It's a tie!")
                            st.session_state.clear()
                        else:
                            game.current_turn = 'computer'
                            st.experimental_rerun()

    #* computer's turn
    if game.current_turn == 'computer':
        game.computer_move()
        winner = game.has_player_won()
        if winner:
            st.success(f"{winner.capitalize()} won!")
            st.session_state.clear()
        elif game.is_board_full():
            st.warning("It's a tie!")
            st.session_state.clear()
        else:
            game.current_turn = 'player'
            st.experimental_rerun()