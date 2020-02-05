 
from time import ctime

def get_number_input(prompt):
    value = None

    while type (value) != float:
        try:
            value = float(input(prompt))
            return value
        except KeyboardInterrupt:
            exit()

        except ValueError as e:
            print("Invalid input!")
            print(ctime(), e, file=ERROR_FILE)

def main():
   while True:
       client_name = input('what is the customer\'s name: ')
       if not client_name:
           break

       while True:
           product_name = input('what is the product name?: ')
           if not product_name:
               break

           product_qty = get_number_input(f'how many {product_name} is purchased?: ')
           product_price = get_number_input(f'how much is {product_name}: ')

           total = product_price * product_qty
           print(total)
           



if __name__ == '__main__':
    #superglobals
    ERROR_FILE = open('error_log.txt', 'a')

# the main code
    main()
    ERROR_FILE.close()