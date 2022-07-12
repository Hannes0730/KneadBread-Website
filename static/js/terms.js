 function validate(){
    var isCheck = document.getElementById("formCheck-1");
    var button = document.getElementById("registerBtn");
    button.disabled = !isCheck.checked;
}
