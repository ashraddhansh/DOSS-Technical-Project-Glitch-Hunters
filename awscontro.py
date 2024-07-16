import boto3
import tkinter as tk

# Function to fetch instances
def get_all_instances():
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    instances = ec2.describe_instances()
    return instances['Reservations']

# Function to fetch running instances
def get_running_instances():
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    return instances['Reservations']

# Function to start instance
def start_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    ec2.start_instances(InstanceIds=[instance_id])

# Function to stop instance
def stop_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    ec2.stop_instances(InstanceIds=[instance_id])

# Function to terminate instance
def terminate_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    ec2.terminate_instances(InstanceIds=[instance_id])

# Function to refresh instance list
def refresh_list():
    instance_list.delete(0, tk.END)
    if show_all_var.get():
        instances = get_all_instances()
    else:
        instances = get_running_instances()
    for reservation in instances:
        for instance in reservation['Instances']:
            instance_list.insert(tk.END, f"{instance['InstanceId']} - {instance['InstanceType']} ({instance['State']['Name']})")

# Function to launch instance
def launch_instance():
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    # Modify the following parameters as per your requirement
    response = ec2.run_instances(
        ImageId='ami-09298640a92b2d12c',  # Specify the AMI ID
        InstanceType='t2.micro',  # Specify the instance type
        MaxCount=1,
        MinCount=1
    )
    new_instance_id = response['Instances'][0]['InstanceId']
    refresh_list()  # Refresh instance list after launching the new instance

# Create the Tkinter window
root = tk.Tk()
root.title("AWS Instance Controller")

root.geometry('1200x800')
root.configure(background="#88B752")

text_label = tk.Label(root, text="AWS Control Panel", fg='black', bg='#88B752')
text_label.pack(pady=(50, 10))
text_label.config(font=("Vandana", 25))

# Create frames for buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, padx=150)

# Refresh button
refresh_btn = tk.Button(button_frame, text="Refresh List", command=refresh_list, font=("Arial", 14), bg='yellow', width=15, height=2)
refresh_btn.pack(fill=tk.X, pady=0)

# Show all instances checkbox
show_all_var = tk.BooleanVar()
show_all_checkbox = tk.Checkbutton(button_frame, text="Show All Instances", variable=show_all_var, command=refresh_list, font=("Arial", 14), bg='#88B752', width=15, height=2)
show_all_checkbox.pack(fill=tk.X, pady=0)

# Separator frame with background color
sep1_frame = tk.Frame(button_frame, bg='#88B752', height=5)
sep1_frame.pack(fill=tk.X, pady=(0, 5))

# Start button
start_btn = tk.Button(button_frame, text="Start Instance", command=lambda: start_instance(instance_list.get(tk.ACTIVE).split()[0]), font=("Arial", 14), bg='yellow', width=15, height=2)
start_btn.pack(fill=tk.X, pady=0)

# Separator frame with background color
sep1_frame = tk.Frame(button_frame, bg='#88B752', height=5)
sep1_frame.pack(fill=tk.X, pady=(0, 5))


# Stop button
stop_btn = tk.Button(button_frame, text="Stop Instance", command=lambda: stop_instance(instance_list.get(tk.ACTIVE).split()[0]), font=("Arial", 14), bg='yellow', width=15, height=2)
stop_btn.pack(fill=tk.X, pady=0)

# Separator frame with background color
sep1_frame = tk.Frame(button_frame, bg='#88B752', height=5)
sep1_frame.pack(fill=tk.X, pady=(0, 5))


# Terminate button
terminate_btn = tk.Button(button_frame, text="Terminate Instance", command=lambda: terminate_instance(instance_list.get(tk.ACTIVE).split()[0]), font=("Arial", 14), bg='yellow', width=15, height=2)
terminate_btn.pack(fill=tk.X, pady=0)

# Separator frame with background color
sep1_frame = tk.Frame(button_frame, bg='#88B752', height=5)
sep1_frame.pack(fill=tk.X, pady=(0, 5))


# Launch button
launch_btn = tk.Button(button_frame, text="Launch Instance", command=launch_instance, font=("Arial", 14), bg='yellow', width=15, height=2)
launch_btn.pack(fill=tk.X, pady=0)

# Create a frame for the instance list
list_frame = tk.Frame(root)
list_frame.pack(side=tk.RIGHT, padx=70)

# Create a listbox to display instances with increased height
instance_list = tk.Listbox(list_frame, width=50, font=("Arial", 14), height=25)
instance_list.pack(pady=10)

# Initial population of instance list
refresh_list()

# Start the Tkinter event loop
root.mainloop()
