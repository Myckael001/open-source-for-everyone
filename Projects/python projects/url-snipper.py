import re

name = input("You Are Looking For A Username On Which Application: ") # Applications Such As Facebook, Instagram, Twitter Etc

url = input(f"I Need The URL From {name}: ").strip() # Give Your URL To Get Username

def main(name, url):

    catch = rf"^https?://(?:www\.)?{re.escape(name)}.com/(?:[a-zA-Z0-9.-]+/)?/?(\d+)?/?@?([a-zA-Z0-9_.-]+)" # How Its Going Snip Your Name
    
    if matches := re.search(catch, url, re.IGNORECASE):
        print(f"This {name} Accounts Username:", matches.group(2)) # matches.group(2) Is Giving Us The Second Capturing Group
        
    else:
        print("Incorrect Application Or URL")

if __name__ == "__main__":
    main(name, url)