const bdForm = document.querySelector('#bd-form');
const reminderForm = document.querySelector("#reminder-form");
const textArea = document.querySelector("textarea");
const bdMain = document.querySelector("#bd-main");
const reminderMain = document.querySelector("#reminder-main");
const bdUl = document.querySelector("#bd-ul-list");
const reminderUl = document.querySelector("#reminder-ul-list");
const reminderValues = document.querySelectorAll(".reminder-value");


// create li for brain dumps
function createBdLi() {
    const li = document.createElement('li');
    const span = document.createElement('span');
    span.textContent = textArea.value;
    const editBtn = document.createElement('button');
    editBtn.textContent = 'edit';
    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'remove';
    
    li.appendChild(span);
    li.appendChild(editBtn);
    li.appendChild(removeBtn);

    return li;
    
}

// create li for reminders
function createReminderLi() {
    const rValues = []
    const li = document.createElement('li');
    const span = document.createElement('span');
    for (const i = 0; i <= reminderValues.length - 1; i++) {
        rValues.push(reminderValues[i].textContent)
    }
    span.textContent = rValues;
    const editBtn = document.createElement('button');
    editBtn.textContent = 'edit';
    const removeBtn = document.createElement('button');
    removeBtn.textContent = 'remove';
    
    li.appendChild(span);
    li.appendChild(editBtn);
    li.appendChild(removeBtn);

    return li;
    
}

bdForm.addEventListener('submit', (evt) => {
    evt.preventDefault();

    const li = createBdLi();
    
    if(textArea.value === "") {
        alert("Please enter text before submitting!");
    } else {
        bdUl.appendChild(li);
    }
});

reminderForm.addEventListener('submit', (evt) => {
    evt.preventDefault();

    const li = createReminderLi();
    
    if(reminderValues === []) {
        alert("Please enter text before submitting!");
    } else {
        reminderUl.appendChild(li);
    }
});

// button actions

bdUl.addEventListener('click', (evt) => {
    if(evt.target.tagName==='BUTTON') {
        const button = evt.target;
        const li = button.parentNode;
        const ul = li.parentNode;
        if(button.textContent === 'remove') {
            ul.removeChild(li);
        } else if(button.textContent === 'edit') {
            const span = li.firstElementChild;
            const text = document.createElement('textarea');
            text.value = span.textContent;
            li.insertBefore(text, span);
            li.removeChild(span);
            button.textContent = 'save';
        } else if(button.textContent === 'save') {
            const text = li.firstElementChild;
            const span = document.createElement('span');
            span.textContent = text.value;
            li.insertBefore(span, text);
            li.removeChild(text);
            button.textContent = 'edit';
        }
    }

});