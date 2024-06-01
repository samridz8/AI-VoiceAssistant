import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyD6eEgFQ7PPVWLdaLOndSawg7JUaBQCf0M")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
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
        "",
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

response = chat_session.send_message("who is cristiano ronaldo")

print(response.text)
print(chat_session.history)