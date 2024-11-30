from flask import Flask, render_template
import json
import bisect
from datetime import datetime

app = Flask(__name__,
    template_folder="public",
    static_folder="public/static"
)

with open("data.json", "r") as f:
    data = json.load(f)
    
cumulative_lengths = [entry["cumulativeLength"] for entry in data]

@app.route("/")
def index():
    current_timestamp = datetime.now().timestamp()
    current_cumulative = current_timestamp % cumulative_lengths[-1]
    index = bisect.bisect_left(cumulative_lengths, current_cumulative)
    return render_template("index.html", data = data[index])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
