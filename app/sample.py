from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Sample PDF for Assignment', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create a PDF object
pdf = PDF()
pdf.add_page()

# Add some chapters
pdf.chapter_title('Introduction')
pdf.chapter_body(
    "This is a sample PDF file created for testing purposes. It includes multiple pages of text "
    "to simulate a realistic document. The content is meant to be used for extracting and querying "
    "text using a FastAPI application."
)

pdf.chapter_title('Page 2')
pdf.chapter_body(
    "Here is some additional content to ensure that the PDF file has multiple pages. This text will "
    "be used to test the PDF text extraction and querying functionality. The PDF file should be long "
    "enough to test the chunking logic in the FastAPI application."
)

pdf.chapter_title('Page 3')
pdf.chapter_body(
    "Finally, this is the content for the third page. The document is designed to test various aspects "
    "of PDF handling, including text extraction, chunking, and question answering. The text content "
    "should be varied to provide comprehensive testing."
)

# Save the PDF
pdf_output_path = 'sample_assignment.pdf'
pdf.output(pdf_output_path)

print(f'Sample PDF generated: {pdf_output_path}')
