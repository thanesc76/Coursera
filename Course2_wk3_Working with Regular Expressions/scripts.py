import re
import csv

def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):
    return True
  return False

def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'

  # modified
  csv_file_location = 'user_emails.csv'  
  report_file = 'updated_user_emails.csv'

  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []
  
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))  # list of list, if not put list(), <_csv.reader object at 0x0000022DF2167040>
    user_email_list = [data[1].strip() for data in user_data_list[1:]]  # user_data_list[1:] will contain data.  user_data_list[0] is header, data[0]=name data[1]=email.  data[1].strip() get rid of space
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)  # find index of ' Email Address' in a list
    for user in user_data_list[1:]:  # user_data_list[1:] contains list of list of name and email without header
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):  # zip return tuple, although inputs are lists
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
    f.close()
  
  with open(report_file, 'w+', newline = "") as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()

    
main()
