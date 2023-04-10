#!/usr/bin/env python3
"""importing flask modules to render
The page.
"""
from flask import flask, render_template


app = (__flask__)


@app.route('/')
def get_index():
    """The index rendering"""
    return render_template('0-index.html') 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

