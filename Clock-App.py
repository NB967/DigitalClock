import streamlit as st
import datetime
import time
import subprocess # Import subprocess to run shell commands

# --- Streamlit App Configuration ---
st.set_page_config(
    page_title="Digital Clock with Git Info",
    page_icon="⏰",
    layout="centered"
)

st.title("Live Digital Clock")
st.write("This simple application displays the current time, updating every second.")

# --- Git Information Section ---
st.header("Application Version (Git Info)")

def get_git_last_commit_info():
    """
    Runs a git command to get the last commit hash and message.
    Returns a formatted string or an error message.
    """
    try:
        # Command to get the last commit hash and subject (message)
        # %h: Abbreviated commit hash
        # %s: Commit subject
        command = ["git", "log", "-1", "--pretty=format:%h - %s"]
        
        # Run the command
        # capture_output=True: captures stdout and stderr
        # text=True: decodes output as text
        # check=True: raises CalledProcessError if the command returns a non-zero exit code
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except FileNotFoundError:
        return "Error: Git is not installed or not found in system PATH."
    except subprocess.CalledProcessError as e:
        # This occurs if it's not a Git repository or other git errors
        return f"Error: Not a Git repository or Git command failed. ({e.stderr.strip()})"
    except Exception as e:
        return f"An unexpected error occurred while getting Git info: {e}"

# Get Git info once when the app starts
git_info = get_git_last_commit_info()
st.info(f"Last Commit: {git_info}")

# --- Clock Display ---
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
