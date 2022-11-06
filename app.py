from flask import Flask, render_template, request, redirect, flash
from process import paste_frame
import secrets

app = Flask(__name__)
# セッション情報を暗号化するためのキー設定
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def show_form():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if "file" not in request.files:
            flash("ファイルが選択されていません")
            return redirect(request.url)

        file = request.files["uploadfile"]

        if file.filename == "":
            flash("ファイルが選択されていません")
            return redirect(request.url)

        if file:
            outfile = paste_frame(file)
            return render_template("upload.html", outfile=outfile)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
