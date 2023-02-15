document.querySelector("#add").onclick = function(){
    if(document.querySelector("#textField").value == 0){
        return;
    }
    else{
    document.querySelector("#tasks").innerHTML += `
    <div class="task">
        <div class="left">
        <input type="checkbox" class = "check">
        <p>${document.querySelector("#textField").value}</p>
        </div>
        <button class="delete">
        </button>
    </div>
    `

    let tasks = document.querySelectorAll(".delete")
    for(let i = 0; i < tasks.length; i++){
        tasks[i].onclick = function(){
            this.parentNode.remove();
        }
    }
}
document.querySelector("#textField").value = '';
}

let checkboxes = document.querySelectorAll('.check');
for(let checkbox in checkboxes){
    checkbox.onchange = function(e) {
        if(e.target.checked) {
          task.classList.toggle("chosen", true)
        } else {
          task.classList.toggle("chosen", false)
        }
    }   
}
