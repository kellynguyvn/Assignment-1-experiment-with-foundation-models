# Gemini Long Context Use Cases
# This code is designed to be run in a Google Colab notebook

!pip install google-generativeai

import google.generativeai as genai
import os
from IPython.display import display, Markdown

# Configure the API key (you'll need to set this in Colab)
genai.configure(api_key='YOUR_API_KEY_HERE')

# Set up the model
model = genai.GenerativeModel('gemini-pro')

def generate_usecases():
    prompt = """
    Generate 10 novel and innovative use cases for long context in Gemini AI. 
    These should be unique applications that showcase the power of extended context.
    For each use case, provide:
    1. A title
    2. A brief description (2-3 sentences)
    3. A potential demo scenario
    
    Format the output as a numbered list.
    """
    
    response = model.generate_content(prompt)
    return response.text

def demo_usecase(usecase):
    prompt = f"""
    Create a detailed demo for the following use case of Gemini's long context capability:
    
    {usecase}
    
    Provide a step-by-step walkthrough of how this demo would work, including:
    1. Input data or context
    2. Gemini's processing steps
    3. Expected output or results
    
    Make this demo as realistic and practical as possible.
    """
    
    response = model.generate_content(prompt)
    return response.text

def write_article_section(usecase, demo):
    prompt = f"""
    Write a section for a Medium article about the following use case of Gemini's long context capability:
    
    Use Case:
    {usecase}
    
    Demo:
    {demo}
    
    The section should include:
    1. An engaging introduction to the use case
    2. Explanation of how Gemini's long context enables this application
    3. Description of the demo and its results
    4. Potential real-world impact of this application
    
    Write in a clear, engaging style suitable for a technical audience on Medium.
    """
    
    response = model.generate_content(prompt)
    return response.text

# Generate use cases
usecases = generate_usecases()
display(Markdown("# Generated Use Cases"))
display(Markdown(usecases))

# Demo each use case and write article sections
usecases_list = usecases.split('\n\n')
for i, usecase in enumerate(usecases_list, 1):
    display(Markdown(f"## Use Case {i}"))
    display(Markdown(usecase))
    
    demo = demo_usecase(usecase)
    display(Markdown("### Demo"))
    display(Markdown(demo))
    
    article_section = write_article_section(usecase, demo)
    display(Markdown("### Article Section"))
    display(Markdown(article_section))

# Compile full article
full_article = "# 10 Novel Use Cases of Gemini's Long Context Capability\n\n"
for i, usecase in enumerate(usecases_list, 1):
    demo = demo_usecase(usecase)
    article_section = write_article_section(usecase, demo)
    full_article += f"## {i}. {usecase.split('.', 1)[1].strip()}\n\n"
    full_article += article_section + "\n\n"

display(Markdown("# Full Medium Article"))
display(Markdown(full_article))

# Save the full article to a file
with open('gemini_long_context_article.md', 'w') as f:
    f.write(full_article)

print("Article saved to 'gemini_long_context_article.md'")