library(randomNames)
library(csv)

# Define job titles and departments for random selection
job_titles <- c('Laborer', 'Engineer', 'Foreman', 'Electrician', 'Plumber', 'Carpenter')
genders <- c('Male', 'Female')

# Generate employee details
num_workers <- 400
workers <- data.frame(matrix(ncol = 4, nrow = num_workers))
colnames(workers) <- c('Employee Name', 'Gender', 'Job Title', 'Salary')

for (employee in 1:num_workers) {
  workers$`Employee Name`[employee] <- randomNames(which.names = 'both')
  workers$Gender[employee] <- sample(genders, 1)
  workers$`Job Title`[employee] <- sample(job_titles, 1)
  workers$Salary[employee] <- sample(5000:35000, 1)
}

print(head(workers)) # Printing the first 6 Rows of the workers data frame to ensure code functionality

payment_slips <- data.frame(matrix(ncol = 5, nrow = num_workers))
colnames(payment_slips) <- c('Employee Name', 'Gender', 'Job Title', 'Salary', 'Employee Level')

for (worker in 1:nrow(workers)) {
  tryCatch({
    slip <- list(
      "Employee Name" = workers$`Employee Name`[worker],
      "Gender" = workers$Gender[worker],
      "Job Title" = workers$`Job Title`[worker],
      "Salary" = workers$Salary[worker],
      "Employee Level" = NA
    )
    
    # Conditional statements to assign employee level
    if (10000 < workers$Salary[worker] & workers$Salary[worker] < 20000) {
      slip$"Employee Level" <- "A1"
    }
    
    else if (7500 < workers$Salary[worker] & workers$Salary[worker] < 30000 & workers$Gender[worker] == "Female") {
      slip$"Employee Level" <- "A5-F"
    }
    else {
      slip$"Employee Level" <- "Not disclosed"
    }
    payment_slips[worker, ] <- slip
  }, error = function(e) {
    print(paste("Error processing worker details for", workers$`Employee Name`[worker], ":", e)) # 'Print' Outputs the error message, which 'Paste' has concatenated, into the console
  })
}

print(head(payment_slips)) # Printing the first 6 Rows of the payment_slips data frame to ensure code functionality

View(payment_slips) # Opens an interactive viewer for exploring payment_slips data frame

# Export to CSV File
csv_file <- 'highridge_payslip.csv' # Creates and Names a csv file

write.csv(payment_slips, file = csv_file, row.names = FALSE) # Writes the payment_slip data frame into the created csv file 

print(paste("CSV file", csv_file, "created successfully.")) # 'Print' Outputs the result, which 'Paste' has concatenated, into the console

