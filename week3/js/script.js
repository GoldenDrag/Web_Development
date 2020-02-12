function anotherToDo() {
    var input = document.getElementById("user-input").value;
    var node = document.createElement("li");
    var v = document.createElement("INPUT");
    var x = document.createElement("input");
    
    v.setAttribute("type", "checkbox");
    v.style.float = "left";
    x.type = "button";
    x.style.height = "10px";
    x.style.width = "10px";
    x.style.float = "right";
    // v.className = "chichi";
    v.onclick = checked;
    node.className = "activity";

    if (input == "") {
        alert("TY SCHO?")
    }
    else {
        node.appendChild(v);
        node.innerHTML=input;
        node.appendChild(x);
        document.getElementById("todo").appendChild(node);
    }
    // document.getElementById("user-input") = "";
}

function checked() {
    node.className = "checked";
}