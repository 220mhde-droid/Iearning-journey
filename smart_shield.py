import os

# أداة ريان لحماية النظام من الأوامر الخطرة
def smart_shield(code_to_check):
    danger_words = ["socket.connect", "requests.post", "os.remove", "eval(base64"]
    is_safe = True
    
    print("🛡️ جاري فحص نوايا الكود...")
    
    for word in danger_words:
        if word in code_to_check:
            print(f"🛑 خطر! تم اكتشاف محاولة: {word}")
            is_safe = False
            break
            
    if is_safe:
        print("✅ الكود لا يحتوي على أوامر اختراق مباشرة.")
    else:
        print("⚠️ نصيحة ريان: لا تقم بتشغيل هذا الكود أبداً!")

# تجربة الدرع على نص مشبوه
test_code = "socket.connect(('192.168.1.1', 80))"
smart_shield(test_code)