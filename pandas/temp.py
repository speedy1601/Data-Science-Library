import keyboard

# This variable will store the currently typed sentence
current_sentence = ""

def on_key_event(event:keyboard.KeyboardEvent):
    global current_sentence

    # When any key is pressed (including characters, special keys, etc.)
    if event.event_type == "down":
        # If a period (.) is detected
        if event.name == ".":
            # Convert the previous sentence to uppercase
            uppercase_sentence = current_sentence.upper()
            # Replace the current sentence with its uppercase version
            keyboard.write(f"\b" * len(current_sentence))  # Deletes the current sentence
            keyboard.write(uppercase_sentence)  # Writes the uppercase version
            keyboard.write(".")  # Adds the period back
            current_sentence = ""  # Reset for the next sentence
        else:
            # Add the pressed key to the current sentence if it's a character
            if len(event.name) == 1:
                current_sentence += event.name

a = print("Write Something : ", end=' ')
# Hook the keyboard listener
keyboard.hook(on_key_event)

# Keep the script running
keyboard.wait()