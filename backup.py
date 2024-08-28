import subprocess
import datetime

# Database credentials
db_host = 'localhost'
db_port = '5432'
db_name = 'your_database_name'
db_user = 'your_username'
db_password = 'your_password'

# Backup directory is in the local disc of the Linux server and in directory /mnt/backups
backup_dir = '/mnt/backups/'

# Generate backup file name
backup_file = backup_dir + 'backup_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.sql'

# Command to perform the backup
backup_command = f'pg_dump -h {db_host} -p {db_port} -U {db_user} -Fc -f {backup_file} {db_name}'

# Execute the backup command
try:
    subprocess.run(backup_command, shell=True, check=True)
    print('Backup completed successfully!')
except subprocess.CalledProcessError as e:
    print(f'Backup failed: {e}')s