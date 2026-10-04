from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def status():

    return jsonify({
        "candidate": "candidate_1042",
        "status": "MORE_EVIDENCE_REQUIRED",

        "hypotheses": {
            "Moving astronomical object": 0.58,
            "Stationary astronomical source": 0.25,
            "Measurement or imaging artifact": 0.14,
            "Transient astronomical event": 0.03
        },

        "evidence": [
            "Motion detected",
            "Spectral evidence available",
            "Astronomical catalog match"
        ],

        "motion": {
            "delta_x": 4.0,
            "delta_y": 3.0,
            "displacement": 5.0,
            "velocity": 0.5
        },

        "catalog": {
            "matched": True,
            "catalog_id": "STAR-001",
            "name": "Known Star A",
            "distance_arcsec": 0.0
        }
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )