import speech_recognition as sr
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"


def chat_response(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{text}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    return response


def listen_and_respond():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ko-KR")
        # response = chat_response(text)
        print(f"You: {text}")
        # print(f"ChatGPT: {response}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


if __name__ == "__main__":
    listen_and_respond()
