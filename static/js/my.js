var navbtn = document.getElementById("phoneNav")
navbtn.className = "hidden";

function navFunc() {
    if (navbtn.className == "hidden") {
        navbtn.className = "block"
        
    }
    else {
        navbtn.className = "hidden"
    }
}


    