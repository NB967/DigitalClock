import streamlit as st
import datetime
import time

# --- Streamlit App Configuration ---
st.set_page_config(
    page_title="Digital Clock",
    page_icon="⏰",
    layout="centered"
)

st.title("Live Digital Clock")
st.write("This simple application displays the current time, updating every second.")

# Create an empty placeholder for the clock display
# This allows us to update the content in place without re-rendering the whole app
clock_placeholder = st.empty()

# --- Clock Logic ---
# Streamlit applications re-execute from top to bottom.
# To create a continuously updating clock, we'll use a loop combined with st.rerun().
# st.rerun() tells Streamlit to re-run the entire script immediately.
while True:
    # Get the current time
    # datetime.datetime.now() gets the current date and time
    # strftime("%H:%M:%S") formats it as HH:MM:SS (e.g., 14:35:01)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Update the content of the placeholder with the current time
    # The Markdown string is styled using HTML and CSS for a larger, more prominent display.
    # We use unsafe_allow_html=True to render the HTML.
    clock_placeholder.markdown(
        f"<h1 style='text-align: center; font-size: 80px; font-weight: bold; color: #4CAF50;'>{current_time}</h1>",
        unsafe_allow_html=True
    )

    # Pause for 1 second before updating again
    time.sleep(1)

    # Force Streamlit to rerun the script immediately.
    # This is crucial for the clock to update every second without user interaction.
    st.rerun()

# Note: This continuous loop with st.rerun() is suitable for simple, constantly updating displays.
# For more complex Streamlit apps that need real-time updates and also handle user interactions
# efficiently, consider more advanced patterns involving session state and callbacks, or
# Streamlit's own components for long-running tasks if applicable.
