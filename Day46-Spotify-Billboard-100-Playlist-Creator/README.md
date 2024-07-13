# Spotify Billboard 100 Playlist Creator

This script scrapes the Billboard Hot 100 chart for a specified date, searches for the tracks on Spotify, and creates a private playlist with those tracks.

## Prerequisites

- Python 3.6+
- Spotify Developer Account
- Spotify App with client ID and client secret

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/spotify-billboard-playlist.git
   cd spotify-billboard-playlist
   ```

2. Install required packages:

   ```sh
   pip install spotipy requests beautifulsoup4
   ```

3. Set up your Spotify developer credentials:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create a new app and get your `Client ID` and `Client Secret`.
   - Set a redirect URI (e.g., `http://example.com`) in your Spotify app settings.

## Configuration

1. Create a file named `.env` in the project directory and add your Spotify credentials:
   ```env
   SPOTIPY_CLIENT_ID='your_client_id'
   SPOTIPY_CLIENT_SECRET='your_client_secret'
   SPOTIPY_REDIRECT_URI='http://example.com'
   ```

## Usage

1. Run the script:

   ```sh
   python playlist_creator.py
   ```

2. Enter the date for which you want to create the Billboard Hot 100 playlist in the format `YYYY-MM-DD` when prompted.

## Example

1. When prompted, enter the date:

   ```
   Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2020-07-10
   ```

2. The script will:
   - Scrape the Billboard Hot 100 chart for the specified date.
   - Search for each track on Spotify.
   - Create a private playlist named `2020-07-10 Billboard 100`.
   - Add the found tracks to the playlist.

## Notes

- The script may not find every track on Spotify. If a track is not found, it will be skipped with a message.
- Ensure your Spotify app has the necessary permissions (`playlist-modify-private`).
