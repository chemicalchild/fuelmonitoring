// Function to fetch and update card values with real-time data
function updateCardValues() {
  fetch('http://127.0.0.1:5000/send_data') // Replace with your Flask app's URL
    .then(response => response.json())
    .then(data => {
      console.log('Data received:', data)
      // Assuming data is an array of objects with keys: timestamp, temperature, ph, turbidity, tds
      if (data.length > 0) {
        // Update Temperature Card
        document.getElementById('latitude').textContent = data[data.length - 1].latitude;

        // Update pH Card
        document.getElementById('longitude').textContent = data[data.length - 1].longitude;

        // Update Turbidity Card
        document.getElementById('level').textContent = data[data.length - 1].fuel_level + ' %';

        if (data[data.length - 1].fuel_level <= 20) {
             document.getElementById('monitorIndicator').style.backgroundColor = "red";
          } else {
            document.getElementById('monitorIndicator').style.backgroundColor = "green";
          }

        // Update TDS Card
        // document.getElementById('tdsValue').textContent = data[data.length - 1].tds + ' ppm';
      }
    })
    .catch(error => {
      console.error('Error fetching real-time data:', error);
    });
}

// Call the updateCardValues function periodically (e.g., every 5 seconds)
setInterval(updateCardValues, 5000); // Adjust the interval as needed
