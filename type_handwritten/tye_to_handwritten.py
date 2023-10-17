import pywhatkit as pw

text=input("Enter the text you want to convert to Handwritten :\n")
pw.text_to_handwriting(text,"file.png")
print("Successfully done !!!")