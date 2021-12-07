# impor os
# def power(base, exp):
#     assert exp>0 and int(exp)==exp, 'postive integer'
#     if exp==0:
#         return 1
#     if exp==1:
#         return base
# #     return base*power(base, exp-1)
# # print(power(2,5))
# import os
# os.chdir('C:\\Users\\itnes\\Downloads')
# import docx
# g=docx.Document()

# indx=1
# for file in os.listdir():
#     if file.endswith('.docx'):
#         g.add_heading('Assignment {indx}',0)
#         g=docx.Document(file)
#         for i in g.paragraphs:
#             g.add_paragraph(i.text)
#             g.save('All_Assignment.docx')
#             indx+=1
import logging
logging.basicConfig(filename='test6.log',level=logging.INFO)
def func(*args):
    logging.info('this is my sum function')
    sum=0
    for i in args:
        logging.info(str(i))
        sum=sum+i
    return sum
        
f=open('test6.log','r')
print(f.read())