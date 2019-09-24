import urllib.request, json
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from datetime import datetime
from datetime import timedelta
from kivy.clock import Clock
from kivy.uix.label import Label
from datetime import date
import calendar
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty, ObjectProperty
import webbrowser

my_date = date.today()

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyAae9XuxUasMbqrUUDNOAr1rFN9wpPDu4M'

time = []

url1 = 'https://www.google.com/maps/dir/Wilmeth+Active+Learning+Center+(WALC),+Centennial+Mall+Dr,+West+Lafayette,+IN/Wilmeth+Active+Learning+Center+(WALC),+340+Centennial+Mall+Dr,+West+Lafayette,+IN+47907/@40.427421,-86.9482564,13z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x8812fd37423e0507:0x36aba311641c1373!2m2!1d-86.9132371!2d40.4274263!1m5!1m1!1s0x8812fd37423e0507:0x36aba311641c1373!2m2!1d-86.9132371!2d40.4274263!3e2'
url2 = 'https://www.google.com/maps/dir/Wilmeth+Active+Learning+Center+(WALC),+Centennial+Mall+Dr,+West+Lafayette,+IN/steven+beering+hall+of+lib+arts+%2526+ed/@40.4265127,-86.9156848,18z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x8812fd37423e0507:0x36aba311641c1373!2m2!1d-86.9132371!2d40.4274263!1m5!1m1!1s0x8812e2b16788b7b9:0x6aee7b16b42ba33c!2m2!1d-86.9160625!2d40.4253928'
url3 = 'https://www.google.com/maps/dir/Wilmeth+Active+Learning+Center+(WALC),+Centennial+Mall+Dr,+West+Lafayette,+IN/steven+beering+hall+of+lib+arts+%2526+ed/@40.4265127,-86.9156848,18z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x8812fd37423e0507:0x36aba311641c1373!2m2!1d-86.9132371!2d40.4274263!1m5!1m1!1s0x8812e2b16788b7b9:0x6aee7b16b42ba33c!2m2!1d-86.9160625!2d40.4253928' \
       ''
url4 = 'https://www.google.com/maps/dir/Wilmeth+Active+Learning+Center+(WALC),+Centennial+Mall+Dr,+West+Lafayette,+IN/Neil+Armstrong+Hall+of+Engineering,+West+Stadium+Avenue,+West+Lafayette,+IN/@40.4294039,-86.9161848,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x8812fd37423e0507:0x36aba311641c1373!2m2!1d-86.9132371!2d40.4274263!1m5!1m1!1s0x8812fd4d2c94148b:0xbe2d6407d66fe7aa!2m2!1d-86.9149125!2d40.4310566!3e2'
url5 = 'https://www.google.com/maps/dir/Wilmeth+Active+Learning+Center+(WALC),+Centennial+Mall+Dr,+West+Lafayette,+IN/Neil+Armstrong+Hall+of+Engineering,+West+Stadium+Avenue,+West+Lafayette,+IN/@40.4294039,-86.9161848,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x8812fd37423e0507:0x36aba311641c1373!2m2!1d-86.9132371!2d40.4274263!1m5!1m1!1s0x8812fd4d2c94148b:0xbe2d6407d66fe7aa!2m2!1d-86.9149125!2d40.4310566!3e2'
url6 = 'https://www.google.com/maps/dir/Wilmeth+Active+Learning+Center+(WALC),+Centennial+Mall+Dr,+West+Lafayette,+IN/brian+lamb+school+of+communication/@40.4267567,-86.9158135,18z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x8812fd37423e0507:0x36aba311641c1373!2m2!1d-86.9132371!2d40.4274263!1m5!1m1!1s0x8812e2b15be9ae95:0x9652d7e089dc876b!2m2!1d-86.9162105!2d40.4256266'

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
"""
def open_map():
    webbrowser.get(chrome_path).open(url2)
"""
var01 = ""
var02 = ""
var03 = ""
var04 = ""
var05 = ""
var06 = ""




class screen_one(GridLayout):

    def store_var(self, var):
        ls = [None] * 24
        destination = [None] * 6
        nav_request = [None] * 6
        request = [None] * 6
        response = [None] * 6
        directions = [None] * 6
        routes = [None] * 6
        legs = [None] * 6


        for item in var:
            ls[var.index(item)] = item.text

        for x in range(0, 6):
            origin = 'Purdue+Hillenbrand'
            mode = 'walking'

            for y in range(0, len(destination)):
                destination[y] = 'Purdue+' + ls[y*4].replace(' ', '+')
                nav_request[y] = 'origin={}&destination={}&mode={}&key={}'.format(origin, destination[y], mode, api_key)
                # Building the URL for the request
                request[y] = endpoint + nav_request[y]
            # Sends the request and reads the response.
                response[y] = urllib.request.urlopen(request[y]).read()
            # Loads response as JSON
                directions[y] = json.loads(response[y])
                routes[y] = directions[y]['routes']
            # duration = directions['duration']
                legs[y] = routes[y][0]['legs']
            # print(directions)
                time.append(legs[y][0]['duration']['text'])
        # print("It will take " + time + ".")


        """
        if len(destination) <= 6:
            var06 = time[5]
            var05 = time[4]
            var04 = time[3]
            var03 = time[2]
            var02 = time[1]
            var01 = time[0]
        elif len(destination) <= 5:
            var05 = time[4]
            var04 = time[3]
            var03 = time[2]
            var02 = time[1]
            var01 = time[0]
        elif len(destination) <= 4:
            var04 = time[3]
            var03 = time[2]
            var02 = time[1]
            var01 = time[0]
        elif len(destination) <= 3:
            var03 = time[2]
            var02 = time[1]
            var01 = time[0]
        elif len(destination) <= 2:
            var02 = time[1]
            var01 = time[0]
        elif len(destination) <= 1:
            var01 = time[0]
            """

        print(var01)
        print(var02)
        print(var03)
        print(var04)
        print(var05)
        print(var06)

    def clear_inputs(self, text_inputs):
        for item in text_inputs:
            item.text = ""


# second screen
class SubInterface(GridLayout):
    """
    url2 = 'https://www.google.com/maps/dir/40.4201472,-86.9122048/steven+beering+hall+of+lib+arts+%26+ed/@40.4227341,-86.9166245,17z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x8812e2b16788b7b9:0x6aee7b16b42ba33c!2m2!1d-86.9160625!2d40.4253928'

    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    """

    def open_map1(self):
        webbrowser.get(chrome_path).open(url1)

    def open_map2(self):
        webbrowser.get(chrome_path).open(url2)

    def open_map3(self):
        webbrowser.get(chrome_path).open(url3)

    def open_map4(self):
        webbrowser.get(chrome_path).open(url4)

    def open_map5(self):
        webbrowser.get(chrome_path).open(url5)

    def open_map5(self):
        webbrowser.get(chrome_path).open(url6)

    var1 = StringProperty()
    var2 = StringProperty()
    var3 = StringProperty()
    var4 = StringProperty()
    var5 = StringProperty()
    var6 = StringProperty()
    var1 = var01
    var2 = var02
    var3 = var03
    var4 = var04
    var5 = var05
    var6 = var06

class boilerpace(App):

    def build(self):
        self.screen_manager = ScreenManager()

        self.screen_one = screen_one()
        screen = Screen(name = 'screen_one')
        screen.add_widget(self.screen_one)
        self.screen_manager.add_widget(screen)

        self.screen_two = SubInterface()
        screen2 = Screen(name = 'screen_two')
        screen2.add_widget(self.screen_two)
        self.screen_manager.add_widget(screen2)

        return self.screen_manager

if __name__ == "__main__":
    boilerpace().run()
