import os
from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('logo.png', 10, 8, 33)  # Agar logo bo'lsa
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'CRM Cosmos EDU - Technical Specification', 0, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def create_crm_pdf():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Set font
    pdf.set_font('Arial', '', 12)
    
    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'CRM Cosmos EDU - Texnik Topshiriq (Technical Specification)', 0, 1)
    pdf.ln(10)
    
    # Loyiha tavsifi
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '1. Loyiha Tavsifi', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 'CRM Cosmos EDU - bu onlayn ta\'lim markazlarini to\'liq boshqarish uchun mo\'ljallangan veb-platforma. Sistema 5 turdagi foydalanuvchilar uchun imkoniyatlarni taqdim etadi.')
    pdf.ln(5)
    
    # Platforma va texnologiyalar
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '2. Platforma va Texnologiyalar', 0, 1)
    pdf.set_font('Arial', '', 12)
    platforms = [
        'Platforma: Responsive Web (Desktop + Mobile)',
        'Frontend: React (Single Page Application)',
        'Backend: Django REST API',
        'Database: PostgreSQL / MySQL',
        'Authentication: JWT + OTP',
        'Real-time: WebSocket / Webhook bildirishnomalar uchun'
    ]
    for item in platforms:
        pdf.cell(0, 10, '• ' + item, 0, 1)
    pdf.ln(5)
    
    # Continue adding all sections from the TZ...
    # [Qolgan kontentni shu tarzda davom ettiramiz]
    
    pdf.output('CRM_Cosmos_EDU_TZ.pdf')
    print("PDF fayli yaratildi: CRM_Cosmos_EDU_TZ.pdf")

if __name__ == '__main__':
    create_crm_pdf()