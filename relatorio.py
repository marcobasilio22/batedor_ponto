from reportlab.pdfgen import canvas
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.get_database("Ponto")
collection = db.get_collection("Registros")

def r_pdf():
    docs = collection.find({}, {"_id": 0})

    pdf = canvas.Canvas("relatorio.pdf")

    y = 700
    for doc in docs:
        for key, value in doc.items():
            pdf.drawString(100, y, f"{key}: {value}")
            y -= 20
        y -= 20

    pdf.save()

