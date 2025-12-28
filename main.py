from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest
from kivy.core.window import Window

class ARMSignalX(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        layout = BoxLayout(orientation='vertical', padding=50)
        self.label = Label(
            text="ARMSignalX\nLoading Market Data...",
            font_size='22sp',
            color=(1, 1, 1, 1),
            halign="center"
        )
        layout.add_widget(self.label)
        self.get_prices()
        return layout

    def get_prices(self):
        url = "https://api.twelvedata.com/price?symbol=EUR/USD,BTC/USD,XAU/USD&apikey=demo"
        UrlRequest(url, self.on_success)

    def on_success(self, request, result):
        if isinstance(result, dict):
            text = "ARMSignalX - MARKET\n\n"
            for s, d in result.items():
                text += f"{s}: {d.get('price', '0.00')}\n"
            self.label.text = text

if __name__ == '__main__':
    ARMSignalX().run()
