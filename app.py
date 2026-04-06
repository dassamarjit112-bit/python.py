import qrcode
import io
from flask import Flask, render_template, request, send_file
app = Flask(__name__)
# This route displays the home page
@app.route('/', methods=['GET', 'POST'])
def home():

    # Check if the user submitted the form
    if request.method == 'POST':
        # Get the input data from the HTML form (linked by 'name="username"')
        user_input = request.form.get('username')
        if user_input:
            img = qrcode.make(user_input)
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            return send_file(buffer,mimetype='image/png')
            8
    # Send the greeting variable back to the HTML page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)