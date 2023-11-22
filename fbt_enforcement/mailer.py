from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image
from reportlab.lib.units import inch


def create_speeding_ticket_pdf(car_data):
    # Content
    file_name = 'traffic_citation.pdf'
    document_title = 'Traffic Citation'
    title = 'Notice of Speed Violation'
    border_line = ['_______________________________________________________']

    citation_details = [
        f'Location: {car_data["owner"]["address"]}',
        # f'Date: {car_data["date"]}',  # Add the appropriate date field from your data
        # f'Time: {car_data["time"]}',  # Add the appropriate time field from your data
        # f'Sign Speed: {car_data["sign_speed"]} MPH',
        f'Vehicle Speed: {car_data["miles_per_hour"]} MPH',
        f'Plate Number: {car_data["plate_number"]}',
        f'Vehicle Make: {car_data["vehicle"]["make"]}'
    ]
    citation_body = [
        '',  # Empty string for a line break
        'Your vehicle was photographed speeding, '
        'in violation of 7-15 and 8-1-2-6, Eugene Ordinances, '
        'and OSL 1972 66-7-104 of the Oregon State Motor Vehicle Code',
        '',  # Empty string for a line break
        'As the vehicle\'s registered owner, you are liable for the violation. '
        'The civil penalty is $100.00 (payment instructions below). '
        'Payment is deemed an admission and waiver of your right to appeal. '
        'Failure to pay may result in this case being forwarded to a collection company.',
        '',  # Empty string for a line break
        'PAYMENT OF THE PENALTY AMOUNT FOR THE VIOLATION WILL NOT RESULT IN '
        'POINTS AND CANNOT BE USED TO INCREASE YOUR INSURANCE RATES.',
        '',  # Empty string for a line break
        'City of Eugene Officer\'s Certificate',
        'Based on personal inspection of vehicle images showing '
        'violation of 7-15 and 8-1-2-6, Eugene Ordinances, '
        'and OSL 1972 66-7-104 of the Oregon State Motor Vehicle Code',
        '',  # Empty string for a line break
    ]
    officer_signature = [
        'Sworn to or affirmed by:',
        '________________________________',
        'Signature of Officer       Date'
    ]

    # Create the PDF with the desired pagesize
    doc = SimpleDocTemplate(file_name, pagesize=letter)

    # Create a single Frame that spans the entire page width with margins on both sides
    frame = Frame(inch, inch, doc.width - 2 * inch, doc.height - 2 * inch, id='normalFrame')

    # Create the PageTemplate using the single frame
    page = PageTemplate(id='main', frames=frame)
    doc.addPageTemplates(page)

    # Add the PageTemplate to the document
    doc.addPageTemplates([page])

    # Create story elements for the left side (text)
    story = []
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH1 = styles['Heading1']
    # styleH3 = styles['ParagraphStyle']
    # styleN.alignment = 1  # 0=left, 1=center, 2=right
    # styleH1.alignment = 1
    # styleH3.alignment = 2
    styleP = ParagraphStyle(
        'Paragraph',
        # parent=styleN,
        fontName='Helvetica-Bold',
        fontSize=10,
        alignment=0  # Align to the left
    )
    # Add image path

    image_path = r'C:\Users\micha\OneDrive\Desktop\Dev\fbt-enforcement\fbt_enforcement\Eugene_Seal.jpg'
    # Add the image to the pdf
    story.append(Image(image_path, width=1 * inch, height=1 * inch))
    # story.append(Spacer(1, 12))  # Added space for separation
    # Adding lines to separate sections

    for line in [title]:
        p = Paragraph(line, styleH1)
        story.append(p)

    for line in border_line:
        p = Paragraph(line, styleN)
        story.append(p)

    for line in citation_details:
        p = Paragraph(line, styleP)
        story.append(p)

    for line in citation_body:
        p = Paragraph(line, styleN)
        story.append(p)
        story.append(Spacer(1, 6))

    for line in officer_signature:
        p = Paragraph(line, styleN)
        story.append(p)
        story.append(Spacer(1, 12))

    # Build the PDF with the story
    doc.build(story)
    print(f"Traffic citation PDF created: {file_name}")
