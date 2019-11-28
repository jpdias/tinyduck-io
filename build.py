Import("env")

print("Encoding script.duck")
env.Execute("java -jar encoder.jar -i script.duck -o output.bin -l pt")

print("Removing old source")
env.Execute("rm src/main.cpp")

print("Generating source code")
env.Execute("python duck2spark.py -i output.bin -l 4 -f 2500 -r 3000 -o src/main.cpp")

print("Removing temporary files")
env.Execute("rm output.bin")