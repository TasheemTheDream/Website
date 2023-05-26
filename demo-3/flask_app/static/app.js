const form = document.querySelector("#form-upload");
const progress = document.querySelector(".progress");
const progressBar = document.querySelector(".progress-bar");
const errorMessageDiv = document.querySelector("#error-div");
const successMessageDiv = document.querySelector("#success-div");

// Helper functions
function showProgressBar() {
    progress.style.display = "flex";
}
function setProgressBarPercentage(percentage) {
    progressBar.style.width = `${percentage}%`;
}

function showErrorMessage(message) {
    errorMessageDiv.innerHTML = message;
    errorMessageDiv.style.display = "block";
}

function showSuccessMessage(message) {
    successMessageDiv.innerHTML = message;
    successMessageDiv.style.display = "block";
}

function hideMessages() {
    errorMessageDiv.style.display = "none";
    successMessageDiv.style.display = "none";
}

form.addEventListener("submit", handleFormSubmission);

/*
Steps to upload a file
1) We need to grab the file that we want to upload
2) Upload the file
3) Check the server response if it's success show a success message
4) Check the server response if its a failed response, show an error message
*/

function handleFormSubmission(event) {
    event.preventDefault();
    hideMessages()

    const input = document.querySelector('input[type="file"]');
    const file = input.files[0];

    const formData = new FormData();
    formData.append("my_file", file);

    const xhr = new XMLHttpRequest();

    xhr.onload = function () {
        const response = JSON.parse(xhr.response);
        if ("error" in response) {
            showErrorMessage(response.error)
        }
        else if("success" in response) {
            const msg = `Your file has been successfully uploaded, you can view it here <a href='${response.file_path}' target='_blank'>Here</a>`
            showSuccessMessage(msg)
        } else {
            showErrorMessage("Unknown server response")
        }
    };

    xhr.open("POST", "/upload");
    xhr.send(formData);
}
