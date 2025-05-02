# Spotify for Learning

**Spotify for Learning** is an innovative web application that allows users to generate personalized 5-minute educational audio snippets on various topics. The app utilizes the **Google Gemini 1.5** model to generate engaging learning content, which is then converted into speech using **pyttsx3**. This tool is ideal for anyone who wants to quickly learn about specific topics during their daily routine.

---

## Features
- **Personalized Learning**: Generate 5-minute learning snippets based on topics and time limits.
- **User-friendly**: Simple and easy-to-use interface for quick access to educational content.
- **Audio Playback**: Converts generated text to speech and allows users to listen to their personalized snippets.

---

## How It Works

1. **User Input**: The user enters a list of topics (comma-separated) and a desired time limit (in minutes).
2. **Content Generation**: The app sends the input to the **Gemini 1.5 model** to generate a relevant educational text.
3. **Text-to-Speech**: The generated text is converted to speech using **pyttsx3**, and an audio file is saved.
4. **Audio Playback**: The audio file is made available for the user to listen to directly within the app.

---

## Tech Stack

- **Backend**: Flask (Python)
- **AI Model**: Google Gemini 1.5
- **Text-to-Speech**: pyttsx3
- **Frontend**: HTML, CSS (for UI)
- **Hosting**: Local (can be deployed on platforms like Heroku or AWS)

---

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/spotify-for-learning.git
    cd spotify-for-learning
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment variables:
    - Add your **Google Gemini API Key** to your environment variables or directly in the code.
    - Specify the directory where audio files will be saved.

4. Run the application:
    ```bash
    python app.py
    ```

---

## Demo

Check out the **[Demo Video](#https://youtu.be/_Qt2xTaP4Ns)** to see the app in action!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
