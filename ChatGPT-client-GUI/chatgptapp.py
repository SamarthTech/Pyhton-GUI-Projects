from delphifmx import *
import openai

openai.api_key = ''  # Set your API key here

class ChatGPTForm(Form):

    def __init__(self, owner):
        self.stylemanager = StyleManager(self)
        self.stylemanager.SetStyleFromFile("Air.style")

        self.SetProps(Caption="OpenAI ChatGPT Example", OnShow=self.__form_show, OnClose=self.__form_close)

        self.layout_top = Layout(self)
        self.layout_top.SetProps(Parent=self, Align="Top", Height="50", Margins = Bounds(RectF(3, 3, 3, 3)))

        self.prompt_label = Label(self)
        self.prompt_label.SetProps(Parent=self.layout_top, Align="Left", Text="Prompt:", Position=Position(PointF(20, 20)), Margins = Bounds(RectF(3, 3, 3, 3)))

        self.prompt_edit = Edit(self)
        self.prompt_edit.SetProps(Parent=self.layout_top, Align="Client", Text="What is Embarcadero Delphi?", Position=Position(PointF(80, 18)), Width=200, Margins = Bounds(RectF(3, 3, 3, 3)))

        self.generate_button = Button(self)
        self.generate_button.SetProps(Parent=self.layout_top, Align = "Right", Text="Generate", Position=Position(PointF(290, 18)), Width=80, OnClick=self.__button_click, Margins = Bounds(RectF(3, 3, 3, 3)))

        self.memo_control = Memo(self)
        self.memo_control.SetProps(Parent=self, Align="Client", WordWrap="True", Position=Position(PointF(20, 60)), Width=350, Height=350, Margins = Bounds(RectF(3, 3, 3, 3)))

    def __form_show(self, sender):
        self.SetProps(Width=640, Height=480)

    def __form_close(self, sender, action):
        action = "caFree"

    def __button_click(self, sender):
        prompt = self.prompt_edit.text
        self.memo_control.Lines.Text = ""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are the best writer, marketer, and programmer in the world."},
                {"role": "user", "content": prompt}
            ]
        )
        output = response['choices'][0]['message']['content']
        for item in output:
                self.memo_control.Lines.Text = self.memo_control.Lines.Text + item

def main():
    Application.Initialize()
    Application.Title = "OpenAI ChatGPT Example"
    Application.MainForm = ChatGPTForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
