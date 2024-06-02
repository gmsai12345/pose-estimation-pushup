# Pushup Counter Application

This application counts pushups and gives form feedback in real-time using your webcam. It utilizes OpenCV for video capture, MediaPipe for pose detection, and Streamlit for the web interface.

## Features

- Real-time pushup counting
- Form feedback to ensure correct posture
- Visual progress bar indicating pushup motion

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pushup-counter.git
    cd pushup-counter
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Ensure your webcam is connected and functioning.
2. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

3. A new tab will open in your default web browser displaying the application.

## Project Structure

- `app.py`: Main application code.
- `PoseModule.py`: Custom module for pose detection using MediaPipe.
- `requirements.txt`: List of required Python packages.

