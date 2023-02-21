// delete reminders
const deleteBtns = document.querySelectorAll(".delete-to-do");

for (const toDoBtn of deleteBtns) {
    toDoBtn.addEventListener('click', (evt) => {
        evt.preventDefault();
        
        fetch('/delete-to-do', {
            method: "POST",
            body: JSON.stringify({'btn_id': toDoBtn.id}),
            headers: {
                'Content-Type': 'application/json'
                    },
                
        })

        .then((response) => {console.log(response)
            return response
        })
        .then((responseJson) => {
            document.querySelector(`#delete${toDoBtn.id}`).remove();
            console.log(responseJson)
        })

        

    });
};

// delete braindumps
const deleteBdBtns = document.querySelectorAll(".delete-bd");

for (const btn of deleteBdBtns) {
    btn.addEventListener('click', (evt) => {
        evt.preventDefault();

        fetch('/delete-braindumps', {
            method: "POST",
            body: JSON.stringify({'bd_btn_id': btn.id}),
            headers: {
                'Content-Type': 'application/json'
                    },
        })

        .then((response) => {console.log(response)
            return response
        })
        .then((responseJson) => {
            document.querySelector(`#delete${btn.id}`).remove();
            console.log(responseJson);
        })

        

    });
}
