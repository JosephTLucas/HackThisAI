from challenge import app
from flask import Flask
import markdown
import markdown.extensions.fenced_code


@app.route("/", methods=["GET"])
def index():
    with open("README.md", "r") as readme:
        md_template = markdown.markdown(readme.read(), extensions=["fenced_code"])
    return md_template
