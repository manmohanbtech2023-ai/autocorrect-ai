from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(_name_)

html = """
<h2>Text Auto Correct System</h2>
<form method="post">
<textarea name="text" rows="5" cols="40"></textarea><br><br>
<button type="submit">Correct</button>
</form>

{% if result %}
<h3>Corrected Text:</h3>
<p>{{ result }}</p>
{% endif %}
"""

@app.route("/", methods=["GET","POST"])
def home():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        result = str(TextBlob(text).correct())
    return render_template_string(html, result=result)

app.run(host="0.0.0.0", port=10000)