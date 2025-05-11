# gitbook2txt
Converts a documentation to text - for ai propting

A simple Python script that downloads an entire GitBook website and saves all content into a single text file optimized for LLM context.

## Overview

This tool allows you to easily extract content from GitBook documentation sites for various purposes:
- Creating offline documentation archives
- Preparing context for AI/LLM applications
- Knowledge base extraction
- Content analysis

The script preserves the hierarchical structure of the GitBook by including page titles as section headers within the single output file.

## Features

- Downloads all accessible pages from a GitBook URL
- Consolidates all content into a single text file
- Includes clear page demarcations with titles
- Names the output file based on the input URL
- Handles errors gracefully, continuing with available pages if some fail
- Shows progress during the download process

## Requirements

- Python 3.6+
- Required Python packages:
  - requests
  - beautifulsoup4

## Installation

Install the required dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage

Run the script from the command line with a GitBook URL as the argument:

```bash
python gitbook2txt.py https://your-gitbook-url.com
```

### Example

```bash
python gitbook2txt.py https://docs.example-project.com
```

The script will:
1. Start downloading all pages it can find from the GitBook
2. Show progress as it processes each page
3. Save everything to a single text file named after the URL (e.g., `docs_example-project_com.txt`)

## Output Format

The generated text file will have the following structure:

```
# GitBook Content: [GitBook Title]
# Source URL: [Original URL]

## PAGE: [Page 1 Title]
[Full content of page 1]

--------------------------------------------------------------------------------

## PAGE: [Page 2 Title]
[Full content of page 2]

--------------------------------------------------------------------------------

[And so on for all pages...]
```

This format is optimized for providing context to LLMs while preserving the document structure.

## Error Handling

If the script encounters errors while downloading specific pages, it will:
1. Print an error message for the problematic page
2. Continue processing the remaining pages
3. Include all successfully downloaded content in the final file

## Limitations

- The script can only access publicly available pages
- Some GitBooks with complex JavaScript-based navigation may not be fully captured
- Rate limiting on some sites might affect download speed or completeness
