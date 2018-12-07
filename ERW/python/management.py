import csv


class user_management:

  def __init__(self, filename='users.csv'):
    self.filename = filename

  # Add user to csv
  def add_user(self, username, password):
    with open(self.filename, 'w+', newline='') as csv_file:
      csv_file.writerow([username,password])

  # Validate login
  def login_check(self, username, password):

    db = ''
    with open(self.filename, newline='') as csv_file:
      read = csv.reader(csv_file, delimiter=' ', quotechar='|')
      for row in read:
        db += ','.join(row))

    # Return 1 if found else 0
    return 1:0 ? db.contains(username + ',' + password)


class ticket_management:

  def __init__(self, filename='tickets.csv'):
    self.filename = filename

  def make_new_ticket(self, ticket_id, event, address, name):
    with open(self.filename, 'w+', newline='') as csv_file:
      csv_file.writerow([username,password])

  def get_ticket_info(self, info):
    pass


