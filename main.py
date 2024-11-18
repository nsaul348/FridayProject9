import tkinter as tk
import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path=r'C:\Users\sauln\OneDrive\Documents\CSC Practice\fp9.env')
client = openai.OpenAI(
api_key = os.getenv('OPENAI_API_KEY'),
)

# Set the OpenAI API key


def get_completion():
    prompt = text_input.get("1.0", tk.END).strip()  # Get user input from the text box
    if prompt:
        try:
            # Call the OpenAI API for text completion
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # or another model you prefer
                messages=[{"role": "user", "content": prompt}],
            )
            # Display the result in the output box
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, response.choices[0].message.content)
        except Exception as e:
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, f"Error: {str(e)}")
    else:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")

# Set up the GUI window
root = tk.Tk()
root.title("OpenAI Prompt Completion")

# Create the input text box (where the user types the prompt)
text_input = tk.Text(root, height=10, width=50)
text_input.pack(padx=10, pady=10)

# Create the submit button to trigger API call
submit_button = tk.Button(root, text="Submit", command=get_completion)
submit_button.pack(pady=10)

# Create the output text box (where the response will be displayed)
output_box = tk.Text(root, height=10, width=50)
output_box.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()