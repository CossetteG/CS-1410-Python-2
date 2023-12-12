# imports module
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from desserts import Order, Cookie, Candy, IceCream, Sundae

def make_receipt(data:list[list[str,int,float]], out_file_name:str):
	"""makes a pdf receipt of our order"""

	# creating a Base Document Template of page size A4
	pdf = SimpleDocTemplate( out_file_name , pagesize = A4 )

	# standard stylesheet defined within reportlab itself
	styles = getSampleStyleSheet()

	# fetching the style of Top level heading (Heading1)
	title_style = styles[ "Heading1" ]

	# 0: left, 1: center, 2: right
	title_style.alignment = 1

	# creating the paragraph with
	# the heading text and passing the styles of it
	title = Paragraph( "Dessert Receipt" , title_style )

	# creates a Table Style object and in it,
	# defines the styles row wise
	# the tuples which look like coordinates
	# are nothing but rows and columns
	style = TableStyle(
		[
			( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
			( "GRID" , ( 0, 0 ), ( 5 , 15 ), 1 , colors.black ),
			( "BACKGROUND" , ( 0, 0 ), ( 4, 0 ), colors.gray ),
			( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
			( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
			( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
		]
	)

	# creates a table object and passes the style to it
	table = Table(data , style = style )

	# final step which builds the
	# actual pdf putting together all the elements
	pdf.build([ title , table ])

#not called
'''
def main():
	dessert_order = _main()

	data = dessert_order.receipt_input()
	order_length = str(len(dessert_order))
	
	totals = data.pop()
	#conv_data = [[str(name), "$"+str(cost), "$"+str(tax)],  for [name, cost, tax] in data]
	conv_data = []
	for name, cost, tax in data:
		print_name = str(name)
		print_cost = "$"+str(cost)
		print_tax = "$"+str(tax)
		conv_data.append([print_name, "", print_cost, print_tax])
	conv_totals = [ "$"+str(price) for price in totals]

	# data which we are going to display as tables
	DATA = [
		[ "Name", "Quantity", "Unit Price" "Item Cost", "Tax" ],] + conv_data + [
			"-"*56, "", ""] +[
		[ "Order Subtotals", "", conv_totals[0], conv_totals[1]],
		[ "Total", "", "", conv_totals[2]],
		[ "Total items in the order", "", "", order_length]
	]
  

	make_receipt(DATA, "receipt.pdf")
'''

def make_data(order, name, count, id):
    """makes data that can be passed to make_receipt"""
    data = order.receipt_input()
    totals = data.pop()
    paytype = totals.pop()
    #conv_data = [[str(name), "$"+str(cost), "$"+str(tax)],  for [name, cost, tax] in data]
    # conv_data = []
    # for name, quantity, unit_price, cost, tax in data:
    #     print_name = str(name)
    #     print_cost = "$"+str(cost)
    #     print_tax = "$"+str(tax)
    #     conv_data.append([print_name, "", print_cost, print_tax])
    conv_totals = [ "$"+str(price) for price in totals] #subtotal, tax, total

    # data which we are going to display as tables
    DATA = [
        [ "Name", "Quantity", "Unit Price", "Item Cost", "Tax" ]] + data + [
         [ "", "", "-"*56, "", ""]] +[
      [ "Order Subtotals", "", "", conv_totals[0], conv_totals[1]],
      [ "Total", "",  "", "", conv_totals[2]],
      [ "Total items in the order", "", "", str(len(order))],
      ["", "", "-"*56, "", ""], 
      ["Paid with ", paytype, "", "", "" ], 
      ["Customer Name: " + name, "Customer ID: " + str(id), "Total Orders: " + str(count)]
      ]

    return DATA 