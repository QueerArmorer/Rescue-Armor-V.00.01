import subprocess

# We-a check da CPU
cmd = ["blender", "-b", "blender_benchmark_1.0.0.blend", "-f", "1", "--render-output", "temp", "-t", "0"]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait your turn, asshole
output, error = process.communicate()
time_taken = float(output.split(b"Time: ")[1].split(b" ")[0])

# Are you still all there?
with open("good_cpu_time.txt", "r") as f:
    good_time = float(f.read())

# Talk to me, Goose.
if time_taken > good_time * 1.05:
    print("Performance degradation detected! The system may be compromised, Rescue Armor cannot verify the security of this system.")
else:
    print("Rescue Armor did not detect any degredation in CPU performance.")

