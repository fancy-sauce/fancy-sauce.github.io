---
layout: post
title: Bug Bounty Workflow
subtitle: Personal notes
gh-repo: fancy-sauce/fancy-sauce.github.io
gh-badge: [star, follow]
tags: [Automation, Nuclei, bugbounty, linux]
comments: true
---

## Get a scope from hackerone:
```
bbscope h1 -t YourAPIKeyHere -u HackeroneUsername -b -o t > targets.txt
```

# Retrieve only URLs in scope
```
bbscope h1 -t YourAPIKeyHere -u HackeroneUsername -b -o t -a -c url > targetURLs.txt
```

# Script to clean target list

```
#!/bin/bash

# Check if the input file exists
if [ -z "$1" ]; then
  echo "Usage: $0 <input_file>"
  exit 1
fi

input_file="$1"
output_file="targets_clean.txt"

# Remove "https://*.", "http://*.", "www.", and lines starting with "*."
# Also, remove any empty lines
sed -e 's|https\?://[^ ]*\.[^ ]*||g' \
    -e 's|^\*\.[^ ]*||g' \
    -e 's|www\.||g' \
    -e '/^$/d' "$input_file" > "$output_file"

echo "Cleaning complete. The results have been saved to $output_file."
```

# Clean target list

```
./cleantargets.sh targetURLs.txt
```

This will output targets_clean.txt

# Check for vulns against a list of hosts
(I used the bbscope command before to generate the list)
```
nuclei -list targets_clean.txt -tags rce
```

TEST