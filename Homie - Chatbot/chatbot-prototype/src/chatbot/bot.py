from openai import OpenAI

class ChatBot:
    def __init__(self):
        self.user_input = ""
    
    def start_chat(self):
        print("Welcome to the House Finder Homee!")
        print("You can ask me to find houses for rent or sale based on your criteria.")

    def process_input(self, user_input):
        # Here you would typically process the input and call the search functionality
        client = OpenAI(
            api_key="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"
        )

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": f"DO NOT PROVIDE REAL INFO, ROLE PLAY AS REAL ESTATE AGENT: help me find a property based on provided criteria in the london area. Anywhere outside of London is not part of our services: {user_input}. Keep information concise."}
            ]
        )

        response = completion.choices[0].message.content
        return response