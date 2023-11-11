import re
import os

# Search all files in scans/ directory for IP addresses, to see if any match.
# Regex used:
# ^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$
# Am scanning the already saved files in order to prevent unnecessary requests being made to server.

def ip_search(directory):

    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    total_matches = {}

    if os.path.isdir(directory): # Check directory exists
        
        for filename in os.listdir(directory):

            if os.path.isfile(os.path.join(directory, filename)): # Check is a file and not a directory - recursive depth of this is only 1, currently operates fine but worth looking into in the future
                
                with open(os.path.join(directory, filename)) as tmp_file:

                    tmp_file = tmp_file.read()
                    matches = re.findall(pattern, tmp_file)

                    if len(matches) > 0: # If any matches found, add to dict
                        total_matches[filename] = matches

        return(total_matches) # Return dictionary object with all the total regex matches

    else:
        return 'Scan has not been completed on target yet.'