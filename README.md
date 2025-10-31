# Streamlit Application

This project is a Streamlit application that displays a looping video with an overlay button. Below are the details of the project structure and how to set it up.

## Project Structure

```
streamlit_app
├── bday_home.py
├── assets
│   ├── ts_eye.png
│   └── background_video.mp4
├── pages
│   └── other_pages.py
├── requirements.txt
└── README.md
```

## File Descriptions

- **bday_home.py**: The main file for the Streamlit application. It sets up the page configuration, adds a title and text, checks for the existence of a video file, and displays the video in a loop. A button is overlaid on the video for user interaction.

- **assets/ts_eye.png**: An image file that was previously used in the application. It may no longer be necessary if the video is being used.

- **assets/background_video.mp4**: The video file that will be displayed in the application. It is set to loop continuously.

- **pages/other_pages.py**: A placeholder for additional pages in the Streamlit application. This file can be expanded to include more features or components related to the app.

- **requirements.txt**: This file lists the dependencies required for the project, including Streamlit and any other necessary libraries.

## Setup Instructions

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Navigate to the Project Directory**: Open a terminal and navigate to the `streamlit_app` directory.

3. **Install Dependencies**: Run the following command to install the required libraries:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**: Start the Streamlit application by executing:
   ```
   streamlit run bday_home.py
   ```

5. **Access the Application**: Open your web browser and go to the URL provided in the terminal (usually `http://localhost:8501`).

## Usage

Once the application is running, you will see a looping video with a button overlay. You can interact with the button as needed. 

## Notes

- Ensure that the video file `background_video.mp4` is present in the `assets` directory for the application to function correctly.
- The image file `ts_eye.png` is included but may not be necessary for the current implementation.