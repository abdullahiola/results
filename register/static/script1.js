// script.js

function checkResult() {
    const examNumberInput = document.getElementById('examNumber');
    const examYearInput = document.getElementById('examYear');
    const alertContainer = document.getElementById('alert');

    // Check if both fields are filled
    if (examNumberInput.value.trim() === '' || examYearInput.value.trim() === '') {
        // Display the alert if fields are not filled
        alertContainer.style.display = 'block';
        return; // Exit the function if fields are not filled
    }

    // Reset the alert if fields are filled
    alertContainer.style.display = 'none';

    // Continue with result checking logic...
    // (your existing code for fetching and displaying results)
    
    // For the sake of the example, let's display a dummy result
    displayResult({
        examNumber: examNumberInput.value.trim(),
        examYear: examYearInput.value.trim(),
        grade: 'A',
    });
}

function displayResult(data) {
    const resultContainer = document.getElementById('resultContainer');
    const resultElement = document.getElementById('result');

    // Update the UI with the result details
    resultElement.innerHTML = `
        <p><strong>Exam Number:</strong> ${data.examNumber}</p>
        <p><strong>Exam Year:</strong> ${data.examYear}</p>
        <p><strong>Grade:</strong> ${data.grade}</p>
    `;

    // Display the result container
    resultContainer.style.display = 'block';
}
