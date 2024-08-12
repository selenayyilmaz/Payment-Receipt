from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle



DATA = [["Date","Product Name","Installment","Price($)","Per Month($)"],
        ["12/08/2024","Computer",4,400,""],
        ["12/08/2024","Microsoft Xbox Series X + Diablo IV Bundle",4,572,""],
        ["12/08/2024","Marvel Legends Series Wolverine Action Figure",2,37,""],
        ["Sub Total","","",""],
        ["Discount (sub total>1000$)","","","200"],
        ["Total","","",""]
        ]

sub_total = 0

for product in range(1,(len(DATA)-3)):
    sub_total += DATA[product][3]
    price = int(DATA[product][3]) if isinstance(DATA[product][3], str) else DATA[product][3]
    installment = int(DATA[product][2]) if isinstance(DATA[product][2], str) else DATA[product][2]
    per_month = price / installment if installment != 0 else 0
    DATA[product][4] = per_month

DATA[-3][3] = sub_total


if sub_total > 1000 :
    DATA[-1][3] = sub_total - 200
else:
    DATA[-1][3] = sub_total


pdf = SimpleDocTemplate('paymentreceipt.pdf',pagesize= A4)

style = getSampleStyleSheet()

title_style = ParagraphStyle(
    name="Custom Title",
    fontName="Times-Roman",
    fontSize= 16,
    alignment= 1,
    spaceAfter= 10
)             # 0: left, 1: center, 2: right

title = Paragraph("Your Payment Receipt",title_style)

table = Table(DATA, style=[('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                        ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                        ('LINEBELOW',(0,-1),(-1,-1),2,colors.gray),
                        ('ALIGN',(1,1),(-1,-1),'RIGHT'),
                        ('BACKGROUND',(0,0),(-1,0),colors.yellowgreen),
                        ('BACKGROUND', (0, -3), (-1, -3), colors.yellowgreen),
                        ('BACKGROUND', (0, -2), (-1, -2), colors.yellowgreen),
                        ('BACKGROUND', (0, -1), (-1, -1), colors.whitesmoke),
                        ])


pdf.build([title,table])




