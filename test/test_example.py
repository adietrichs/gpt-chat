import package_name

def test_greeting():
    greeting = package_name.greeting()
    assert greeting == "Hello World!", "Invalid greeting:  " + str(greeting)
