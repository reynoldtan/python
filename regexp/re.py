#!/usr/bin/env python3
import re
log = 'July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade'

# Using index
index = log.index('[')
print(log[index+1:index+6])

# Using regexp
# r is rawstring, interpreter shouldn't try to interpret any special
# characters, and instead just pass the string as is.
regexp = r"\[(\d+)\]"
result = re.search(regexp, log)
print(result[1])

result1 = re.search(r"aza", "plaza")
result2 = re.search(r"aza", "bazaar")
# Will return none - None is used in Python to indecate item is not found.
result3 = re.search(r"aza", "maze")
# Case-insensitive match using re.IGNORECASE
result3 = re.search(r"aza", "Maze", re.IGNORECASE)

# www.regex101.com
# https://docs.python.org/3/howto/regex.html
# . single chars: nic. = nice or nick
# ^ beginning of string: ^fruit = fruitcake
# $ end of string: cat$ = muscat, bobcat
# [] Character class: list chars to match 
#   [Pp]ython = Python or python
#   [a-z]way = lowercase letter from a to z - away, highway
#   [A-Z] = uppercase
#   [0-9] = digits
#   combine [a-zA-Z0-9]
# [^a-z] Not in the list = not a character
# cat|dog (pipe symbol) or search, if both are in a line only one will be returned
#   use re.findall() to return both.
# * Repetition Qualifiers 0 or many times
# ? Repetition Qualifiers 0 or 1 times
# + Repetition Qualifiers 1 or more times
# \w letters numbers and underscores
# \d digits
# \s spaces new lines tabs
# \b word boudaries \b[a-z]{5}\b words with 5 letters only
# {n1, n2} - n ranges [a-z]{5} letters repeating 5 times
#            n1 lower range and n2 upper range
#            \w{5, 10} - at least 5 or 10 letters
#            \w{5, } - at least 5 and no limit.
#            \w{, 10} - 0 up to 10 repetitions. 

# Capturing groups - enclosed in ().
result = re.search(r"^(\w*), (\w*)$", "Lovelace Ada")
# Return 2 groups lastnamd and firstname.
print(result.groups())
# result[0] will containt the full match
# result[1] is the first group - lastname
# result[2] is the 2nd group - firstname

# SPLITTING AND REPLACING
re.split(r"[.?!]", 'Sentence one. Sentence 2? Sentence 3!')
# Result will exclude punctuation marks. To include them use ()
re.split(r"([.?!])", 'Sentence one. Sentence 2? Sentence 3!')

# Replace email with [REDACTED]
re.sub(r"[\w.%+-]+@[\w.-]+", '[REDACTED]', 'Received email from gome@my.example.ca')

# Order of captured group. \2 is the 2nd capture group and \1 is the first.
re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
# Ada Lovelace

# Fill in the code to check if the text passed contains the vowels a, e and i, 
# with exactly one occurrence of any other character in between.
def check_aei (text):
  result = re.search(r".a.e.i.", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

# Fill in the code to check if the text passed contains punctuation symbols: commas, periods, 
# colons, semicolons, question marks, and exclamation points.
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False


# The repeating_letter_a function checks if the text passed includes the 
# letter "a" (lowercase or uppercase) at least twice. For example, 
# repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. 
# Fill in the code to make this work. 
def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


# Fill in the code to check if the text passed looks like a standard sentence, 
# meaning that it starts with an uppercase letter, followed by at least some 
# lowercase letters or a space, and ends with a period, question mark, or 
# exclamation point. 
def check_sentence(text):
  result = re.search(r"^[A-Z].*[\.\?\!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


# Fix the regular expression used in the rearrange_name function so that 
# it can match middle names, middle initials, as well as double surnames.
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)


# The long_words function returns all words that are at least 7 
# characters. Fill in the regular expression to complete this function.
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []


# Add to the regular expression used in the extract_pid function, 
# to return the uppercase message in parenthesis, after the process id.
def extract_pid(log_line):
    regex = r"\[(\d+)\]:\s+([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2].upper())

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


#Replace the domain name
#!/usr/bin/env python3
#import re
#import csv
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
  csv_file_location = '<csv_file_location>'
  report_file = '<path_to_home_directory>' + '/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()
main()