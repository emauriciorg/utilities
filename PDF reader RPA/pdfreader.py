import PyPDF2
# pdf file object

# you can find find the pdf file with complete code in  below

def get_tex (pdf_file_name):
 pdfFileObj = open(pdf_file_name, 'rb')
 # pdf reader object
 pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 # number of pages in pdf
 #print(pdfReader.numPages)
 # a page object
 pageObj = pdfReader.getPage(0)

 text = pageObj.extractText();
 #print(pageObj.extractText())
 return text;

def get_name(stream):
 name_index= text.find("Para: ");
 name_entry= text[name_index:name_index+25];
 name = name_entry.replace("Para: ",'')
 return name

def get_name_old(stream):
 name_index= stream.find("Nombre: ");
 name_entry= stream[name_index:name_index+25];
 name = name_entry.replace("Nombre: ",'')
 return name

pdf_name = "foo";

def get_phone(stream):
 x= stream.find("Teléfono");
 phone_entry= text[x:x+25];
 total_digits=sum(c.isdigit() for c in phone_entry);
 phone_entry_list = phone_entry.split();
 phone= phone_entry_list[1][0:10];
 return phone;


def get_phone_old(stream):
 name_index= stream.find("Nombre: ");
 sub_stream= stream[name_index:name_index+100];
 #print(sub_stream);
 x= sub_stream.find("Teléfono");
 phone_entry= sub_stream[x:x+25];
 total_digits=sum(c.isdigit() for c in phone_entry);
 phone_entry_list = phone_entry.split();
 #print(phone_entry_list);
 phone= phone_entry_list[1][0:10];
 #phone ="333"
 return phone;


import os
files  = os.listdir("pdfs/");
#print(files);

contacts = [["none","00000000000"]];

for x in files :
 text = get_tex ("pdfs/"+x);
 name = get_name_old(text);
 phone= get_phone_old(text);
 print(str(x),',',name ,',', phone);
 contacts.append([name,phone]);

print ("contacts ******************")
#print(contacts);
####
