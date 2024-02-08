import streamlit as st
from st_keyup import st_keyup
from datetime import datetime
import asyncio
from streamlit_sortables import sort_items
import pandas as pd


# Function to move to the next step
def next_step():
    st.session_state.step += 1

# Function to display data entry form
def data_entry(step, text):
#    st.header(f"Step {step}: Data Entry")
    image = "images/dates.png"
    st.image(image, caption="Date data")
    st.sidebar.header("Enter the dates from the image one per line.")
    if step == 7:
        st.sidebar.header("Dates should have the format")
        st.sidebar.markdown("**:red[YYYY-MM-DD]**")
    data_input1 = st_keyup(text, key=str(step) + "1")
    data_input2 = st_keyup(text, key=str(step) + "2")
    data_input3 = st_keyup(text, key=str(step) + "3")
    data_input4 = st_keyup(text, key=str(step) + "4")
    data_input = [data_input1, data_input2, data_input3, data_input4]
    return data_input

# Function to record entered data
def record_step_data(data, step):
    if step == 2:
        st.session_state.data1 = data
    if step == 7:
        st.session_state.data2 = data
    next_step()

# Function to sort data based on dates
def sort_data(data):
    try:
        # Assuming data is entered in the forced list format
        sorted_data = sorted(data, key=lambda x: x)
        return sorted_data
    except Exception as e:
        st.error("Error sorting data. Please check the format.")
        return e

# Function to capture timer start time
def capture_time(step):
    if step == 3:
        st.session_state.step4_clockstart = datetime.now()
    if step == 8:
        st.session_state.step9_clockstart = datetime.now()
    next_step()

# Start timer
def timer(clockstart):
    test = st.sidebar.empty()   
    asyncio.run(watch(test, clockstart))

# Format timer
async def watch(test, clockstart):
    while True:
        st.markdown("""
<style>
.time {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)
        test.markdown(
            f"""
            <p class="time">
                {str((datetime.now() - clockstart))[:7]}
            </p>
            """, unsafe_allow_html=True)
        r = await asyncio.sleep(1)

# Function to record stress level and move to the next step
def record_stress_level(level, step):
    if step == 5:
        st.session_state.stress_no_formatting += level
    else:
        st.session_state.stress_w_formatting += level
    next_step()

# Main app function
def main():
    
    # Initialize session state variables
    if 'step' not in st.session_state:
        st.session_state['step'] = 1
    if 'data1' not in st.session_state:
        st.session_state['data1'] = ""
    if 'data2' not in st.session_state:
        st.session_state['data2'] = ""
    if 'step4_clockstart' not in st.session_state:
        st.session_state['step4_clockstart'] = 0
    if 'step9_clockstart' not in st.session_state:
        st.session_state['step9_clockstart'] = 0
    if 'stress_no_formatting' not in st.session_state:
        st.session_state['stress_no_formatting'] = 0
    if 'stress_w_formatting' not in st.session_state:
        st.session_state['stress_w_formatting'] = 0

    # Step 1 - Directions
    if st.session_state.step == 1:
        st.title("Date Data Dash")
        st.image("images/cover.webp")
        st.header("Instructions:")
        st.markdown("""
                    - Carefully read and follow the instructions for each step of the following data entry game.
                    - On the next screen, you will copy date data into the fields provided.
                    - Take a deep breath.
                    """)
        
        if st.button("Begin", on_click=next_step):
            pass

    # Step 2 - First data entry
    if st.session_state.step == 2:
        step2 = data_entry(st.session_state.step, "")

        if st.button("Submit", on_click=record_step_data, args=(step2, st.session_state.step)):
            pass

    # Step 3 - Directions
    if st.session_state.step == 3:
        st.header("Instructions:")
        st.markdown("""
                    - On the next screen, you will sort the dates you entered *chronologically*.
                    - The computer will attempt to help you by pre-sorting the dates alphabetically.
                    - This exercise is will be timed.
                    """)
        
        if st.button("Proceed", on_click=capture_time, args=(st.session_state.step,)):
            pass

    # Step 4 - First data sorting
    if st.session_state.step == 4:
        st.sidebar.header("Sort the dates chronologically.")
        sorted_data1 = sort_data(st.session_state.data1)
        sort_items(sorted_data1, direction='vertical', key='sorter1')
        if st.button("Submit", on_click=next_step):
            pass
        timer(st.session_state.step4_clockstart)

    # Step 5 - First stress rating
    if st.session_state.step == 5:
        st.sidebar.header("Rate your stress level from 1 to 10 (1 = least stressed):")
        stress_level1 = st.slider("", 1, 10, 1)
        if st.button("Submit", on_click=record_stress_level, args=(stress_level1, st.session_state.step)):
            pass
    
    # Step 6 - Directions
    if st.session_state.step == 6:
        st.header("Instructions:")
        st.markdown("""
                    - You will now repeat this game using improved *data governance* practices!
                    - On the next screen, you will once again copy date data into the fields provided.
                    - Take a deep breath.
                    """)
        
        if st.button("Begin", on_click=next_step):
            pass

    # Step 7 - Second data entry
    if st.session_state.step == 7:
        step7 = data_entry(st.session_state.step, "Use the format YYYY-MM-DD.")

        if st.button("Submit", on_click=record_step_data, args=(step7, st.session_state.step)):
            pass

    # Step 8 - Directions
    if st.session_state.step == 8:
        st.header("Instructions:")
        st.markdown("""
                    - On the next screen, you will once again sort the dates you entered *chronologically*.
                    - The computer will attempt to help you by pre-sorting the dates alphabetically.
                    - This exercise is will be timed.
                    """)
        
        if st.button("Proceed", on_click=capture_time, args=(st.session_state.step,)):
            pass

    # Step 9 - Second data sorting
    if st.session_state.step == 9:
        st.sidebar.header("Sort the dates chronologically.")
        sorted_data2 = sort_data(st.session_state.data2)
        sort_items(sorted_data2, direction='vertical', key='sorter1')
        if st.button("Submit", on_click=next_step):
            pass
        timer(st.session_state.step9_clockstart)

    # Step 10 - Second stress rating
    if st.session_state.step == 10:
        st.sidebar.header("Rate your stress level from 1 to 10 (1 = least stressed):")
        stress_level2 = st.slider("", 1, 10, 1)
        if st.button("Submit", on_click=record_stress_level, args=(stress_level2, st.session_state.step)):
            pass
    
    # Step 11 - Final results
    if st.session_state.step == 11:
        df = pd.DataFrame.from_records([[st.session_state.stress_no_formatting, st.session_state.stress_w_formatting]],
                                       columns=['Baseline stress', 'Stress with data governance'],
                                       )
        st.dataframe(df, hide_index=True)

        if st.session_state.stress_w_formatting < st.session_state.stress_no_formatting:
            st.markdown("Congratulations!  You've successfully demonstrated that good **data governance practices can reduce stress** and be implemented simply.")
        else:
            st.markdown("Unfortunately, data governance principles did not reduce your stress this time, but we hope you see how they made the sorting analysis easier.")
        
        st.header("Thank you for playing!")
if __name__ == "__main__":
    main()
