from flask import Flask, request, jsonify
import subprocess
import os
import json

app = Flask(__name__)

@app.route("/invoke", methods=["POST"])
def invoke():
    data = request.get_json()

    function_name = data.get("function")
    params = data.get("params", {})

    function_path = f"/functions/{function_name}.py"

    if not os.path.exists(function_path):
        return jsonify({"error": f"Function file not found: {function_path}"}), 400

    # Set environment variables for the function runner
    env = os.environ.copy()
    env["FUNC_FILE"] = f"/functions/{function_name}.py"
    env["FUNC_EVENT"] = json.dumps(params)

    try:
        # Call run_function.py as subprocess
        result = subprocess.run(
            ["python", "run_function.py"],
            capture_output=True,
            text=True,
            cwd="/handler",
            env=env
        )

        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500

        return jsonify(json.loads(result.stdout))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
