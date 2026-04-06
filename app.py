import qrcode
from flask import Flask, render_template, request
app = Flask(__name__)
# This route displays the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    greeting = ""

    # Check if the user submitted the form
    if request.method == 'POST':
        # Get the input data from the HTML form (linked by 'name="username"')
        user_input = request.form.get('username')
        qr= qrcode.make(user_input)
        qr.save("qr.png")
        if user_input:
            greeting = "qr.png"
            
    # Send the greeting variable back to the HTML page
    return render_template('index.html', output=greeting)

if __name__ == '__main__':
    app.run(debug=True)