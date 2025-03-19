# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# st.set_page_config(page_title=="Data Sweeper" ,layout="wide")

# #css
# st.markdown(

#     """
#     <style>
#     .stApp{
#         background-colour: black;
#         colour:white;
#         }    
#         </style>
#         """,
#         unsafe_allow_html=True
# )

# #title
# st.title("Datasweeper Sterling Integrator By Duaa Raza")
# st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization creating the project for quarter 3 ")





import streamlit as st
import random
import pandas as pd

# Set up the Streamlit page
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

# Sample Data (for Progress Tracker)
data = {"Day": [1, 2, 3, 4, 5], "Challenges Completed": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Beliefs for DataSweeper (Limiting Beliefs)
beliefs = ["I'm not good enough", "I will fail", "I can't learn new things", "Success is for others, not me"]

# Define the Feedback Function based on the number of challenges completed
def give_feedback(challenges_completed):
    if challenges_completed <= 2:
        return "Keep pushing forward! You've got this."
    elif challenges_completed <= 4:
        return "Great progress! You're building resilience every day."
    else:
        return "Amazing! You have a strong growth mindset now."

# Home Page Layout
st.title("Welcome to the Growth Mindset Challenge!")
st.subheader("Cultivate a growth mindset and improve yourself daily.")
st.write("Each day, you will get a new challenge to complete, helping you overcome obstacles and improve resilience.")

# Navigation Buttons
home_button = st.button('Home')
challenge_button = st.button('Start Challenge')
progress_button = st.button('Track Progress')
resources_button = st.button('Growth Resources')

# Home Page Content
if home_button:
    st.subheader("What is a Growth Mindset?")
    st.write("""
    A Growth Mindset is the belief that abilities and intelligence can be developed with effort, learning, and perseverance.
    Adopting this mindset helps you embrace challenges and overcome setbacks.
    """)

# Challenge Section (with DataSweeper)
if challenge_button:
    st.subheader("Today's Challenge")
    st.write("What does failure mean to you?")
    failure_response = st.text_area("Write your thoughts:")
    
    if st.button("Submit Response"):
        st.success("Your response has been submitted!")
        # Provide feedback based on response (you can expand this part later)
        feedback = give_feedback(3)  # Placeholder feedback
        st.write(feedback)

    # DataSweeper Feature: Sweep Away Limiting Beliefs
    st.subheader("Time to Sweep Away Limiting Beliefs!")
    belief_to_sweep = random.choice(beliefs)
    st.write(f"Your belief: '{belief_to_sweep}'")

    if st.button("Sweep It Away!"):
        st.success(f"You've just swept away: '{belief_to_sweep}'")
        # Update user progress or store the data (this can be enhanced with a real database)
        st.write("Well done! Keep building your growth mindset.")

# Progress Tracker
if progress_button:
    st.subheader("Your Progress")
    st.write("Here's how you're progressing with your daily challenges:")
    st.line_chart(df.set_index("Day"))

    # Personalized Feedback based on progress (simulate user data)
    challenges_completed = 3  # Replace with actual user data (example value)
    feedback = give_feedback(challenges_completed)
    st.write(feedback)

# Resources Page
if resources_button:
    st.subheader("Growth Resources")
    st.write("""
    Here are some great resources to help you develop a growth mindset:
    - **Books**: 
        - *Mindset: The New Psychology of Success* by Carol Dweck
        - *Grit: The Power of Passion and Perseverance* by Angela Duckworth
    - **Articles**: 
        - [Growth Mindset: A Complete Guide](https://www.mindsethealth.com/)
        - [How to Cultivate a Growth Mindset](https://www.forbes.com/sites/ashleystahl/2020/05/26/how-to-cultivate-a-growth-mindset/)
    - **Videos**: 
        - [Carol Dweck on the Growth Mindset](https://www.youtube.com/watch?v=WUqfH-UFJzA)
    """)

# Footer Section
st.markdown("---")
st.write("Made with ❤️ by [Your Name].")
st.write("Contact: your.email@example.com")
