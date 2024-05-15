import zmq
import json
import re

def count_characters(string):
    character_frequency = {}
    for char in string:
        character_frequency[char] = character_frequency.get(char, 0) + 1
    return character_frequency

def count_words(string):
    word_frequency = {}
    words = string.split()
    for word in words:
        word_frequency[word] = count_characters(word)
    return word_frequency

def validate_string(string):
    # Regular expression to match non-English characters
    non_english_characters = re.findall(r'[^\x00-\x7F]', string)
    return len(non_english_characters) == 0, non_english_characters

def process_string(string):
    is_valid, invalid_characters = validate_string(string)
    if not is_valid:
        return {'error': 'Non-English characters found', 'invalid_characters': invalid_characters}, None
    
    character_frequency = count_characters(string)
    word_frequency = count_words(string)
    
    return character_frequency, word_frequency

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        # Wait for next request from client
        message = socket.recv_json()
        print("Received message from client:", message)

        # Process the received message
        character_frequency, word_frequency = process_string(message['string'])
        print("Processing message...")

        # Print character and word frequencies
        print("Character frequency:", character_frequency)
        print("Word frequency:", word_frequency)

        # Send the response back to client
        socket.send_json({'character_frequency': character_frequency, 'word_frequency': word_frequency})
        print("Response sent to client.")

if __name__ == "__main__":
    main()
