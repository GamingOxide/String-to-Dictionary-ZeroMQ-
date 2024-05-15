# String-to-Dictionary-ZeroMQ-

## Using the Microservice

### Requesting Data

To programmatically request data from the microservice, follow these steps:

1. **Instantiate a ZeroMQ REQ socket**: In your client application, create a ZeroMQ REQ socket to connect to the microservice.
   
2. **Connect to the Microservice**: Connect the REQ socket to the microservice using the TCP transport protocol and the address `tcp://localhost:5555`.

3. **Send Request**: Send a JSON-formatted request to the microservice. The request should contain the input string that you want to process.

4. **Receive Response**: Wait for and receive the response from the microservice. The response will contain the character and word frequencies of the input string.

    - The response will be a JSON object containing two fields: `character_frequency` and `word_frequency`.
    - `character_frequency` will contain a dictionary mapping each character in the input string to its frequency.
    - `word_frequency` will contain a dictionary mapping each word in the input string to a dictionary of its character frequencies.
    - Example response:
    ```json
    {
        "character_frequency": {"H": 1, "e": 1, "l": 3, "o": 2, ",": 1, " ": 1, "w": 1, "r": 1, "d": 1, "!": 1},
        "word_frequency": {"Hello,": {"H": 1, "e": 1, "l": 2, "o": 1, ",": 1}, "world!": {"w": 1, "o": 1, "r": 1, "l": 1, "d": 1, "!": 1}}
    }
    ```

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

![Sequence diagram](https://github.com/GamingOxide/String-to-Dictionary-ZeroMQ-/assets/79893952/88e34a7f-4ba6-4689-9d87-7888de0e4094)
