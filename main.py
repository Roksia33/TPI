import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import speedtest
import os

def run_speed_test():
    st = speedtest.Speedtest(secure=True)
    st.get_best_server()
    download_speed = st.download() / (10**6)
    upload_speed = st.upload() / (10**6)
    ping_speed = st.results.ping
    operator = st.results.client['isp']

    operator_label.config(text=f"Operator: {operator}\n")
    download_label.config(text=f"Prędkość pobierania: {download_speed:.2f} Mbps\n")
    upload_label.config(text=f"Prędkość wysyłania: {upload_speed:.2f} Mbps\n")
    ping_label.config(text=f"Ping: {ping_speed:.2f} ms")

    text_label = tk.Label(root, text="", font=("Helvetica", 20))
    text_label.pack(pady=20)
    run_button.pack_forget()
    save_button.pack(pady=5)
    reset_button.pack(pady=5)
    exit_button.pack(pady=5)

def reset_results():
    main_text_label.config(text="Sprawdź prędkość swojego internetu", font=("Helvetica", 20))
    operator_label.config(text="Operator: ----\n", font=("Helvetica", 17))
    download_label.config(text="Prędkość pobierania: ----\n", font=("Helvetica", 17))
    upload_label.config(text="Prędkość wysyłania: ----\n", font=("Helvetica", 17))
    ping_label.config(text="Ping: ----\n", font=("Helvetica", 17))

    run_button.pack(pady=30)
    save_button.pack_forget()
    reset_button.pack_forget()
    exit_button.pack_forget()

def save_results():
    now = datetime.now()
    date = now.strftime("%d.%m.%Y")
    time = now.strftime("%H:%M:%S")
    operator_show = operator_label.cget("text")
    download_speed = download_label.cget("text")
    upload_speed = upload_label.cget("text")
    ping_speed = ping_label.cget("text")
    dec1 =(" "*2+"-"*20)
    dec2 =" | "
    dec3 =("-"*35)

    current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    filename = f"wyniki_speedtestu_{current_time}.txt"
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    filepath = os.path.join(desktop_path, filename)

    with open(filepath, "w") as file:
        file.write(dec1+"\n")
        file.write(dec2+"Data: "+str(date)+(" "*2)+dec2+"\n")
        file.write(dec2+"Godzina: "+str(time)+(" "*1)+dec2+"\n")
        file.write(dec1+"\n\n")
        file.write(dec3+"\n")
        file.write(f"{operator_show}"+"\n")
        file.write(f"{download_speed}"+"\n")
        file.write(f"{upload_speed}"+"\n")
        file.write(f"{ping_speed}"+"\n")
        file.write(dec3+"\n")
        file.close()
    messagebox.showinfo("Info", f"Wyniki zostały zapisane na pulpicie pod nazwą:\n{filename}")


def exit_program():
    result = messagebox.askquestion("Wyjście", "Czy na pewno chcesz wyjść z programu?")
    if result == "yes":
        root.quit()

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("TPI App")
window_width = 550
window_height = 750
center_window(root, window_width, window_height)
root.resizable(False,False)

main_text_label = tk.Label(root, text="Sprawdź prędkość swojego internetu", font=("Helvetica", 20))
operator_label= tk.Label(root,text="Operator: ----\n", font=("Helvetica", 17))
download_label = tk.Label(root, text="Prędkość pobierania: ----\n", font=("Helvetica", 17))
upload_label = tk.Label(root, text="Prędkość wysyłania: ----\n", font=("Helvetica", 17))
ping_label = tk.Label(root, text="Ping: ----\n", font=("Helvetica", 17))

main_text_label.pack(pady=40)
operator_label.pack()
download_label.pack()
upload_label.pack()
ping_label.pack()

run_button = tk.Button(root, text="Uruchom tester", cursor ="hand2", height = 3, width = 25, bg='#ffb92d', command=run_speed_test, font=("Helvetica", 16))
reset_button = tk.Button(root, text="Reset", cursor ="hand2", height = 3, width = 25, bg='#ffb92d', command=reset_results, font=("Helvetica", 16))
save_button = tk.Button(root, text="Zapisz Wyniki", cursor ="hand2", height = 3, width = 25, bg='#ffb92d', command=save_results, font=("Helvetica", 16))
exit_button = tk.Button(root, text="Wyjdź", cursor ="hand2", height = 3, width = 25, bg='#ffb92d', command=exit_program, font=("Helvetica", 16))

run_button.pack(pady=30)

root.protocol("WM_DELETE_WINDOW", exit_program)

if __name__ == "__main__":
    root.mainloop()
