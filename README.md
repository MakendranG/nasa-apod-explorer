# NASA Astronomy Picture of the Day Explorer

This project is a simple web application that uses NASA's [APOD API](https://api.nasa.gov/#apod) to display the Astronomy Picture of the Day. Users can also explore pictures from previous dates.

---

## Features
- Fetches the Astronomy Picture of the Day from NASA's API.
- Displays the picture (or video) along with its title, date, and explanation.
- Allows users to explore pictures from earlier dates.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MakendranG/nasa-apod-explorer.git
   cd nasa-apod-explorer
   ```

2. Install Flask:
   ```bash
   pip install flask
   ```

3. Add your NASA API key:
   - Open `app.py` and replace `your_nasa_api_key` with your actual NASA API key.

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## Contributions
Feel free to fork the repository and submit pull requests for improvements.

---

## License
This project is licensed under the MIT License.
