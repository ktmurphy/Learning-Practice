from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorieCalculator import CalorieCalculator
from temperatureGetter import TemperatureGetter

app = Flask(__name__)

class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')

class CalorieFormPage(MethodView):
    
    def get(self):
        form = CalorieForm()
        return render_template('calorie_form_page.html', form = form)
    
    def post(self):
        form = CalorieForm(request.form)
        weight = float(form.weight.data)
        height = float(form.height.data)
        age = float(form.age.data)
        city = form.city.data
        country = form.country.data
        temperature = TemperatureGetter(city = city, country = country).getTemperature()
        calories_needed = CalorieCalculator(weight, age, height, temperature).calculateCalories()

        return render_template('calorie_form_page.html', 
                               result = True,
                               calories = calories_needed,
                               form = form)
class CalorieForm(Form):
    weight = StringField("Weight in Pounds", default = 45)
    height = StringField("Height in Centimeters", default = 175)
    age = StringField("Age", default = 30)
    city = StringField("City")
    country = StringField("Country")
    button = SubmitField("Calculate")

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_form_page', view_func=CalorieFormPage.as_view('calorie_form_page'))

app.run(debug=True)