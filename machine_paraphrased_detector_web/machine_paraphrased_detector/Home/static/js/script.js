document.addEventListener('DOMContentLoaded', function() {
    let triggerButton = document.getElementById('check_button');
    let modal = document.getElementById('exampleModalCenter');

    // Add event listener to the check button
    triggerButton.addEventListener('click', function() {
        let hideInterval = setTimeout(function() {
            modal.style.display = 'none'; // Hide the modal
        }, 3000);

        // Store the timeout ID in a data attribute
        modal.dataset.hideInterval = hideInterval;
});