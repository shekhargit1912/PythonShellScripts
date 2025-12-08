

logs_file = r"\microservices_logs.txt" # file path

error_count={}
warning_count=0
with open(logs_file,"r",encoding="utf-8") as logfile:
    for line in logfile:
        if "ERROR" in line:
            error_message=line.strip()
            if error_message not in error_count:
                error_count[error_message]=0
            error_count[error_message]+=1
        elif "WARNING" in line:
            warning_count+=1
print("Error Type Counts:")
for error,count in error_count.items():
    print(f"{error}: {count}")
print(f"Total WARNING logs: {warning_count}")
total_errors=sum(error_count.values())
print(f"Total ERROR logs: {total_errors}")
# Calculate error rates
total_logs=0
with open(logs_file,"r") as logfile:
    for line in logfile:
        total_logs+=1
error_rate=(total_errors/total_logs)*100 if total_logs>0 else 0
warning_rate=(warning_count/total_logs)*100 if total_logs>0 else 0
print(f"Error Rate: {error_rate:.2f}%")
print(f"Warning Rate: {warning_rate:.2f}%")
