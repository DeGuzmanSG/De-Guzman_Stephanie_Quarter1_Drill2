from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value
    hobby = document.querySelector("#hobby").value
    

    # Clear the output div first
    document.querySelector("#output").innerText = ""

    # Multiline message using input values
    message = f"""📖 Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}
    Hobby : {hobby}

    Notes:\n{name} is currently {age} years old and studies at {school}.\nThis student also likes {hobby}!\nPlease don't be unfriendly or a hater towards her!
    """

    display(message, target="output")

