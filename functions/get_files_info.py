import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_target_dir):
        return f'Error: "{directory}" is not a directory'

    contents = os.listdir(abs_target_dir)

    try:
        result_list = list(map(lambda name: format_entry(abs_target_dir, name), contents))
        return "\n".join(result_list)
    except Exception as e:
        return f"Error listing files: {e}"


def format_entry(directory, name):
    path = os.path.join(directory, name)

    size = os.path.getsize(path)
    is_dir = os.path.isdir(path)

    return f"- {name}: file_size={size} bytes, is_dir={is_dir}"
