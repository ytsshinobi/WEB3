import random
import string
import os
from flask import Flask, request, render_template_string

app = Flask(__name__)
TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
GROUP_LINK = "https://t.me/+2oxLmAzwvTM4MDgy"
current_password = ""

def generate_password():
    """Tasodifiy 6 xonali parol yaratish"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def update_password():
    global current_password
    current_password = generate_password()
    print(f"Yangi maxfiy parol: {current_password}")

update_password()

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Maxfiy Guruh Havolasi</title>
</head>
<body>
    <h2>Maxfiy guruhga kirish</h2>
    <form method="POST">
        <label for="password">Parolni kiriting:</label>
        <input type="text" id="password" name="password" required>
        <button type="submit">Tasdiqlash</button>
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        user_password = request.form.get('password')
        if user_password == current_password:
            message = f"To‘g‘ri! Guruh havolasi: <a href='{GROUP_LINK}'>Bu yerda</a>"
        else:
            message = "Noto‘g‘ri parol. Qaytadan urinib ko‘ring."
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
