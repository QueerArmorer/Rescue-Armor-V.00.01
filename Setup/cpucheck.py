import subprocess

# We-a check da CPU
cmd = ["blender", "-b", "blender_benchmark_1.0.0.blend", "-f", "1", "--render-output", "temp", "-t", "0"]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait your turn, asshole
output, error = process.communicate()
time_taken = float(output.split(b"Time: ")[1].split(b" ")[0])

# And the time across the line was ...
with open("good_cpu_time.txt", "w") as f:
    f.write(str(time_taken))

