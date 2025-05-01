# 🎵 95.7 BenFM to Amazon Music Playlist Converter

Easily convert the daily playlist from Philadelphia’s 95.7 BenFM to your Amazon Music account — automatically.

## 🚀 Features

- Pulls all songs played today by 95.7 BenFM
- Uses [TuneMyMusic](https://www.tunemymusic.com/) to convert and transfer the playlist
- Syncs directly to your Amazon Music account

## 📦 Requirements

- A [TuneMyMusic](https://www.tunemymusic.com/) account
- Amazon Music account (linked within TuneMyMusic)
    - this could work with other platforms but has not been tested


## 🔧 Setup Instructions

1. **Create an account on TuneMyMusic**  
   - Visit: [https://www.tunemymusic.com/](https://www.tunemymusic.com/)  
   - In your settings, connect your **Amazon Music** account

2. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/benfm-amazon-converter.git
   cd benfm-amazon-converter
   ```

3. **Set up the repository**
    1. Create a .env file and add 
   ```bash
    USERNAME=your_tunemymusic_username
    PASSWORD=your_tunemymusic_password
    ```
    2. Update PLAYLIST_NAME within main.py for your given playlist on amazon music 
        - This playlist MUST already be created with at least 1 song in it on Amazon Music
    ```bash
    PLAYLIST_NAME = "BenFM 2025"
    ```
    3. [Install Tech Stack Dependencies](#installation)

## 💡 How It Works

1. Fetches the songs played by 95.7 BenFM’s website
2. Parses and cleans up the song list
3. Finds any new songs not added already to your playlist (songs added by this application only not you manually adding songs)
4. Uses TuneMyMusic’s website to transfer the list to your Amazon Music Playlist
5. Console logs all songs that were added (Essentially any songs added to SongList.txt because they were not duplicates)

## 🛠 Tech Stack

To run the script, you'll need the following Python libraries:

- **Selenium**: Automates browser interactions.
- **python-dotenv**: Loads environment variables from a `.env` file.
- **BeautifulSoup (from `bs4`)**: Parses HTML content.
- **chromedriver_autoinstaller**: Manages the Chrome WebDriver.

### Prerequisites

- Python 3.x (ensure it's installed on your system)

### Installation

- Install the required dependencies by running the following command:

    ```bash
    pip install selenium python-dotenv beautifulsoup4 chromedriver-autoinstaller
