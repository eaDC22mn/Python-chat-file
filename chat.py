import http.server
import socketserver
import threading
import time

HTML = b"""
<!DOCTYPE html>
<html>
<head>
  <title>Simple Chat</title>
  <style>
    body { font-family: sans-serif; margin: 20px; }
    #chat { border: 1px solid #ccc; height: 300px; overflow-y: auto; padding: 10px; }
  </style>
</head>
<body>

<h2>Global Chat (Refresh to see new messages)</h2>
<h4>find on www.github.com/eaDC22mn</h4>
<form method="POST">
  <input name="name" id="name" placeholder="Name">
  <input name="msg" placeholder="Message">
  <button>Send</button>
</form>

<script>
  // Restore saved name on page load
  if (localStorage.username) {
    document.getElementById("name").value = localStorage.username;
  }

  // Save name whenever the user types it
  document.getElementById("name").addEventListener("input", () => {
    localStorage.username = document.getElementById("name").value;
  });
</script>

<script>
  // Auto-scroll to bottom of chat on page load
  window.onload = function() {
    const chat = document.getElementById("chat");
    chat.scrollTop = chat.scrollHeight;
  };
</script>

<div id="chat">
__MESSAGES__
</div>

</body>
</html>
"""

messages = []

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        page = HTML.replace(b"__MESSAGES__", "<br>".join(messages).encode())
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(page)

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length).decode()
        parts = dict(x.split("=") for x in data.split("&"))
        name = parts.get("name", "Anon")
        msg = parts.get("msg", "")
        messages.append(f"{name}: {msg}")
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()

PORT = 3000
print(f"Chatroom running at http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()