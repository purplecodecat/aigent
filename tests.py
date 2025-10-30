from functions.get_files_info import get_files_info 
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test_get_files_info():
    current_test = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(current_test)
    print("")

    pkg_test = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(pkg_test)
    print("")

    errortest1 = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(errortest1)
    print("")

    errortest2 = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(errortest2)
    print("")


def test_get_file_content__truncation():
    result = get_file_content("calculator", "lorem.txt")
    print("Result for 'lorem.txt':")
    print(result)
    print("")


def test_get_file_content():
    result = get_file_content("calculator", "main.py")
    print("Result for 'main.py' file:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg/calculator.py' file:")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin/cat' file:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for missing file:")
    print(result)
    print("")


def test_write_file():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for 'lorem.txt':")
    print(result)
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for 'pkg/morelorem.txt':")
    print(result)
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for writing outside working directory:")
    print(result)
    print("")


def test_run_python_file():
    result = run_python_file("calculator", "main.py")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    print("")

    result = run_python_file("calculator", "lorem.txt")
    print(result)
    print("")



if __name__ == "__main__":
    print("Running tests...\n\n")
    # test_get_files_info()
    # test_get_file_content__truncation()
    # test_get_file_content()
    # test_write_file()
    test_run_python_file()
