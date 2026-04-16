import vpype
import subprocess

def optimize(in_filename, out_filename):
    subprocess.run(["vpype", "read",in_filename, "linesort", "write", out_filename])