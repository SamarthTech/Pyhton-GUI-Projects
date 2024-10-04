# Dependencies to bbe installed: tkinter,qrcode,PIL

import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk


def generate_qr():
    url = url_entry.get()

    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL!")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save("qr.jpg")

    qr_image = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image

    messagebox.showinfo("Success", "QR code generated and saved as 'qr.jpg'!")


root = tk.Tk()
root.title("QR Code Generator")


window_width = 500
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

root.geometry(
    f"{window_width}x{window_height}+{position_right}+{position_top}")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

title_label = tk.Label(frame, text="QR Code Generator",
                       font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

url_label = tk.Label(frame, text="Enter URL:", font=("Arial", 14))
url_label.pack(pady=10)

url_entry = tk.Entry(frame, font=("Arial", 14), width=30)
url_entry.pack(pady=10)


def on_enter(e):
    generate_button['background'] = '#4CAF50'
    generate_button['foreground'] = '#FFFFFF'


def on_leave(e):
    generate_button['background'] = '#5C85D6'
    generate_button['foreground'] = '#FFFFFF'


generate_button = tk.Button(frame, text="Generate QR Code", font=("Arial", 14), bg="#5C85D6", fg="white",
                            activebackground="#4CAF50", activeforeground="white", command=generate_qr)
generate_button.pack(pady=20)

generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)


qr_label = tk.Label(frame, bg="white", relief="solid",
                    bd=2, width=300, height=300)
qr_label.pack(pady=20)

root.mainloop()
