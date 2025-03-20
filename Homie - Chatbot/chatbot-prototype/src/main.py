# main.py

import tkinter as tk
from tkinter import scrolledtext
from chatbot.bot import ChatBot
import time
global previouschathistory
previouschathistory =""
class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Homie")
        self.root.geometry("375x667")  # Size of a mobile phone

        # Set font and color for chat display
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Helvetica", 12), bg="#f0f0f0", fg="#333333")
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(fill=tk.X, padx=10, pady=10)

        # Set font and color for entry text
        self.entry_text = tk.Entry(self.entry_frame, font=("Helvetica", 12), bg="#ffffff", fg="#333333")
        self.entry_text.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.entry_text.bind("<Return>", self.send_message)

        # Set font and color for send button
        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.send_message, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")
        self.send_button.pack(side=tk.RIGHT)

        self.chatbot = ChatBot()
        self.chatbot.start_chat()  # Initialize the chatbot
        self.display_message("HOMEE", "Welcome to the House Finder Homee!")

    def send_message(self, event=None):
        global previouschathistory
        user_message = self.entry_text.get()
        if user_message.strip():
            self.display_message("You", user_message)
            self.entry_text.delete(0, tk.END)
            user_message = "previous conversation history: ", previouschathistory, user_message
            bot_response = self.chatbot.process_input(user_message)  # Process the user input
            self.display_message("HOMEE", bot_response)
            previouschathistory = previouschathistory, user_message, bot_response

    def display_message(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)

def main():
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()