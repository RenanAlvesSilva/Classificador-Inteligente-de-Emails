let dropZone = document.getElementById("dropzone_file");
let emailText = document.getElementById("email_text");
let changeText = document.getElementById("changeText");
let changeFile = document.getElementById("changeFile");
let labelText = document.getElementById("labelText");
let btnSubmition = document.getElementById("btnSubmition");
let btnSendAgain = document.getElementById("btnSendAgain");
let formContent = document.getElementById("formContent");
let analisando = document.getElementById("analisando");
let resultArea = document.getElementById("resultArea");
let instructionText = document.getElementById("instructionText");

changeFile.addEventListener("click", function (e) {
    e.preventDefault();
    dropZone.classList.remove("hidden");
    emailText.classList.add("hidden");
    changeFile.classList.add("hidden");
    changeText.classList.remove("hidden");
    labelText.classList.add("hidden");
});

changeText.addEventListener("click", function (e) {
    e.preventDefault();
    dropZone.classList.add("hidden");
    emailText.classList.remove("hidden");
    changeText.classList.add("hidden");
    changeFile.classList.remove("hidden");
    labelText.classList.remove("hidden");
});

btnSubmition.addEventListener("click", function (e) {
    instructionText.classList.add("hidden");
    btnSubmition.classList.add("hidden");
    btnSendAgain.classList.remove("hidden");
    formContent.classList.add("hidden");
    analisando.classList.remove("hidden");
})
btnSendAgain.addEventListener("click", function (e) {
    e.preventDefault();
    resultArea.classList.add("hidden");
})

