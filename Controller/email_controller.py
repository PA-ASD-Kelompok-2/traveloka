from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

def send_mail(email, receipt_id, flight_id, name, from_location, to_location, plane, ticket_code):

    day = datetime.datetime.now().strftime("%A")
    month = datetime.datetime.now().strftime("%B")
    year = datetime.datetime.now().strftime("%Y")
    clock = datetime.datetime.now().strftime("%H:%M")
    date = datetime.datetime.now().strftime("%d")

    message = Mail(
        from_email='fauzan@janjianaja.com',
        to_emails=email)

    message.dynamic_template_data = {
        'subject': 'TRAVELOKA: Receipt #' + receipt_id,
        'nomor_pesanan': receipt_id,
        'nomor_penerbangan': flight_id,
        'nama': name,
        'email': email,
        'asal_penerbangan': from_location,
        'tujuan_penerbangan': to_location,
        'pesawat': plane,
        'kode_tiket': ticket_code,
        'jam': clock,
        'hari': day,
        'tanggal': date,
        'bulan': month,
        'tahun': year,
    }
    message.template_id = 'd-df19ec40d75b465c8f4ca6e7f29a4e61'

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        code, body, headers = response.status_code, response.body, response.headers
        print(f"Response code: {code}")
        print(f"Response headers: {headers}")
        print(f"Response body: {body}")
        print("Dynamic Messages Sent!")
    except Exception as e:
        print("Error: {0}".format(e))

