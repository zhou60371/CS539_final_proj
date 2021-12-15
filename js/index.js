console.log("123");

var overview = document.getElementById("overview");
var overviewBox = document.getElementsByClassName("overview")[0];
var dataset = document.getElementById("dateset");
var datasetBox = document.getElementsByClassName("dataset")[0];
var model = document.getElementById("model");
var modelBox = document.getElementsByClassName("model")[0];
var result = document.getElementById("result");
var resultBox = document.getElementsByClassName("result")[0];
var demo = document.getElementById("demo");
var demoBox = document.getElementsByClassName("demo")[0];
var team = document.getElementById("team");
var teamBox = document.getElementsByClassName("team")[0];



overview.addEventListener("click", function () {
    overviewBox.style.display = "block";
    overview.classList.add("active");
    datasetBox.style.display = "none";
    dataset.classList.remove("active");
    modelBox.style.display = "none";
    model.classList.remove("active");
    resultBox.style.display = "none";
    result.classList.remove("active");
    demoBox.style.display = "none";
    demo.classList.remove("active");
    teamBox.style.display = "none";
    team.classList.remove("active");
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
    demoBox.style.display = "none";
    demo.classList.remove("active");
    teamBox.style.display = "none";
    team.classList.remove("active");
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
    demoBox.style.display = "none";
    demo.classList.remove("active");
    teamBox.style.display = "none";
    team.classList.remove("active");
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
    demoBox.style.display = "none";
    demo.classList.remove("active");
    teamBox.style.display = "none";
    team.classList.remove("active");
})

demo.addEventListener("click", function (e) {
    overviewBox.style.display = "none";
    overview.classList.remove("active");
    datasetBox.style.display = "none";
    dataset.classList.remove("active");
    modelBox.style.display = "none";
    model.classList.remove("active");
    resultBox.style.display = "none";
    result.classList.remove("active");
    demoBox.style.display = "block";
    demo.classList.add("active");
    teamBox.style.display = "none";
    team.classList.remove("active");
})

team.addEventListener("click", function (e) {
    overviewBox.style.display = "none";
    overview.classList.remove("active");
    datasetBox.style.display = "none";
    dataset.classList.remove("active");
    modelBox.style.display = "none";
    model.classList.remove("active");
    resultBox.style.display = "none";
    result.classList.remove("active");
    demoBox.style.display = "none";
    demo.classList.remove("active");
    teamBox.style.display = "block";
    team.classList.add("active");
})


