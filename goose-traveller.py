import socket
import argparse


def run_server(port: int, detination_filename: str):

    serversocket = socket.socket()
    serversocket.bind(("", port))
    serversocket.listen(1)

    print("Waiting for connection..")
    clientsocket, address = serversocket.accept()
    print("Connected!")

    print("Receiving data..")
    with open(detination_filename, "wb") as f:
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            f.write(data)
    print(
        f"Data is received and saved under the {detination_filename}. Seems it is.. a goose!")

    clientsocket.close()
    print("Connection is closed.")
    print("All done! Honk-honk.")


def run_client(hostname: str, port: int, source_filename: str):

    clientsocket = socket.socket()

    print("Trying to connect..")
    clientsocket.connect((hostname, port))
    print("Connected!")

    print("Sending the data..")
    with open(source_filename, "rb") as f:
        data = f.read()
        clientsocket.send(data)
    print("The data has been sent.")

    clientsocket.close()
    print("Connection is closed.")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sending and receving pictures of various animals.")
    subparsers = parser.add_subparsers(
        dest="mode", required=True, help="modes")

    parser_server = subparsers.add_parser("server", help="run in server mode")
    parser_server.add_argument("--port", "-p", type=int, metavar="PORT", required=True,
                               help="port to listen to")

    parser_server.add_argument("--file", "-f", type=str, metavar="FILE", required=True,
                               help="file to save the received data")

    parser_client = subparsers.add_parser("client", help="run in client mode")
    parser_client.add_argument("--host", "-H", type=str, metavar="HOST", required=True,
                               help="remote hostname for connection")

    parser_client.add_argument("--port", "-p", type=int, metavar="PORT", required=True,
                               help="remote port for connection")

    parser_client.add_argument("--file", "-f", type=str, metavar="FILE", required=True,
                               help="file to send")

    return parser.parse_args()


def main():
    args = parse_args()
    if args.mode == "server":
      run_server(args.port, args.file)
    elif args.mode == "client":
      run_client(args.host, args.port, args.file)


main()
