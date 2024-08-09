import os
import subprocess
from datetime import datetime, timedelta
import time
import random

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
            # Use the --date option to set the commit date
            run_git_command(f'git commit --date="{author_date.strftime("%a %b %d %H:%M:%S %Y")}" -m "{commit_message}"')
            run_git_command('git push')
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_date = datetime.strptime("2024-06-16", '%Y-%m-%d')
    end_date = datetime.strptime("2024-08-24", '%Y-%m-%d')
    delta_days = (end_date - start_date).days + 1

    # Select 60 random days out of the delta_days
    commit_days = random.sample(range(delta_days), 60)

    for day_offset in commit_days:
        commit_date = start_date + timedelta(days=day_offset)
        num_commits = random.randint(1, 8)  # Random number of commits between 1 and 8
        main(commit_date, num_commits)
        time.sleep(1)  # Sleep for 1 second between different dates to simulate time progression
