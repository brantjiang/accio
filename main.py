import google.generativeai as genai

def main():
    key = open("./api_keys/gemini.apikey", "r").readline()
    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Hello, introduce yourself in 1 sentence.")
    print(response.text)

if __name__ == '__main__':
    main()