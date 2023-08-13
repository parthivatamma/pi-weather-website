from wsgiref.simple_server import make_server

def file_parser(word, filename):
    print("in here")
    with open(filename, "r") as fp:
        lines = fp.readlines()
        print(lines)
        for row in lines:
            if row.find(word) != -1:
                return (lines[lines.index(row)])


def app(environ, start_response):
    status = "200 OK"
    response_headers = [("Content-type", "text/plain"),
                        ('Access-Control-Allow-Origin', '*')]
    path = environ["PATH_INFO"]
    if path == "/humidity":
        start_response("200 OK", response_headers)
        print([file_parser("humidity", "pi_data.txt")])
        return [file_parser("humidity", "tests.json").encode()]

    if path == "/pressure":
        start_response("200 OK", response_headers)
        return [file_parser("pressure", "tests.json").encode()]

    if path == "/temp":
        start_response("200 OK", response_headers)
        return [file_parser("temp", "tests.json").encode()]

if __name__ == "__main__":
    server = make_server("", 8000, app)
    server.serve_forever()
