// delete reminders
const deleteBtns = document.querySelectorAll(".delete-reminder");

for (const rBtn of deleteBtns) {
    rBtn.addEventListener('click', (evt) => {
        evt.preventDefault();
        console.log(typeof rBtn)
        
        fetch('/delete-reminder', {
            method: "POST",
            body: JSON.stringify({'btn_id': rBtn.id}),
            headers: {
                'Content-Type': 'application/json'
                    },
        })

        .then((response) => {console.log(response)
            return response
        })
        .then((responseJson) => {
            document.querySelector(`#delete${rBtn.id}`).remove();
            console.log(responseJson);
        })

        

    });
};

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
