import streamlit as st
import pandas as pd

# Initialize the session state to keep track of the data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Link', 'Owner', 'Description', 'Name'])

# Function to add a new row to the data
def add_row():
    new_data = {
        'Link': st.session_state.link,
        'Owner': st.session_state.owner,
        'Description': st.session_state.description,
        'Name': st.session_state.name
    }
    st.session_state.data = st.session_state.data.append(new_data, ignore_index=True)

# Sidebar to add new entries
st.sidebar.header('Add New Entry')
st.sidebar.text_input('Link', key='link')
st.sidebar.text_input('Owner', key='owner')
st.sidebar.text_input('Description', key='description')
st.sidebar.text_input('Name', key='name')
st.sidebar.button('Add Row', on_click=add_row)

# Main dashboard
st.title('Real-Time Updating Dashboard')
st.text_input('Search Filter', '')

# Display the data table
st.table(st.session_state.data)

# Save the data to a CSV file
if st.button('Save Data'):
    st.session_state.data.to_csv('dashboard_data.csv', index=False)
    st.success('Data saved successfully')
