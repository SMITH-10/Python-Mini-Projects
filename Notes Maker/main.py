import google.generativeai as genai
import os

genai.configure(api_key=os.environ["YOUR_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
Subject=input("Enter a subject to make notes for: ")
Topic=input("Enter a Topic to make notes for: ")


response = model.generate_content(f"""Actas a {Subject} teacher and create a detailed notes for the topic :{Topic}. 
Notes should include following things:
Definition:
Provide a concise and formal definition of the concept.
Layman's Explanation: Explain the concept in simpler, more relatable terms that anyone can understand, using analogies or everyday examples if possible.
Key Points:
Highlight the points of the topic,.
Abbreviation for Easy Recall: Create an abbreviation or mnemonic that helps to remember these key points. Relate it to the topic for stronger retention.
Learning Tips:
Include a quick and easy method to grasp the concept (e.g., a diagram, short story, or relatable scenario).
Focus on repetition or any fun method (like rhyming or visual association) that makes learning more engaging.""") 


print(response.text)