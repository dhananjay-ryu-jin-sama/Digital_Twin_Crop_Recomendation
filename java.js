function display() {
  // Example: fetching humidity value from somewhere
  var humidityValue   = 50  ; // Example value (you can replace this with your actual value)
  var moisture_val    = 70;
  var temperature_val = 80;
  var sodium_val      = 90;
  var potasium_val    = 20;

  // Update humidity value in the span
  var humiditySpan = document.querySelector('.humidity span');
  if (humiditySpan) {
      humiditySpan.textContent = humidityValue;
  }

  var moistureSpan = document.querySelector('.Moisture span');
  if (moistureSpan) {
      moistureSpan.textContent = moisture_val;
  }

  var temperatureSpan = document.querySelector('.Temperature span');
  if (temperatureSpan) {
      temperatureSpan.textContent = temperature_val;
  }

  var sodiumSpan = document.querySelector('.Sodium span');
  if (sodiumSpan) {
      sodiumSpan.textContent = sodium_val;
  }

  var potasiumSpan = document.querySelector('.Potasium span');
  if (potasiumSpan) {
      potasiumSpan.textContent = potasium_val;
  }


}
