import speech_recognition as sr
import os
import webbrowser
import datetime

import random
import google.generativeai as genai
import numpy as np
from google.generativeai import GenerationConfig

chatStr = ""
def chat(query):
    global chatStr
    chatStr += f"User: {query}\n"

    # Send the query to the AI model and get a response
    genai.configure(api_key="AIzaSyD6eEgFQ7PPVWLdaLOndSawg7JUaBQCf0M")

    # Assuming model and safety_settings are set globally or otherwise accessible
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        safety_settings=[
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ],
        generation_config=GenerationConfig(
            temperature=1,
            top_p=0.95,
            top_k=64,
            max_output_tokens=8192,
            response_mime_type="text/plain",
        )
    )

    # Start a chat session
    chat_session = model.start_chat(
        history=[
            {"role": "user", "parts": ["Start the chat session"]},
        ]
    )

    response = chat_session.send_message(query)
    chatStr += f"Jarvis: {response.text}\n"
    print(response.text)

    if not os.path.exists("pythonProject"):
        os.mkdir("pythonProject")
    with open(f"pythonProject/chat_history.txt", "a") as f:
        f.write(chatStr)

    say(response.text)


def ai(prompt):
    genai.configure(api_key="AIzaSyD6eEgFQ7PPVWLdaLOndSawg7JUaBQCf0M")
    text = f"JarvisAI response for prompt: {prompt} \n****************\n\n"
    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = GenerationConfig(
        temperature=1,
        top_p=0.95,
        top_k=64,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        safety_settings=safety_settings,
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "write a job application for software engineer\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "##  [Your Name]\n##  [Your Phone Number] | [Your Email Address] | [Your LinkedIn Profile (Optional)]\n\n**[Date]**\n\n**[Hiring Manager Name (If known)]**\n**[Company Name]**\n**[Company Address]**\n\n**Dear [Hiring Manager Name or \"Hiring Team\"],**\n\nI am writing to express my keen interest in the Software Engineer position at [Company Name], as advertised on [Platform where you found the job posting]. I have been following [Company Name]'s work for some time and am particularly impressed with [mention something specific you admire about the company, e.g., their innovative product, commitment to open source, etc.].  \n\nWith [Number] years of experience in software development, I have a strong foundation in [list relevant programming languages, frameworks, and technologies] and a proven track record of successfully [mention a few key accomplishments, e.g., designing and implementing complex systems, collaborating with cross-functional teams, delivering high-quality software on time and within budget]. \n\nIn my previous role at [Previous Company Name], I was responsible for [briefly describe your responsibilities]. I am adept at [mention specific skills relevant to the job description, e.g., problem-solving, debugging, writing clean and efficient code, working in agile environments]. My experience in [mention any relevant industry or domain knowledge] makes me confident in my ability to contribute significantly to [Company Name]'s success.\n\nI am eager to learn more about the Software Engineer position and the opportunity to join your talented team.  I am confident that my skills and experience align perfectly with the requirements of this role, and I am excited to contribute my expertise to [Company Name]'s continued growth. \n\nThank you for your time and consideration. I have attached my resume for your review and welcome the opportunity to discuss my qualifications further.\n\n**Sincerely,**\n\n**[Your Name]** \n\n**[Optional: Include a link to your portfolio or GitHub profile]** \n\n**Please note:**\n\n* **Customize this template:** Replace the bracketed information with your own details.\n* **Tailor your application:** Carefully read the job description and highlight the skills and experience most relevant to the position.\n* **Proofread:** Ensure your application is free of errors before submitting it.\n* **Be confident and enthusiastic:** Show your passion for the company and the opportunity. \n",
                ],
            },
        ]
    )

    response = chat_session.send_message(prompt)

    print(response.text)
    text += response.text
    print(chat_session.history)

    if not os.path.exists("pythonProject"):
        os.mkdir("pythonProject")
    with open(f"pythonProject/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

        
def say(text):
    os.system(f"say {text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-uk')
        return query



if __name__ == "__main__":
    print("Pycharm")
    say("Hello, I am Jarvis")
    print("listening...")
    while True:
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} ")
                webbrowser.open(site[1])

        if "time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f" time is {hour}  {min} ")

        if "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        if "open spotify".lower() in query.lower():
            os.system(f"open /Applications/Spotify.app")

        if "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)







