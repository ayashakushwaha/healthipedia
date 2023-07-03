window.addEventListener("load", () => {
    const data = new URL(document.location).searchParams.get("data").split(",");
  
    // const age = params.get("age");
    // const gender = params.get("gender");
    // const bilirubin = params.get("bilirubin");
    // const phosphate = params.get("phosphate");
    // const aminotransferase = params.get("aminotransferase");
    // const aspertate = params.get("aspertate");
    // const protein = params.get("protein");
    // const albumin = params.get("albumin");
    // const globulin = params.get("globulin");
  
    document.getElementById("result-age").innerHTML = data[0];
    document.getElementById("result-gender").innerHTML = data[1] ? "Male" : "Female";
    document.getElementById("result-bilirubin").innerHTML = data[2];
    document.getElementById("result-phosphate").innerHTML = data[4];
    document.getElementById("result-aminotransferase").innerHTML = data[5];
    document.getElementById("result-aspertate").innerHTML = data[6];
    document.getElementById("result-protein").innerHTML = data[7];
    document.getElementById("result-albumin").innerHTML = data[8];
    document.getElementById("result-globulin").innerHTML = data[9];
});
  
document.querySelector(".reset-button").addEventListener("click", () => {
    document.querySelectorAll("input").value = "";
});