import csv
import names
import random


num_workers = 400 #Generate 400 workers
workers = [] # Create an empty variable list
for employee in range(num_workers): # List the information that will be displayed in the empty list
    name = names.get_full_name()
    gender = random.choice(['Male', 'Female'])
    job = random.choice(['Labourer', 'Engineer', 'Foreman', 'Electrician', 'Plumber', 'Carpenter'])
    salary = random.randint(5000, 35000)
    workers.append({'Employee Name': name, 'Gender': gender, 'Job Title': job, 'Salary': salary}) # Defines how the info will be displayed in the workers [] list frame
#print(workers[:5]) # Displaying the first five workers for example to check code functionality
  
#Generate payment slips
payment_slips = []
for worker in workers:
    try:
        slip = {
            "Employee Name": worker['Employee Name'], 
            "Gender": worker['Gender'],
            "Job Title": worker['Job Title'],
            "Salary": worker['Salary'], 
            "Employee Level": None
        }
        #Conditional statements to assign Employee Level
        if 10000 < worker['Salary'] < 20000: 
            slip["Employee Level"] = "A1"
        elif 7500 < worker['Salary'] < 30000 and worker['Gender'] == "Female": 
            slip["Employee Level"] = "A5-F"
        else: 
            slip["Employee Level"] = "Not disclosed"
        # Generating payment slip format 
        payment_slips.append(slip) #Add everything in slip to the payment slip [] list frame.
    except Exception as e:
        print(f"Error generating slip for {worker['Employee Name']}: {e}")
#Displaying a sample of payment slips
print(payment_slips[:5]) # Displaying the first five payment slips for example        

#Export to CSV file
csv_file = 'highridge_construction_payment_slips.csv'
with open(csv_file, mode='w', newline='') as file: 
    writer = csv.DictWriter(file, fieldnames=payment_slips[0].keys())
    writer.writeheader()
    writer.writerows(payment_slips)
print(f"csv file {csv_file} created successfully!")    