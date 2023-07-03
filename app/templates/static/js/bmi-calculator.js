var form = document.getElementById("form");
form.addEventListener("submit", function (event) {
  event.preventDefault();
  var h = parseFloat(document.getElementById("height").value);
  var w = parseFloat(document.getElementById("weight").value);
  var bmi = (w / (h * h)) * 10000;
  if (bmi < 18.5) var result = "UNDERWEIGHT.😢Start taking a healthy diet.";
  else if (bmi >= 18.5 && bmi <= 24.9)
    var result = "NORMAL WEIGHT.👌Keep Maintaining.";
  else if (bmi >= 25.0 && bmi <= 29.9)
    var result = "OVERWEIGHT.Start Exercising .👍";
  else var result = "OBESITY.👍";
  document.getElementById("output").style.color = "black";
  document.getElementById("output").style.fontSize = "bold";
  document.getElementById("output").innerHTML =
    "Your BMI is " + bmi + "<br>" + result;
});
