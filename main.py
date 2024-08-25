import os
import subprocess
from datetime import datetime, timedelta
import time
import random

def set_git_env_variable(author_date):
    os.environ['GIT_AUTHOR_DATE'] = author_date.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Environment variable set: GIT_AUTHOR_DATE={os.environ['GIT_AUTHOR_DATE']}")

def modify_file(file_path, content):
    with open(file_path, 'a') as file:  # Use 'a' mode to append to the file
        file.write(content + '\n')
    print(f"Modified file: {file_path}")

def run_git_command(command):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def main(author_date, num_commits):
    for _ in range(num_commits):
        # Set the environment variable
        set_git_env_variable(author_date)

        # Path to the file to be modified
        file_path = './text.txt'

        # Content to write to the file (make it unique)
        new_content = f"This is the new content of the file at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."

        # Modify the file
        modify_file(file_path, new_content)

        # Git commands to add, commit, and push changes
        try:
            run_git_command('git add .')
            commit_message = f"Update file at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            run_git_command(f'git commit -m "{commit_message}"')
            run_git_command('git push')
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

if __name__ == "_main_":
    start_date = datetime.strptime("2023-01-01", '%Y-%m-%d')
    end_date = datetime.strptime("2023-03-31", '%Y-%m-%d')
    delta_days = (end_date - start_date).days + 1

    # Select 300 random days out of 365
    commit_days = random.sample(range(delta_days), 60)

    for day_offset in commit_days:
        commit_date = start_date + timedelta(days=day_offset)
        num_commits = random.randint(1, 8)  # Random number of commits between 1 and 10
        main(commit_date, num_commits)
        time.sleep(1)  # Sleep for 1 second between different dates to simulate time progression