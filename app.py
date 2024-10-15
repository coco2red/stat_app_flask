from flask import Flask, render_template, send_file
from data import calculate_stats
import matplotlib.pyplot as plt
import io
import numpy as np
import markdown  # Import the markdown library
import os

app = Flask(__name__)

# Route for main page
@app.route('/')
def index():
    # Sample ages data
    ages = [13, 12, 11, 14, 13, 12, 15, 13, 11, 14, 13, 12]

    # Calculating basic statistics
    stats = calculate_stats(ages)

    # Pass both stats and the list of ages to the template
    return render_template('index.html', stats=stats, ages=ages)

# Route for the graph page
@app.route('/graph')
def graph():
    img = io.BytesIO()
    ages = [13, 12, 11, 14, 13, 12, 15, 13, 11, 14, 13, 12]
    age_counts = np.bincount(ages)
    plt.bar(range(len(age_counts)), age_counts, color='skyblue')
    plt.title('Frequency of Ages in Class')
    plt.xlabel('Ages')
    plt.ylabel('Number of Students')
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

# Route for the graph page template
@app.route('/graph_page')
def graph_page():
    return render_template('graph.html')

# Route for discussion page
@app.route('/discussion')
def discussion():
    # Read the markdown file and convert it to HTML
    with open(os.path.join(os.path.dirname(__file__), 'discussion.md'), 'r') as f:
        content = f.read()
    # Convert markdown to HTML
    html_content = markdown.markdown(content)
    return render_template('discussion.html', content=html_content)

if __name__ == "__main__":
    app.run(debug=True)
