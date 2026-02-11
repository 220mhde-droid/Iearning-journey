import os
from datetime import datetime

# نسخة ريان المطورة: الدرع مع سجل التعقب (V2)
def smart_shield_v2(code_to_check):
    # وضعنا "os." ككلمة خطر أساسية بناءً على تحليلك الذكي
    danger_words = ["os.", "socket.connect", "requests.post", "eval(base64"]
    is_safe = True
    
    print("🛡️ جاري فحص نوايا الكود...")
    
    for word in danger_words:
        if word in code_to_check:
            is_safe = False
            # توثيق محاولة الاختراق في ملف سري للأدلة
            with open("security_log.txt", "a") as log:
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log.write(f"[{time_now}] محاولة اختراق مكتشفة باستخدام: {word}\n")
            break
            
    if is_safe:
        print("✅ الكود نظيف ولا يحتوي على أوامر اختراق مباشرة.")
    else:
        print("🛑 خطر! ريان، هذا الكود حاول العبث بجهازك وتم تسجيله.")

# مثال لتجربة الدرع (سيقوم بإنشاء ملف security_log.txt تلقائياً)
code_sample = "os.system('format C:')"
smart_shield_v2(code_sample)