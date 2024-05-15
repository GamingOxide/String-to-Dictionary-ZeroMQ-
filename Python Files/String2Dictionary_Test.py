import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    string = input("Enter a string: ")
    print("Sending string to microservice...")

    # Send the string to the microservice
    socket.send_json({'string': string})

    # Receive and print the response
    print("Waiting for response from microservice...")
    response = socket.recv_json()
    print("Received response from microservice.")
    print("Character Frequency:", response['character_frequency'])
    print("Word Frequency:", response['word_frequency'])

if __name__ == "__main__":
    main()
