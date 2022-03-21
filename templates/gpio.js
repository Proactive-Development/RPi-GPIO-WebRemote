function set_high(){
    var xhttp = new XMLHttpRequest();
    signin_response = "";
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        }
    };
    xhttp.open("GET", "set?pin="+document.getElementById("Pin_Number").value+"&mode=HIGH", true);
    xhttp.send();
}
function set_low(){
    var xhttp = new XMLHttpRequest();
    signin_response = "";
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        }
    };
    xhttp.open("GET", "set?pin="+document.getElementById("Pin_Number").value+"&mode=LOW", true);
    xhttp.send();
}