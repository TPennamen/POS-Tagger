import tkinter as tk
import json
from methods import nltk_pos_tag, ttpw_pos_tag

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        options_list = ["NLTK", "TreeTagger"]
        with open('legend.json') as json_file:
            self.legend = json.load(json_file)

        self.option_choice = tk.StringVar()
        self.option_choice.set(options_list[0])
        self.option_frame = tk.Frame(master = self)
        for option in options_list :
            b = tk.Radiobutton(master=self.option_frame, variable=self.option_choice, indicatoron=0,  text=option, value=option)
            b.pack(side='left', expand=1)
        self.option_frame.pack(ipady=5)
        
        self.input_frame = tk.Frame(master = self)
        self.input_frame.pack(ipady=5)
        tk.Label(master =  self.input_frame, text='Input Text').grid(row=0)
        tk.Button(master = self.input_frame, command=self.show_example, text='Exemple').grid(row=1)
        self.input_entry = tk.Text(master = self.input_frame, height=5)
        self.input_entry.grid(row=2, ipadx=50)

        self.output_frame = tk.Frame(master = self, relief='groove')
        tk.Button(master=self.output_frame,text="Tagger", command=self.tag).grid(row=0)
        self.output_frame.pack(ipady=5)
        tk.Label(master =  self.output_frame, text='Output Text').grid(row=1)
        self.output_box = tk.Text(master = self.output_frame, relief='groove')
        self.output_box.grid(row=2)
        
    def tag(self) :
        self.output_box.delete("1.0", "end")
        result = []
        if self.option_choice.get()=='NLTK' :
            legend = self.legend['NLTK']    
            result = nltk_pos_tag(self.input_entry.get("0.0","end"))
        if self.option_choice.get()=='TreeTagger' :
            legend = self.legend['TreeTagger']    
            result = ttpw_pos_tag(self.input_entry.get("0.0","end"))

        last_word = ""
        if result:
            last_index = 0
            for index, result_word in enumerate(result): 
                word = self.translate(result_word[0])
                self.output_box.insert(f"1.{last_index}",word + ' ')
                word_size = len(word)+1
                self.output_box.tag_add(str(index), f"1.{last_index}", f"1.{last_index + word_size-1}")
                self.output_box.tag_config(tagName=str(index),background=legend[result_word[1]]['color'] if result_word[1] in legend and 'color' in legend[result_word[1]] else "white" )
                last_word = word
                last_index += word_size
   
    def show_example(self) :
        self.input_entry.delete("1.0", "end")
        f = open("example_input.txt", "r")
        self.input_entry.insert(f"1.0", self.translate(f.read()))


    def translate(self, text) :
        try :
            return text.encode('windows-1252').decode('utf-8')
        except UnicodeDecodeError :
            return text

if __name__ =="__main__":
    app = MainApp()
    app.title("POS Tag")
    app.geometry("740x560+100+100")
    app.minsize(640, 460)
    app.mainloop()