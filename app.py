import qrcode
import io
from flask import Flask, render_template, request, send_file
app = Flask(__name__)
# This route displays the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    qr_img_url = None
    # Check if the user submitted the form
    if request.method == 'POST':
        # Get the input data from the HTML form (linked by 'name="username"')
        user_input = request.form.get("username")
        if user_input:
            #genarate qrcode 
            qr = qrcode.Qrcode(version=1, box_size=10, border=5)
            qr.add_data(user_input)
            qr.make(fit=True)
            #save img in memory
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            return send_file(buffer,mimetype='image/png')
    # Send the greeting variable back to the HTML page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)