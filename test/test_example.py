import gpt_chat

def test_greeting():
    greeting = gpt_chat.greeting()
    assert greeting == "Hello World!", "Invalid greeting:  " + str(greeting)
