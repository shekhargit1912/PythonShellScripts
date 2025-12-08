import subprocess
import os
import datetime
import boto3

db_name = "mydb"
db_user = "admin"
backup_dir = "/backups"
s3_bucket_name = "your-s3-bucket-name"
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_file= f'{backup_dir}/{db_name}_backup_{timestamp}.sql'

dump_command = 'pg_dump -U {db_user} {db_name} > {backup_file}'
subprocess.run(dump_command,shell=True,check=True) # This line executes the pg_dump command in the shell to create a backup of the database.
print(f"Backup of database '{db_name}' completed: {backup_file}")
s3 = boto3.client('s3')
s3.upload_file(backup_file,s3_bucket_name,os.path.basename(backup_file))# This line uploads the backup file to the specified S3 bucket.
print(f"Backup file '{backup_file}' uploaded to S3 bucket '{s3_bucket_name}'")

# Optional: Remove backups older than 7 days
retention_days = 7
now = datetime.datetime.now()
for filename in os.listdir(backup_dir):
    if filename.startswith(f"{db_name}_backup_") and filename.endswith(".sql"):
        file_path = os.path.join(backup_dir, filename)
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if (now - file_mtime).days > retention_days:
            os.remove(file_path)
            print(f"Old backup file '{file_path}' removed.")
