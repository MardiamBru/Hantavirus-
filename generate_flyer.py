#!/usr/bin/env python3
"""
Script para gerar folheto PDF sobre Hantavírus com QR Code
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import qrcode
from io import BytesIO

# Cores do projeto
COLOR_RED = HexColor("#d92d2d")
COLOR_DARK = HexColor("#1b1b1b")
COLOR_BLUE = HexColor("#3d6fb2")
COLOR_BG = HexColor("#f5f5f5")

# Dimensões
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 15 * mm
QR_SIZE = 50 * mm

def create_qr_code(data, filename="/tmp/qrcode_temp.png"):
    """Gera QR Code para uma URL e salva em arquivo"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename

def draw_box_with_icon(c, x, y, width, height, title, icon, content, is_blue=False):
    """Desenha uma caixa com título e ícone"""
    # Fundo branco com borda
    c.setLineWidth(2)
    c.setStrokeColor(COLOR_DARK)
    c.setFillColor(white)
    c.roundRect(x, y, width, height, radius=6, stroke=1, fill=1)
    
    # Ícone (círculo)
    icon_x = x + 8
    icon_y = y + height - 14
    c.setLineWidth(2)
    c.setStrokeColor(COLOR_DARK)
    c.setFillColor(COLOR_BLUE if is_blue else COLOR_RED)
    c.circle(icon_x + 7, icon_y, 7, stroke=1, fill=1)
    
    # Ícone texto
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(white)
    c.drawCentredString(icon_x + 7, icon_y - 2, icon)
    
    # Título
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(COLOR_RED)
    c.drawString(x + 20, y + height - 12, title.upper())
    
    # Linha divisória
    c.setLineWidth(1.5)
    c.setStrokeColor(COLOR_DARK)
    c.line(x + 8, y + height - 16, x + width - 8, y + height - 16)
    
    # Conteúdo
    c.setFont("Helvetica", 8)
    c.setFillColor(COLOR_DARK)
    
    text_y = y + height - 22
    for line in content:
        if line.startswith("•"):
            c.drawString(x + 10, text_y, line)
        else:
            c.drawString(x + 10, text_y, line)
        text_y -= 8

def create_flyer_pdf(output_filename="flyer.pdf"):
    """Cria o folheto em PDF"""
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4
    
    # Background pattern (retângulos com transparência simulada)
    c.setFillColor(HexColor("#f0f0f0"))
    
    # Cabeçalho
    y = height - MARGIN
    
    # Logo (círculo com +)
    c.setLineWidth(2)
    c.setStrokeColor(COLOR_RED)
    c.setFillColor(white)
    c.circle(width/2, y - 15, 12, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_RED)
    c.drawCentredString(width/2, y - 18, "✚")
    
    # Título
    y -= 35
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(COLOR_DARK)
    c.drawCentredString(width/2, y, "GUIA INFORMATIVO")
    y -= 20
    c.drawCentredString(width/2, y, "HANTAVÍRUS")
    
    # Subtítulo
    y -= 12
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#555555"))
    c.drawCentredString(width/2, y, "EDUCAÇÃO EM SAÚDE • FATEC BAURU")
    
    # Linha divisória
    y -= 8
    c.setLineWidth(2)
    c.setStrokeColor(COLOR_RED)
    c.line(MARGIN, y, width - MARGIN, y)
    
    # Grid de caixas (2x2)
    y -= 15
    box_width = (width - 3 * MARGIN) / 2
    box_height = 70
    
    # Linha 1
    draw_box_with_icon(
        c, MARGIN, y - box_height, box_width, box_height,
        "O Que É", "i",
        [
            "Doença viral aguda",
            "transmitida por roedores",
            "Taxa de letalidade: 30-50%",
            "Incubação: 7-14 dias"
        ],
        is_blue=True
    )
    
    draw_box_with_icon(
        c, MARGIN + box_width + MARGIN, y - box_height, box_width, box_height,
        "Transmissão", "↔",
        [
            "• Inalação de aerossóis",
            "• Contato com urina/fezes",
            "• Materiais contaminados",
            "⚠️ NÃO se transmite entre pessoas"
        ]
    )
    
    y -= box_height + MARGIN
    
    # Linha 2
    draw_box_with_icon(
        c, MARGIN, y - box_height, box_width, box_height,
        "Sintomas", "✚",
        [
            "• Febre alta (39-40°C)",
            "• Dor muscular",
            "• Dor de cabeça intensa",
            "• Tosse e falta de ar"
        ]
    )
    
    draw_box_with_icon(
        c, MARGIN + box_width + MARGIN, y - box_height, box_width, box_height,
        "Prevenção", "🛡",
        [
            "• Manter ambiente limpo",
            "• Usar máscara PFF2",
            "• Usar luvas e proteção",
            "• Controle de roedores"
        ]
    )
    
    y -= box_height + 15
    
    # Seção de Alerta com QR Code
    alert_height = 50
    c.setLineWidth(2)
    c.setStrokeColor(COLOR_DARK)
    c.setFillColor(COLOR_DARK)
    c.roundRect(MARGIN, y - alert_height, width - 2*MARGIN, alert_height, radius=4, stroke=1, fill=1)
    
    # Texto do alerta
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(white)
    alert_text = [
        "ATENÇÃO:",
        "SE APRESENTAR SINTOMAS",
        "PROCURE IMEDIATAMENTE",
        "UMA UNIDADE DE SAÚDE!"
    ]
    alert_y = y - 12
    for line in alert_text:
        c.drawString(MARGIN + 10, alert_y, line)
        alert_y -= 12
    
    # QR Code
    qr_img = create_qr_code("https://mardiambru.github.io/Hantavirus-/")
    qr_x = width - MARGIN - 45
    qr_y = y - alert_height + 5
    c.drawImage(qr_img, qr_x, qr_y, width=40*mm, height=40*mm)
    
    # Texto do QR
    c.setFont("Helvetica-Bold", 7)
    c.setFillColor(white)
    c.drawCentredString(qr_x + 20, qr_y - 5, "ESCANEIE")
    c.drawCentredString(qr_x + 20, qr_y - 10, "PARA SABER MAIS")
    
    y -= alert_height + 10
    
    # Créditos
    c.setFont("Helvetica", 6)
    c.setFillColor(HexColor("#666666"))
    credits = [
        "Elaborado por Giovana Amancio, Milena Gasparotto e Marcelo Dias",
        "Curso Sistemas Biomédicos • FATEC Bauru • 2026"
    ]
    credit_y = y
    for line in credits:
        c.drawCentredString(width/2, credit_y, line)
        credit_y -= 8
    
    # Salva o PDF
    c.save()
    print(f"✓ Folheto criado com sucesso: {output_filename}")

if __name__ == "__main__":
    create_flyer_pdf("/workspaces/Hantavirus-/flyer.pdf")
