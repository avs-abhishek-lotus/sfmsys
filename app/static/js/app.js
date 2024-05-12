// static/js/app.js

document.addEventListener("DOMContentLoaded", function() {
    // Example: AJAX Form Submission
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the form from submitting through the browser

            const formData = new FormData(this);
            fetch(this.action, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                alert('Form submitted successfully!');
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('Error submitting form!');
            });
        });
    });

    // Example: Dynamic content loading
    const loadContentButton = document.getElementById('load-content');
    if (loadContentButton) {
        loadContentButton.addEventListener('click', function() {
            fetch('/some-endpoint') // Your API endpoint
            .then(response => response.json())
            .then(data => {
                document.getElementById('content').innerHTML = data.message;
            })
            .catch(error => console.error('Error loading the content:', error));
        });
    }

    // Simple client-side validation
    const numberInputs = document.querySelectorAll('input[type="number"]');
    numberInputs.forEach(input => {
        input.addEventListener('change', function() {
            if (this.value < 0) {
                alert('Negative values are not allowed');
                this.value = '';
            }
        });
    });
});

