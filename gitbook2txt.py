import requests
from bs4 import BeautifulSoup
import os
import sys
from urllib.parse import urlparse

# Check if the command line argument (GitBook URL) is provided
if len(sys.argv) != 2:
    print("Usage: python gitbook2txt.py [GitBook URL]")
    sys.exit(1)
    
gitbook_url = sys.argv[1]

# Function to generate filename from URL
def get_filename_from_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace(".", "_")
    path = parsed_url.path.strip("/").replace("/", "_")
    if path:
        return f"{domain}_{path}.txt"
    return f"{domain}.txt"

# Main function to download the entire Gitbook into one file
def download_gitbook(main_url):
    try:
        response = requests.get(main_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get filename from URL
        output_filename = get_filename_from_url(main_url)
        
        # Open one file for all content
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            # Write header with source information
            output_file.write(f"# GitBook Content: {soup.title.string}\n")
            output_file.write(f"# Source URL: {main_url}\n\n")
            
            # Find all links in the GitBook
            links = soup.find_all('a')
            page_urls = set()
            for link in links:
                href = link.get('href')
                if href and not href.startswith('http'):
                    full_url = requests.compat.urljoin(main_url, href)
                    page_urls.add(full_url)
            
            # Process the main page first
            output_file.write(f"## PAGE: {soup.title.string}\n\n")
            main_content = soup.get_text()
            output_file.write(main_content)
            output_file.write("\n\n" + "-"*80 + "\n\n")
            print(f"Added main page content")
            
            # Download and add each page
            for url in page_urls:
                try:
                    page_response = requests.get(url)
                    page_response.raise_for_status()
                    page_soup = BeautifulSoup(page_response.content, 'html.parser')
                    
                    # Add page title as section header
                    page_title = page_soup.title.string
                    output_file.write(f"## PAGE: {page_title}\n\n")
                    
                    # Add page content
                    page_content = page_soup.get_text()
                    output_file.write(page_content)
                    
                    # Add separator between pages
                    output_file.write("\n\n" + "-"*80 + "\n\n")
                    
                    print(f"Added: {page_title}")
                except Exception as e:
                    print(f"Error downloading page {url}: {e}")
            
            print(f"\nAll content saved to: {output_filename}")
            
    except Exception as e:
        print(f"Error downloading GitBook: {e}")

# Run the script with the provided GitBook URL
download_gitbook(gitbook_url)
