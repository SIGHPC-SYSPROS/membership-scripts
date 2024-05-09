import pandas as pd

# Load the data from the CSV file
file_path = '~/Downloads/0324-chapter_member_listing_expired-cleanup.csv'  # Update this to the path of your CSV file
data = pd.read_csv(file_path)

# Filter the rows where the Status is 'expired'
expired_members = data[data['Status'] == 'expired']

# Select only the First Name, Last Name, and E-mail columns
selected_columns = expired_members[['First Name', 'Last Name', 'E-mail']]

# Optionally, save the result to a new CSV file
selected_columns.to_csv('expired_members.csv', index=False)

# Print the resulting data
print(selected_columns)
