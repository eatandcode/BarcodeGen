import barcode
from barcode.writer import ImageWriter
#from barcode.writer import ImageWriter

barcode_input = input("enter barcode")

ean = barcode.get('ean13', barcode_input, writer=ImageWriter())
ean.get_fullcode()
filename = ean.save("barcode4")

#ean = EAN('barcode', writer=ImageWriter())
#fullname = ean.save('barcode_image')


#code = generate('barcode') 


