import csv

def run():

  def read_csv(path):
    with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      header = next(reader)
      data = []
      for row in reader:
        iterable = zip(header, row)
        dicc = dict(iterable)
        data.append(dicc)
      return data

  def country(country):
    countries = []
    for item in country:
      countries.append(item['Country/Territory'])
    return countries

  if __name__ == "__main__":
    final_data = read_csv('data.csv')
    country(final_data)


if __name__ == '__main__':
  run()