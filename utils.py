import subprocess

def run_code_and_get_errors(code: str) -> str:
    with open("temp_code.py", "w") as f:
        f.write(code)

    try:
        output = subprocess.check_output(["python", "temp_code.py"], stderr=subprocess.STDOUT, timeout=5, text=True)
        return "✅ Code ran successfully!\n\n" + output
    except subprocess.CalledProcessError as e:
        return f"❌ Error:\n{e.output}"
    except subprocess.TimeoutExpired:
        return "⚠️ Error: Code took too long to run."
