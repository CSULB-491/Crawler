from flask import Flask, render_template

# gotta figure out how to change the path to src since I do not know where the templates directory is
# within the flask. Tried 'root_path' but it isnt working
app = Flask(__name__, root_path='Crawler/src/')


# app name
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return render_template("src/404.html")


app.run()
