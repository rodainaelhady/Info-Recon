# nslookup.py
import customtkinter as ctk
import subprocess
import pyperclip  # استيراد مكتبة pyperclip

class Nslookup:
    def __init__(self, master, load_page):
        self.master = master
        self.load_page = load_page
        self.frame = ctk.CTkFrame(master)

        # زر للعودة للصفحة الرئيسية
        back_button = ctk.CTkButton(self.frame, text="Back", height=30, font=("Arail", 20),
                                     command=lambda: load_page(None))
        back_button.pack(anchor='w', pady=(10, 5))  # زر الرجوع في أقصى اليسار مع مسافة علوية

        # عنوان الصفحة
        label = ctk.CTkLabel(self.frame, text="Nslookup Page", font=("Arial", 50))
        label.pack(pady=20)  # محاذاة العنوان في المنتصف

        # إطار لإدخال اسم النطاق وزر Nslookup بجانبه
        entry_frame = ctk.CTkFrame(self.frame)
        entry_frame.pack(pady=10)

        # إدخال اسم النطاق
        self.domain_entry = ctk.CTkEntry(entry_frame, placeholder_text="Enter Domain Name", font=("Arial", 20),
                                           width=300, height=50)
        self.domain_entry.pack(side='left', padx=(0, 5))  # إدخال الدومين على اليسار

        # زر لتنفيذ عملية Nslookup بجانب حقل الإدخال
        nslookup_button = ctk.CTkButton(entry_frame, text="Nslookup", height=50, font=("Arail", 30),
                                          command=self.perform_nslookup)
        nslookup_button.pack(side='left')  # زر Nslookup بجانب حقل الإدخال

        # TextBox لعرض النتائج
        self.result_textbox = ctk.CTkTextbox(self.frame, width=450, height=200, font=("Arial", 12))
        self.result_textbox.pack(pady=10)

        # زر لنسخ النتيجة تحت TextBox
        copy_button = ctk.CTkButton(self.frame, text="Copy Result", width=450, font=("Arail", 25),
                                     command=self.copy_result)
        copy_button.pack(pady=(5, 10))  # زر نسخ النتيجة تحت منطقة العرض

    def perform_nslookup(self):
        domain = self.domain_entry.get()  # الحصول على اسم النطاق من ال TextBox
        if domain:
            try:
                # تنفيذ الأمر nslookup باستخدام subprocess
                result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
                self.result_textbox.delete("1.0", ctk.END)  # مسح النص القديم
                self.result_textbox.insert(ctk.END, result.stdout)  # إدخال النتائج في ال TextBox
            except Exception as e:
                self.result_textbox.delete("1.0", ctk.END)  # مسح النص القديم
                self.result_textbox.insert(ctk.END, f"Error: {str(e)}")  # عرض الخطأ في حالة حدوثه
        else:
            self.result_textbox.delete("1.0", ctk.END)
            self.result_textbox.insert(ctk.END, "Please enter a domain name.")

    def copy_result(self):
        # الحصول على النص من الـ TextBox
        result_text = self.result_textbox.get("1.0", ctk.END)
        if result_text.strip():  # التأكد من أن النص ليس فارغاً
            pyperclip.copy(result_text)  # نسخ النص إلى الحافظة
            self.result_textbox.delete("1.0", ctk.END)  # مسح النص القديم
            self.result_textbox.insert(ctk.END, "Result copied to clipboard!")  # إعلام المستخدم
        else:
            self.result_textbox.delete("1.0", ctk.END)
            self.result_textbox.insert(ctk.END, "No result to copy.")

    def pack(self, *args, **kwargs):
        self.frame.pack(*args, **kwargs)
