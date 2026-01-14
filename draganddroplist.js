/**
 * Adds drag and drop functionality to elements.
 * Apply the 'draggable' class to items and 'container' to the parent.
 */
function setupDragAndDrop() {
    const draggables = document.querySelectorAll('.draggable');
    const containers = document.querySelectorAll('.container');

    draggables.forEach(draggable => {
        // Event fired when the user starts dragging
        draggable.addEventListener('dragstart', () => {
            draggable.classList.add('dragging');
        });

        // Event fired when the user releases the item
        draggable.addEventListener('dragend', () => {
            draggable.classList.remove('dragging');
        });
    });

    containers.forEach(container => {
        container.addEventListener('dragover', e => {
            e.preventDefault(); // Required to allow the drop action
            const dragging = document.querySelector('.dragging');
            container.appendChild(dragging); // Moves the element to the new container
        });
    });
}
