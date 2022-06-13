from icecream import ic


class Solution:
    def userInput(self):
        amt = input('Please enter your money amount.\n')
        items = input('Please enter item prices separated by spaces.\n')
        self.balanceCheck(amt, items)

    # Compare amt with list of
    def balanceCheck(self, amt: str, items: str, tax_rate=0.12):
        try:
            amt_int = float(amt)
        except:
            print('Invalid amount received: '+amt)
            amt_int = 0
        items_list = items.split(" ")
        # total amount for all items in list
        total = 0
        tax_rate += 1
        if len(items_list) > 0 and items_list[0] != '':
            for item in items_list:
                try:
                    item = float(item)
                    total += item * tax_rate
                except:
                    print('Invalid format received.\n')
                    continue
        else:
            total = 0

        diff = amt_int - total
        if diff < 0:
            print('$'+str(-round(diff, 2))+' short')
        else:
            print('Enough money. $'+str(round(diff, 2))+' remains.')
        return


test = Solution()
test.userInput()
# ic(test.balanceCheck('25', '10.50 7.60 1.26 3.49'))
# ic(test.balanceCheck('25', '10.50 7.60 1.26'))
