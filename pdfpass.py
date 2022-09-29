import PyPDF2
import argparse


class PDFPass:
    
    
    def main():
        args = argparse.ArgumentParser()
  
        args.add_argument("-f", "--file", help = "File input", required = True)
        args.add_argument("-o", "--output", help = "File to output", required = True)
        args.add_argument("-p", "--password", help = "Password to protect file", required = True)
        
        argument = args.parse_args()
        pdf_input = open(argument.file,'rb')

        inputpdf = PyPDF2.PdfFileReader(pdf_input)
        pages_no = inputpdf.numPages
        output = PyPDF2.PdfFileWriter()

        for i in range(pages_no):
            inputpdf = PyPDF2.PdfFileReader(pdf_input)
            
            output.addPage(inputpdf.getPage(i))
            output.encrypt(argument.password)

            with open(argument.output, "wb") as outputStream:
                output.write(outputStream)

        pdf_input.close()
        
        
PDFPass.main()