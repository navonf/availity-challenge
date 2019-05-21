""" Main entry point for service """

from flask import Flask, jsonify, request
from Util import database_upload, local_upload, print_to_screen

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

@app.route("/")
def root():
    return jsonify({
                "message": "welcome to my file microservice",
                "author": "navon francis",
                "company": "availity"
            }), 200

@app.route("/add-file", methods=["POST"])
def file_intake():
    data = dict()
    provider_codes = {
        "provider1" : "database",
        "provider2" : "local",
        "provider3" : "print"
    }
    files = request.files
    provider_type = request.args.get("provider")

    if len(files) == 0:
        return jsonify({"error": "files not found"}), 404

    print()
    print("Thank you for the files.")
    print("Provider type of", provider_type)

    for f in files:
        data[f] = request.files[f]

    if provider_type == "provider1": database_upload(data)
    if provider_type == "provider2": local_upload(data)
    if provider_type == "provider3": print_to_screen(data)

    return jsonify({"type": provider_codes[provider_type]}), 200


if __name__ == "__main__":
    app.run(debug=False, use_reloader=True)