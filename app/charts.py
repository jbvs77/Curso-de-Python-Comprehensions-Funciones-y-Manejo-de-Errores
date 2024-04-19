'''
import matplotlib.pyplot as plt 



def generate_bar_chart(lables,values):   
  fig, ax = plt.subplots()
  ax.bar(lables,values)
  plt.show()

def generate_pie_chart(lables,values):
  fig, ax = plt.subplots()
  ax.pie(values, lables)
  ax.axis('equal')
  plt.show()


if __name__ == "__main__":
  lables= ['Luis', 'Fernando', 'Gomez']
  values= [100, 200, 80]
  generate_pie_chart(lables,values)


'''

import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):   
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels= labels)
  ax.axis('equal')
  plt.show()


if __name__ == "__main__":
    labels = ['Luis', 'Fernando', 'Gomez']
    values = [100, 200, 80]
    generate_pie_chart(labels, values)