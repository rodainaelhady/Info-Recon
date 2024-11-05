import customtkinter as ctk
from ping import Ping
from traceroute import Traceroute
from nslookup import Nslookup

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Info Recon Tool")
        self.master.geometry("600x400")

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.pack(fill="both", expand=True)

        self.load_page(None)

    def load_page(self, page_class):
        # حذف الصفحة السابقة
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if page_class is None:
            # عرض الصفحة الرئيسية
            welcome_label = ctk.CTkLabel(self.main_frame, text="Welcome to Info Recon Tool", font=("Arial", 50))
            welcome_label.pack(pady=(50, 30))

            # إضافة الأزرار
            button1 = ctk.CTkButton(self.main_frame, text="Ping", font=("Arial", 40), width=400, height=120, corner_radius=200, command=lambda: self.load_page(Ping))
            button1.pack(pady=(10, 50))

            button2 = ctk.CTkButton(self.main_frame, text="Traceroute", font=("Arial", 40), width=400, height=120, corner_radius=200, command=lambda: self.load_page(Traceroute))
            button2.pack(pady=(10, 50))

            button3 = ctk.CTkButton(self.main_frame, text="Nslookup", font=("Arial", 40), width=400, height=120, corner_radius=200, command=lambda: self.load_page(Nslookup))
            button3.pack(pady=(10, 50))

        else:
            # إنشاء وتحميل الصفحة الجديدة
            page = page_class(self.main_frame, self.load_page)
            page.pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = MainApp(root)
    root.mainloop()
