import pandas as pd
import streamlit as st
import pickle
import matplotlib.pyplot as plt
from htmlTemplates import inputform

st.title("Button Linked to Image Example")
from PIL import Image
# Define images

# st.write(inputform)
# st.markdown(inputform)
image1 = Image.open('img1.png')
image2 = Image.open('img2.png')
image3 = Image.open('img3.png')
image4 = Image.open('img4.png')
image5 = Image.open('img5.png')
image6 = Image.open('img6.png')
image7 = Image.open('img7.png')
image8 = Image.open('img8.png')
image9 = Image.open('img9.png')

# Add buttons
button1 = st.button("Show Image 1")
button2 = st.button("Show Image 2")
button3 = st.button("Show Image 3")
button4 = st.button("Show Image 4")
button5 = st.button("Show Image 5")
button6 = st.button("Show Image 6")
button7 = st.button("Show Image 7")
button8 = st.button("Show Image 8")
button9 = st.button("Show Image 9")

# Display image based on button click
if button1:
    st.image(image1, caption="Image 1", use_column_width=True)
elif button2:
    st.image(image2, caption="Image 2", use_column_width=True)
elif button3:
    st.image(image3, caption="Image 3", use_column_width=True)
elif button4:
    st.image(image4, caption="Image 4", use_column_width=True)
elif button5:
    st.image(image5, caption="Image 5", use_column_width=True)
elif button6:
    st.image(image6, caption="Image 6", use_column_width=True)
elif button7:
    st.image(image7, caption="Image 7", use_column_width=True)
elif button8:
    st.image(image8, caption="Image 8", use_column_width=True)
elif button9:
    st.image(image9, caption="Image 9", use_column_width=True)





st.title("Match Winner Prediction")

# Define teams
teams = ['Team1', 'Team2']

# Get user input for match prediction
st.session_state.selected_team = st.radio("Select the team you think will win:", teams)

# Display the user's prediction
# if st.button("Submit Prediction"):
#     st.success(f"Your prediction: {selected_team} will win!")
# else:
#     st.warning("Click the 'Submit Prediction' button to submit your prediction.")


print("")


df = pd.read_csv('Feature_table.csv')

with open('logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)




st.title("Match Outcome Prediction")


with st.form("Match Prediction"):
    # Add input fields to the form
    team1 = st.text_input("Enter Team 1:")
    team2 = st.text_input("Enter Team 2:")

    # Add a submit button
    submitted = st.form_submit_button("Submit")
# Add input fields for user to input team names
if submitted:
    row_loc = df.loc[(df['HomeTeam'] == team1) & (df['AwayTeam'] == team2)]
    model_input = row_loc[['HAS','HDS','AAS','ADS','HST','AST','HC','AC']]
    print(model_input)

    prediction = model.predict(model_input)
    if prediction[0] == 1:
        if(st.session_state.selected_team=='Team1'):
            st.write(f"Predicted Outcome: {team1} will win")
            st.warning(f" you lose the prediction")
        else:
            st.write(f"Predicted Outcome: {team1} will win")
            st.warning(f" you win the prediction")

    if prediction[0] == 0:
        if(st.session_state.selected_team=='Team2'):
            st.write(f"Predicted Outcome: {team2} will win")
            st.warning(f" you win the prediction")
        else:
            st.write(f"Predicted Outcome: {team2} will win")
            st.warning(f" you lose the prediction")
        #st.write(f"Predicted Outcome: {team1} will Lose")





