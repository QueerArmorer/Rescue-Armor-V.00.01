import subprocess
import os
import time
import json

# Function to run the Blender Classroom Benchmark and record the time
def run_blender_classroom_benchmark():
    try:
        # Run Blender Classroom Benchmark using GPU
        start_time = time.time()
        subprocess.run(["blender-benchmark", "--scene", "classroom", "--device", "GPU"], check=True)
        end_time = time.time()

        # Calculate and record the benchmark time
        benchmark_time = end_time - start_time
        with open("classroom_benchmark_results.json", "w") as results_file:
            json.dump({"benchmark_time": benchmark_time}, results_file)

        print(f"Classroom Benchmark completed in {benchmark_time:.2f} seconds.")
    except subprocess.CalledProcessError:
        print("Error running Blender Classroom Benchmark with GPU.")
    except FileNotFoundError:
        print("Blender Benchmark not found. Make sure it's installed.")

if __name__ == "__main__":
    if os.path.exists("classroom_benchmark_results.json"):
        print("Classroom Benchmark results already recorded. Use Script 2 for comparison.")
    else:
        run_blender_classroom_benchmark()

