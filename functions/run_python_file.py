import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if os.path.splitext(abs_file_path)[-1].lower() != ".py":
        return f'Error: File "{file_path}" is not a Python file.'

    command = ["uv", "run", abs_file_path] + args

    try:
        complete = subprocess.run(
            command,
            timeout=30, 
            capture_output=True,
            text=True,
            cwd=abs_working_dir
        )

    except Exception as e:
        return f"Error: executing Python file: {e}"

    parts = []
    if complete.stdout != "":
        parts.append(f"STDOUT:\n{complete.stdout}")
    if complete.stderr != "":
        parts.append(f"STDERR:\n{complete.stderr}")
    if complete.returncode != 0:
        parts.append(f"Process exited with code {complete.returncode}")

    if len(parts) == 0:
        return "No output produced"
    return "\n".join(parts)
        


