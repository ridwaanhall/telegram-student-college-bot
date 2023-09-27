import os

import requests

token = os.environ['TELEGRAM_BOT_TOKEN']


class ANSWERE:

    @staticmethod
    def generate_answer(message):
        if not message:
            return {"error": "Empty message."}

        if not message.startswith("/"):
            url = f'https://api-student-colege.ridwaanhall.repl.co/{message}'
            response = requests.get(url)

            if response.status_code == 200:
                mahasiswa_list = response.json().get("mahasiswa", [])
                result = ""

                for _i, mahasiswa in enumerate(mahasiswa_list, start=1):
                    student_name = mahasiswa.get("student name", "N/A")
                    nim = mahasiswa.get("nim", "N/A")
                    mahasiswa.get("study program", "N/A")
                    college_name = mahasiswa.get("college name", "N/A")
                    detail = mahasiswa.get("detail", "N/A")

                    result += f"Name: {student_name}\nNIM: {nim}\nCollege: {college_name}\nDetail: {detail}\n\n"

                return result.strip()  # Remove trailing newline
            else:
                return "Data not Found!"
        elif message.startswith("/"):
            url = f'https://api-student-colege.ridwaanhall.repl.co/detail_student/{message[1:]}'
            response = requests.get(url)
        
            if response.status_code == 200:
                data = response.json()
                dataumum = data.get("dataumum", {})
                datastatuskuliah = data.get("datastatuskuliah", [])
                datastudi = data.get("datastudi", [])
        
                result = f" ----------- DATA UMUM -----------\n" \
                         f"Name: {dataumum.get('nm_pd', 'N/A')}\n" \
                         f"Gender: {dataumum.get('jk', 'N/A')}\n" \
                         f"nipd: {dataumum.get('nipd', 'N/A')}\n" \
                         f"Degree: {dataumum.get('namajenjang', 'N/A')}\n" \
                         f"Study Program: {dataumum.get('namaprodi', 'N/A')}\n" \
                         f"College Name: {dataumum.get('namapt', 'N/A')}\n" \
                         f"Sign Up Type: {dataumum.get('nm_jns_daftar', 'N/A')}\n" \
                         f"reg_pd: {dataumum.get('reg_pd', 'N/A')}\n" \
                         f"From College Name: {dataumum.get('nm_pt_asal', 'N/A')}\n" \
                         f"From SP Name: {dataumum.get('nm_prodi_asal', 'N/A')}\n" \
                         f"Desc Out: {dataumum.get('ket_keluar', 'N/A')}\n" \
                         f"Date Out: {dataumum.get('tgl_keluar', 'N/A')}\n" \
                         f"Serial Number Ijazah: {dataumum.get('no_seri_ijazah', 'N/A')}\n" \
                         f"Prof: {dataumum.get('sert_prof', 'N/A')}\n" \
                         f"Start: {dataumum.get('mulai_smt', 'N/A')}\n"
        
                if datastatuskuliah:
                    result += "\n ------- DATA STATUS KULIAH: -------\n"
                    for status in datastatuskuliah:
                        result += f"\nID SMT : {status['id_smt']}\n" \
                                  f"SKS    : {status['sks_smt']}\n" \
                                  f"Status : {status['nm_stat_mhs']}\n"
        
                if datastudi:
                    result += "\n -------- DATA STUDY: --------\n"
                    for study in datastudi:
                        result += f"\nCode MK: {study['kode_mk']}\n" \
                                  f"Name MK: {study['nm_mk']}\n" \
                                  f"SKS: {study['sks_mk']}\n" \
                                  f"ID SMT: {study['id_smt']}\n" \
                                  f"Grade: {study['nilai_huruf']}\n"
        
                return result
        
            else:
                return "Data not Found!"



        else:
            return {"error": "Invalid message format."}


class MESSAGE:

    @staticmethod
    def message_parser(message):
        chat_id = message['message']['chat']['id']
        if 'text' in message['message']:
            text = message['message']['text']
            print("Chat ID: ", chat_id)
            print("Message: ", text)
            return chat_id, text
        else:
            print("Chat ID: ", chat_id)
            print("Message does not contain text.")
            return chat_id, []

    @staticmethod
    def send_message_telegram(chat_id, text):
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        text = f'```{text}```'
        payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
        response = requests.post(url, json=payload)
        return response
