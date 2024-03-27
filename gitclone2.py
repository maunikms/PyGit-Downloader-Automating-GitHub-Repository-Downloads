import subprocess

# Path to the file containing the list of repository URLs
url_list_file = "repository_urls.txt"

# Open the file containing repository URLs
with open(url_list_file, "r") as file:
    # Read repository URLs line by line
    for url in file:
        # Remove leading/trailing whitespace and newline characters
        url = url.strip()
        
        # Check if the line is not empty
        if url:
            # Clone the repository
            try:
                subprocess.run(["git", "clone", url])
                print(f"Repository cloned: {url}")
            except Exception as e:
                print(f"Error cloning repository {url}: {e}")
