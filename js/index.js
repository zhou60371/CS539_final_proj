console.log("123");

var overview = document.getElementById("overview");
var overviewBox = document.getElementsByClassName("overview")[0];
var dataset = document.getElementById("dateset");
var datasetBox = document.getElementsByClassName("dataset")[0];
var model = document.getElementById("model");
var modelBox = document.getElementsByClassName("model")[0];
var result = document.getElementById("result");
var resultBox = document.getElementsByClassName("result")[0];



overview.addEventListener("click", function () {
    overviewBox.style.display = "block";
    overview.classList.add("active");
    datasetBox.style.display = "none";
    dataset.classList.remove("active");
    modelBox.style.display = "none";
    model.classList.remove("active");
    resultBox.style.display = "none";
    result.classList.remove("active");
})

dataset.addEventListener("click", function (e) {
    overviewBox.style.display = "none";
    overview.classList.remove("active");
    datasetBox.style.display = "block";
    dataset.classList.add("active");
    modelBox.style.display = "none";
    model.classList.remove("active");
    resultBox.style.display = "none";
    result.classList.remove("active");
})

model.addEventListener("click", function (e) {
    overviewBox.style.display = "none";
    overview.classList.remove("active");
    datasetBox.style.display = "none";
    dataset.classList.remove("active");
    modelBox.style.display = "block";
    model.classList.add("active");
    resultBox.style.display = "none";
    result.classList.remove("active");
})

result.addEventListener("click", function (e) {
    overviewBox.style.display = "none";
    overview.classList.remove("active");
    datasetBox.style.display = "none";
    dataset.classList.remove("active");
    modelBox.style.display = "none";
    model.classList.remove("active");
    resultBox.style.display = "block";
    result.classList.add("active");
})
