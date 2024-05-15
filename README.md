# String-to-Dictionary-ZeroMQ-

## Using the Microservice

### Requesting Data

To programmatically request data from the microservice, follow these steps:

1. **Instantiate a ZeroMQ REQ socket**: In your client application, create a ZeroMQ REQ socket to connect to the microservice.

2. **Connect to the Microservice**: Connect the REQ socket to the microservice using the appropriate transport protocol and address (e.g., TCP or IPC).

3. **Send Request**: Send a JSON-formatted request to the microservice, specifying the string data you want to process.

4. **Receive Response**: Wait for and receive the response from the microservice, which will contain the character and word frequencies of the input string.

#### Example Call

Here's an example of how to request data from the microservice using Python:

```python
import zmq

def request_data(string):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send_json({'string': string})
    response = socket.recv_json()
    return response

# Example call
response = request_data("Hello, world!")
print("Character Frequency:", response['character_frequency'])
print("Word Frequency:", response['word_frequency'])
