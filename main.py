from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SERVERX OFFICIAL WEBSITE</title>
    <style>
        body {
            font-family: sans-serif;
            margin: 0;
            background-color: #f0f0f0; /* Light gray background */
            color: #333; /* Dark gray text color */
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
        }
        .header img {
            max-width: 200px; /* Adjust as needed */
        }
        .navigation {
            background-color: #333; /* Dark gray background */
            color: #fff; /* White text color */
            padding: 10px;
            text-align: center;
        }
        .navigation a {
            color: #fff;
            text-decoration: none;
            padding: 10px;
        }
        .navigation a:hover {
            background-color: #555; /* Slightly lighter gray on hover */
        }
        .content {
            background-color: #fff; /* White background for content */
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        }
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #333; /* Dark gray background */
            color: #fff; /* White text color */
        }
        .screenshot {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto; /* Center the image */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* Add a shadow */
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>OFFICAL SERVERX</h1>
            <nav class="navigation">
                <a href="https://www.youtube.com/@legend4bhi_inxide">Youtube</a>
                <a href="https://www.mediafire.com/file/13nirayy273un6l/SERVERX.apk/file">Download From Here</a>
                <a href="https://about-ypme.onrender.com">About</a>
            </nav>
        </div>
        <div class="content">
            
            <p></p>
            <img class="screenshot" src="https://i.ibb.co/0jycjpQq/bc00634ab05629e026847814ebac4a26.jpg" alt="SHAWX App Screenshot"> <p style="text-align:center;"></p>
            <p style="text-align:center;">Version 1.2</p>
        </div>
        <div class="footer">
        	
            <p>&copy; 2025 Serverx Abhi. All rights reserved.</p>
        </div>
    </div>
</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
