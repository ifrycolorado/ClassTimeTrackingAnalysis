import pandas as pd

def extract_domain(tag):
    # Count the number of occurrences of 'Domain:'
    domain_count = tag.count('Domain:')
    
    # If there are multiple 'Domain:', mark as "DUP"
    if domain_count > 1:
        return "DUP"
    # Otherwise, extract the Domain
    else:
        match = pd.Series(tag).str.extract(r'Domain: ([\w\s]+),')
        return match.iloc[0, 0]
    
def extract_type(tag):
    print(f"Processing tag: {tag}")  # Debugging print
    type_count = tag.count('Type:')
    
    if type_count > 1:
        print("Multiple 'Type:' found.")  # Debugging print
        return "DUP"
    elif type_count == 1:
        match = pd.Series(tag).str.extract(r'Type: (.+)$')
        print(f"Extracted match: {match}")  # Debugging print
        if not match.empty and match.iloc[0, 0] is not None:
            return match.iloc[0, 0]
        else:
            print("No match found.")  # Debugging print
            return None
    else:
        print("'Type:' not found.")  # Debugging print
        return None