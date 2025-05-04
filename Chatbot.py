#My ChatBot
#
#
#
#
pip install openai
import openai
import Key

def generate_response(user_input):
    try:
        #Call the OpenAI API
        completion = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Assume the role a Python teacher, and thick step by step. Your name is Skippy Py."},
                     {"role": "user", "content": user_input}]
        )

    except Expttion as e :
        print("Error generating response:", e)
        return "Sorry, I don't understand your input. Please try again."

def main():
    openai.api_key = key

    while True:
        user_input = input("Enter your message: ")

        if user_input == "exit":
            print("Goodbye")
            break

        response = generate_response(user_input)

        print("Python Study Bot", response)

if __name__ == "__main__":
    main()