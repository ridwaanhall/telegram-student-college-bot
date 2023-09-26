import os, requests

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

                for i, mahasiswa in enumerate(mahasiswa_list, start=1):
                    student_name = mahasiswa.get("student name", "N/A")
                    nim = mahasiswa.get("nim", "N/A")
                    study_program = mahasiswa.get("study program", "N/A")
                    college_name = mahasiswa.get("college name", "N/A")
                    detail = mahasiswa.get("detail", "N/A")

                    result += f"Name: {student_name}\nNIM: {nim}\nCollege: {college_name}\nDetail: {detail}\n\n"

                return result.strip()  # Remove trailing newline
            else:
                return {"error": "Unable to retrieve data from the API."}
        elif message.startswith("/"):
            url = f'https://api-student-colege.ridwaanhall.repl.co/detail_student/{message[1:]}'
            response = requests.get(url)
        
            if response.status_code == 200:
                data = response.json()
                dataumum = data.get("dataumum", {})  # Get the dataumum key, or empty dictionary if it doesn't exist
                return dataumum
            else:
                return {"error": "Unable to retrieve data from the API."}
        

        else:
            return {"error": "Invalid message format."}



class MESSAGE:
    @staticmethod
    def message_parser(message):
        chat_id = message['message']['chat']['id']
        text = message['message']['text']
        print("Chat ID: ", chat_id)
        print("Message: ", text)
        return chat_id, text

    @staticmethod
    def send_message_telegram(chat_id, text):
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': text
        }
        response = requests.post(url, json=payload)
        return response
