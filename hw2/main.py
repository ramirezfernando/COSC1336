'''
Fernando Ramirez 2030198  
COSC 1336
Homework #2
'''

file_name = input("Please enter the data file name: ")
while file_name != "":
  try:
    file = open(file_name)
    lines = file.readlines()
    file.close()
    data = []
    for line in lines[1:]:
      values = line.split(',')
      # TUPLE : date/ high price/ low price
      # we appended the tuple to data list
      data.append( (values[0], float(values[2]), float(values[3])) )

    # HIGHEST PRICE IN TUPLE [1]
    def find_highest_price(file_name):
      highest_price = 0
      for tuple in data:
        if tuple[1] > highest_price:
          sell_date = tuple[0]
          highest_price = tuple[1]
      return (sell_date, highest_price)

    # LOWEST PRICE IN TUPLE [2]
    def find_lowest_price(file_name):
      lowest_price = data[0][2] #522.665039
      for tuple in data:
        if tuple[2] < lowest_price:
          buy_date = tuple[0]
          lowest_price = tuple[2]
      return (buy_date, lowest_price)

    buy_date = find_lowest_price(file_name)[0]
    buy_price = find_lowest_price(file_name)[1]

    sell_date = find_highest_price(file_name)[0]
    sell_price = find_highest_price(file_name)[1]

    largest_profit = 0
    best_sell_index = 0

    for index in range(1,len(data)):
      profit = sell_price - buy_price
      if profit > largest_profit:
        largest_profit = profit
        best_sell_date = index

    # OUTPUT
    if file_name != "":
      print()
      print("Reading data ...",'\n',
      "****************************************",'\n',
      "The maximum profit is ${:.2f} per share".format(largest_profit),'\n',
      "Buy on {} at a price of ${:.2f}".format(buy_date, buy_price),'\n',
      "Sell on {} at a price of ${:.2f}".format(sell_date, sell_price),'\n'
      "Change in value ratio: {:.3f}".format(sell_price / buy_price),'\n',
      "****************************************")
      file_name = ""
    
    file_name = input("Please enter the data file name: ")
  


  except FileNotFoundError:
    print("Error Reading data ..." ,'\n' ,"The file does not exist. Please check the name and try again.")
    file_name = input("Please enter the data file name: ")
  except IsADirectoryError:
    print("Error Reading data ..." ,'\n' ,"The file does not exist. Please check the name and try again.")
    file_name = input("Please enter the data file name: ")

  

