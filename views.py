import tkinter as tk
from typing import Tuple
import customtkinter as ctk



class DevinetteApp(ctk.CTk):
    
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        


# -------------page acceuil-------------------------

class AcceuilPage(ctk.CTkFrame):
    
    def __init__(self,master):
        super().__init__(master)
        
        


        