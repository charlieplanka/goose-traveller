# goose-traveller

The script allows you to send and receive any data using client-server connection between two hosts. For example, you can send an image of a domestic goose to your friend or a lover:

![Domestic goose](/images/domestic_goose.jpg)

Receiving side runs the script in the **server** mode, sending side uses the **client** mode.

If the script is run in the server mode, there are required parameters:
* port - a port to listen to
* file - a filename for recevied data

If the script is run in the client mode, there are required parameters:
* host - a hostname of a server
* port - a port to connect to (should be the same as the server port)
* file - a filename of data to send

All the required parameters are specified when the script is run via the command line.
Examples:

```
goose-traveller.py server --port=5000 --file=received_data.jpg
goose-traveller.py client --host=localhost --port=5000 --file=domestic_goose.jpg
```

Server side runs the script first.

## :baby_chick: Planned improvements 
1. Super-duper GUI.
2. Authentication.
3. Traffic encryption. If some fraudster intercepts the sent file, he won't be able to understand that it's a goose.
