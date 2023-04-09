from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
import random
import os

load_dotenv()

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = os.getenv('SENDINBLUE_API_KEY')


def send_email(email, id_flight, name, asal, tujuan, pesawat, tanggal, waktu_keberangkatan, waktu_kedatangan, harga):
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    receipt = str(random.randint(100000, 999999))
    ticket_code = str(random.randint(100000, 999999))
    to = [{"email": email, "name": name}]
    params = {
        "RECEIPT":receipt,
        "ID_FLIGHT": id_flight,
        "NAMA": name,
        "ASAL": asal,
        "TUJUAN": tujuan,
        "NAMA_PESAWAT": pesawat,
        "TANGGAL": tanggal,
        "WAKTU_KEBERANGKATAN": waktu_keberangkatan,
        "WAKTU_KEDATANGAN": waktu_kedatangan,
        "KODE_TIKET": ticket_code,
        "HARGA": harga
    }
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, params=params, template_id=1)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)

