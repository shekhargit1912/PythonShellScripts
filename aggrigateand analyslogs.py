import os
from datetime import datetime, timedelta

def aaggregate_logs(log_dir,outputfile):
    with open(outputfile,"w",encoding="utf-8") as outfile:
        for log_file in os.listdir(log_dir):
            if log_file.endswith(".log"):
                with open(os.path.join(log_dir,log_file),'r',encoding="utf-8") as infile:
                    for line in infile:
                        outfile.write(line)
    print(f"Aggregated logs written to {outputfile}")
                
def analyze_logs(log_file):
    error_count= 0
    Warning_count=0
    with open(log_file,"r",encoding="utf-8") as file:
        for line in file:
            if "Error" in line:
                error_count+=1
            elif "Warning" in line:
                Warning_count+=1
    print(f"Total Error logs: {error_count}")
    print(f"Total Warning logs: {Warning_count}")

if __name__=="__main__":
    log_directory= r"C:\path\to\log\directory"
    aggregated_log_file= r"C:\path\to\output\aggregated_logs.txt"
    
    aaggregate_logs(log_directory,aggregated_log_file)
    analyze_logs(aggregated_log_file)
