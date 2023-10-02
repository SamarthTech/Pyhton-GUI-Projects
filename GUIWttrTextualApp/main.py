"""
::@name Get Weather for a city and display it in the console

::@description
    Takes input for city. Gives output of weather for a city in a text format.
    Command arg -c City
::@/description

"""
import httpx
from rich.text import Text

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Static, Header, Footer


# pylint: disable=invalid-name
class WTTR_App(App):
    """App to display the current weather."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Input(placeholder="Enter a City")
        with VerticalScroll(id="weather-container"):
            yield Static(id="weather")

    async def on_input_changed(self, message: Input.Changed) -> None:
        """Called when the input changes"""
        self.run_worker(self.update_weather(message.value), exclusive=True)

    async def update_weather(self, city: str) -> None:
        """Update the weather for the given city."""
        weather_widget = self.query_one("#weather", Static)
        if city:
            # Query the network API
            url = f"https://wttr.in/{city}"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                weather = Text.from_ansi(response.text)
                weather_widget.update(weather)
        else:
            # No city, so just blank out the weather
            weather_widget.update("")


if __name__ == "__main__":
    app = WTTR_App()
    app.run()
