import subprocess
import os
from tqdm import tqdm

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def run_cpp(n=10):
    times = []
    file_path = "./cpp/3x+1.cpp"

    subprocess.run(["g++", file_path, "-o", "3x+1"])
    print("Compiled C++ file")

    for i in tqdm(range(n), desc="Running C++", leave=False):
        # Run the compiled C++ file
        result = subprocess.run(["./3x+1"], stdout=subprocess.PIPE)
        out_str = result.stdout.decode("utf-8")
        for c in out_str:
            if not c.isdigit():
                out_str = out_str.replace(c, "")
        times.append(int(out_str))
    
    avg = sum(times) / len(times)
    return avg

def run_fortran(n=10):
    times = []
    file_path = "./fortran/3x+1.f90"

    # Compile the Fortran file
    subprocess.run(["gfortran", file_path, "-o", "3x+1"])
    print("Compiled Fortran file")

    for i in tqdm(range(n), desc="Running Fortran", leave=False):
        # Run the compiled Fortran file
        result = subprocess.run(["./3x+1"], stdout=subprocess.PIPE)
        out_str = result.stdout.decode("utf-8")
        for c in out_str:
            if not c.isdigit():
                out_str = out_str.replace(c, "")
        times.append(int(out_str))
    
    avg = sum(times) / len(times)
    return avg

def run_python(n=10):
    times = []
    file_path = "./py/3x+1.py"

    for i in tqdm(range(n), desc="Running Python", leave=False):
        # Run the Python file
        result = subprocess.run(["python", file_path], stdout=subprocess.PIPE)
        out_str = result.stdout.decode("utf-8")
        for c in out_str:
            if not c.isdigit():
                out_str = out_str.replace(c, "")
        times.append(int(out_str))
    
    avg = sum(times) / len(times)
    return avg

def run_go(n=10):
    times = []
    file_path = "./go/3x+1.go"

    # Compile the Go file
    subprocess.run(["go", "build", "-o", "3x+1", file_path])
    print("Compiled Go file")

    for i in tqdm(range(n), desc="Running Go", leave=False):
        # Run the compiled Go file
        result = subprocess.run(["./3x+1"], stdout=subprocess.PIPE)
        out_str = result.stdout.decode("utf-8")
        for c in out_str:
            if not c.isdigit():
                out_str = out_str.replace(c, "")
        times.append(int(out_str))
    
    avg = sum(times) / len(times)
    return avg



def main():
    print("approx 30s per run")
    n = int(input("How many times to run each program? "))
    #py_avg = run_python(n)
    cpp_avg = run_cpp(n)
    for_avg = run_fortran(n)
    go_avg = run_go(n)
    
    #print("Python average:", py_avg)
    print("C++ average:", cpp_avg)
    print("Fortran average:", for_avg)
    print("Go average:", go_avg)

if __name__ == "__main__":
    main()