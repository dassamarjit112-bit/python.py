from flask import Flask, render_template, request
import qrcode
app = Flask(__name__)

# This route displays the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    greeting = ""
    qr= qrcode.create(user_input)
    qr.save= ("qr.png")

    # Check if the user submitted the form
    if request.method == 'POST':
        # Get the input data from the HTML form (linked by 'name="username"')
        user_input = request.form.get('username')
        
        if user_input:
            greeting = f"qr.png"
            
    # Send the greeting variable back to the HTML page
    return render_template('index.html', output=greeting)

if __name__ == '__main__':
    app.run(debug=True)