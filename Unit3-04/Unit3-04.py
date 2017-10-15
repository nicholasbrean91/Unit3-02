import ui

def calculate_leep_year_touch_up_inside(sender):
	
    leapyear = int(view['leap_year_textfield'].text)
	
    if (leapyear % 4) == 0:
      if (leapyear % 100)== 0:
        if (leapyear % 400) == 0:
          view['answer_label'].text = 'leap year' 
        else:
          view['answer_label'].text = 'not leap year'
      else:
        view['answer_label'].text = 'is a leap year'
    else:
      view['answer_label'].text = 'not leap year'


view = ui.load_view()
view.present('sheet')
