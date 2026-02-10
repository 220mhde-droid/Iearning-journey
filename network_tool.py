# أداة ريان لفحص اتصال الشبكة
import socket

def check_connection(target_url):
    try:
        host = socket.gethostbyname(target_url)
        return f"✅ الهدف {target_url} متصل بالإنترنت. العنوان الرقمي هو: {host}"
    except:
        return f"❌ تعذر الاتصال بالهدف: {target_url}"

target = "google.com"
print(check_connection(target))