import os

# أداة ريان لكشف ملفات التجسس المخفية
def spy_file_detector():
    suspicious_files = ["secret_data.txt", "log.txt", "trace.py"]
    found = False
    
    print("🔍 جاري فحص النظام عن ملفات مشبوهة...")
    
    for file in suspicious_files:
        if os.path.exists(file):
            print(f"⚠️ تحذير: تم العثور على ملف مشبوه: {file}")
            found = True
            
    if not found:
        print("✅ النظام نظيف، لا توجد ملفات تجسس معروفة.")

spy_file_detector()