import subprocess
import os
from tqdm import tqdm

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def seperate_time(time_str):
    time_str = time_str.replace(" ", "").replace("ms", "")
    time_str = time_str.split("?")[1].replace("\n", "")
    for c in time_str:
        if not c.isdigit():
            time_str = time_str.replace(c, "")
    return int(time_str)

def run_cpp(n=10):
    times = []
    file_path = "./cpp/3x+1.cpp"

    subprocess.run(["g++", file_path, "-o", "3x+1"])
    print("Compiled C++ file")

    for i in tqdm(range(n), desc="Running C++", leave=False):
        # Run the compiled C++ file
        result = subprocess.run(["./3x+1"], stdout=subprocess.PIPE)
        out_str = result.stdout.decode("utf-8")
        out_str = seperate_time(out_str)
        times.append(int(out_str))
    
    avg = sum(times) / len(times)
    print("finished C++")
    return avg

def run_fortran(n=10):
    times = []
    file_path = "./fortran/3x+1.f90"

    # Compile the Fortran file
    subprocess.run(["gfortran", file_path, "-o", "3x+1"])
    print("Compiled Fortran 90 file")

    for i in tqdm(range(n), desc="Running Fortran", leave=False):
        # Run the compiled Fortran file
        result = subprocess.run(["./3x+1"], stdout=subprocess.PIPE)
        out_str = result.stdout.decode("utf-8")
        out_str = seperate_time(out_str)
        times.append(int(out_str))
    
    avg = sum(times) / len(times)
    print("finished Fortran 90")
    return avg

def run_python(n=10):
    times = []
    file_path = "./py/3x+1.py"

    for i in tqdm(range(n), desc="Running Python", leave=False):
        # Run the Python file
        result = subprocess.run(["python", file_path], stdout=subprocess.PIPE)
        out_str = result.stdout.decode("utf-8")
        out_str = seperate_time(out_str)
        times.append(int(out_str))
    
    avg = sum(times) / len(times)
    print("finished Python")
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
        out_str = seperate_time(out_str)
        times.append(int(out_str))
    
    avg = sum(times) / len(times)
    print("finished Go")
    return avg

def run_java(n=10):
    pass


def main():
    print("approx 30s per run")
    n = int(input("How many times to run each program? "))
    py_avg = run_python(n)
    #py_avg = 0
    cpp_avg = run_cpp(n)
    for_avg = run_fortran(n)
    go_avg = run_go(n)
    
    print("\n")
    
    time_dict = {
        "Python": py_avg,
        "C++": cpp_avg,
        "Fortran 90": for_avg,
        "Go": go_avg
    }
    
    # Sort the dictionary by value
    sorted_dict = {k: int(v) for k, v in sorted(time_dict.items(), key=lambda item: item[1])}
    
    print("lang".ljust(16), "avg time")
    for lang, avg_time in sorted_dict.items():
        print(lang.ljust(16), str(avg_time) +  "ms")
        
    

if __name__ == "__main__":
    main()