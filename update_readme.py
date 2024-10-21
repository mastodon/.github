import feedparser
from datetime import datetime

# Fetch the RSS feed
feed_url = "https://blog.joinmastodon.org/index.xml"
feed = feedparser.parse(feed_url)


# Function to format the publication date
def format_date(published):
    try:
        # Parse the published date from the entry
        parsed_date = datetime(*published[:6])
        return parsed_date.strftime("%Y-%m-%d")
    except Exception as e:
        # Return an empty string if date parsing fails
        return ""


# Extract the latest 3 posts
max_posts = 3
latest_posts = []
for entry in feed.entries[:max_posts]:
    title = entry.title
    link = entry.link
    pub_date = format_date(entry.published_parsed)  # Format the publication date
    # Add the post with the title, publication date, and optionally the summary
    latest_posts.append(f"- :newspaper: [{title}]({link}) - *{pub_date}*")

with open("profile/README.md", "r") as readme_file:
    readme_content = readme_file.readlines()

start_marker = "<!-- BLOG-POST-LIST:START -->\n"
end_marker = "<!-- BLOG-POST-LIST:END -->\n"

# Ensure the markers are present in the README.md
if start_marker not in readme_content or end_marker not in readme_content:
    print("Markers not found in README.md. Please ensure you have the markers.")
    exit(1)

# Get the content before and after the markers
start_index = readme_content.index(start_marker) + 1
end_index = readme_content.index(end_marker)

# Create the new content between the markers
new_readme_content = (
    readme_content[:start_index]
    + [f"{post}\n" for post in latest_posts]
    + readme_content[end_index:]
)

# Write the new content back to README.md
with open("profile/README.md", "w") as readme_file:
    readme_file.writelines(new_readme_content)

print("profile/README.md has been updated with the latest blog posts.")
