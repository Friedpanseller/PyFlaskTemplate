import argparse
from waitress import serve

app_name = "Sample Application"

print(f"* Starting {app_name}... Please wait for the link to appear")

# Instantiate the parser
parser = argparse.ArgumentParser(description=app_name)

parser.add_argument('-d', action='store_true',
                    help='Enable debug mode for development servers')

parser.add_argument('-port', type=int,
                    help='Specify a port to run the application on')

parser.add_argument('-host', type=str,
                    help='Specify the hostname/ip to run the application on')

args = parser.parse_args()

if __name__ == "__main__":
    from app import app
    host = args.host if args.host else "127.0.0.1"
    port = args.port if args.port else 5001
    print(f"* Running on http://{host}:{port}/ (Press CTRL+C to quit)")

    if args.d:
        app.run(host=host, port=port, debug=True)
    else:
        serve(app, host=host, port=port)
