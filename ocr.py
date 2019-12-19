from pdf2image import convert_from_path
from PIL import Image
from threading import Thread
import sys
import shutil
import pytesseract
import os

if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread

print()
print("Select you language:")
languages = ["0. Sanskrit - san","1. Hindi - hin","2. Gujrati - guj","3. Marathi - mar","4. Punjabi - pan","5. Tamil - tam","6. Kannada - kan","7. Telugu - tel","8. Malayalam - mal","9. Bengali - ben","10 Oriya - ori"]
for langu in languages:
	print(langu)
print()
hehe = int(input("Enter number corresponding to the desired language: "))
while ((hehe>10) and (hehe<0)):
	print("WRONG INPUT! PLEASE ENTER AGAIN")
	hehe = int(input("Enter number corresponding to the desired language: "))
print()
language = languages[hehe][len(languages[hehe])-3:]
print("You have selected ( "+languages[hehe]+" ) language.")

print("\n----------------------------------------------------------------------------------------\n")

list_of_dir = next(os.walk(os.getcwd()))[1]
print(list_of_dir)

print("\n----------------------------------------------------------------------------------------\n")

if ("pdf_images" in list_of_dir):
	print('ALREADY EXISTS ..!!')
	input("Press any key to continue.")
	print("\n----------------------------------------------------------------------------------------\n")
else:
	os.mkdir("pdf_images")

count_pages=0
def create_images_from_pdf(path_to_pdf,dpii):
	global list_of_dir
	global count_pages
	print("Converting pdf pages to jpeg images...............")
	pages = convert_from_path(path_to_pdf,dpii)
	for page in pages:
		page.save('pdf_images/out'+str(count_pages)+'.jpg', 'JPEG')
		count_pages += 1
	print()
	print("Task Done.")
	print("\n----------------------------------------------------------------------------------------\n")

my_pdf_path = "8th-kannada-socialscience-2.pdf"

create_images_from_pdf(my_pdf_path,200)

def ocr(language):
	global list_of_dir
	global count_pages

	if ("text_files" in list_of_dir):
	    print('ALREADY EXISTS ..!!')
	    input("Press any key to continue.")
	    print("\n----------------------------------------------------------------------------------------\n")
	else:
		os.mkdir("text_files")

	def ocr_core(path_to_images,n,language,t):
		img = Image.open(path_to_images+'/out'+str(n)+'.jpg')
		img.load()
		text = pytesseract.image_to_string(img, lang=language)
		f  = open("text_files/page"+str(n)+".txt",'w',encoding='utf-8')
		f.write(text)
		f.close()
		print("Thread "+str(t)+" ---> Text file for image "+str(n)+" saved.")

	def ocr_thread1(a1,b1):
		for thread1_iter in range(a1,b1):
			print("Thread 1---> Running OCR in image "+str(thread1_iter))
			print()
			ocr_core("pdf_images",thread1_iter,language,1)
		print("\n--------------------------------------------------------------------")
		print("\nThread 1 task done.\n")
		print("\n--------------------------------------------------------------------")

	def ocr_thread2(a2,b2):
		for thread2_iter in range(a2,b2):
			print("Thread 2---> Running OCR in image "+str(thread2_iter))
			print()
			ocr_core("pdf_images",thread2_iter,language,2)
		print("\n--------------------------------------------------------------------")
		print("\nThread 2 task done.\n")
		print("\n--------------------------------------------------------------------")

	def ocr_thread3(a3,b3):
		for thread2_iter in range(a3,b3):
			print("Thread 3---> Running OCR in image "+str(thread2_iter))
			print()
			ocr_core("pdf_images",thread2_iter,language,3)
		print("\n--------------------------------------------------------------------")
		print("\nThread 3 task done.\n")
		print("\n--------------------------------------------------------------------")

	def ocr_thread4(a4,b4):
		for thread2_iter in range(a4,b4):
			print("Thread 4---> Running OCR in image "+str(thread2_iter))
			print()
			ocr_core("pdf_images",thread2_iter,language,4)
		print("\n--------------------------------------------------------------------")
		print("\nThread 4 task done.\n")
		print("\n--------------------------------------------------------------------")

	one_partition_size = count_pages // 4
	ocr_thread1_object = Thread(target = ocr_thread1, args=[0,one_partition_size], daemon = False)
	ocr_thread2_object = Thread(target = ocr_thread2, args = [one_partition_size,2*one_partition_size], daemon = False)
	ocr_thread3_object = Thread(target = ocr_thread3, args = [2*one_partition_size,3*one_partition_size], daemon = False)
	ocr_thread4_object = Thread(target = ocr_thread4, args = [3*one_partition_size,count_pages], daemon = False)

	print("Starting OCR on total of 4 threads.")
	print()
	ocr_thread1_object.start()
	ocr_thread2_object.start()
	ocr_thread3_object.start()
	ocr_thread4_object.start()

	ocr_thread1_object.join()
	ocr_thread2_object.join()
	ocr_thread3_object.join()
	ocr_thread4_object.join()

ocr(language)

shutil.rmtree("pdf_images")
print("\n\n")
print("******************************************************************************************************")
print("OCR PROGRAM COMPLETED. Text file saved at /text_files/ .")
print("******************************************************************************************************")
