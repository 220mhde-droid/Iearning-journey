# أداة ريان لفحص قوة كلمة المرور
def check_password(password):
    if len(password) < 8:
        return "⚠️ ضعيفة: يجب أن تكون 8 رموز على الأقل."
    else:
        return "✅ قوية: كلمة المرور تلبي معايير الأمان الأساسية."

pwd = input("أدخل كلمة مرور للتجربة: ")
print(check_password(pwd))