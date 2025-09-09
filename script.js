// Wait for DOM to load
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form");
  const nameInput = document.getElementById("name");
  const emailInput = document.getElementById("email");
  const attendanceSelect = document.getElementById("attendance");
  const guestList = document.getElementById("guest-list");

  // Extra feature: live RSVP count
  const responsesSection = document.getElementById("responses");
  const countDisplay = document.createElement("p");
  let guestCount = 0;
  responsesSection.insertBefore(countDisplay, guestList);
  updateCount();

  // Custom validation function
  function validateForm() {
    let valid = true;
    let errors = [];

    // Check name
    if (nameInput.value.trim() === "") {
      valid = false;
      errors.push("Name is required.");
    }

    // Check email format
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (emailInput.value.trim() === "") {
      valid = false;
      errors.push("Email is required.");
    } else if (!emailInput.value.match(emailPattern)) {
      valid = false;
      errors.push("Please enter a valid email address.");
    }

    // Check attendance
    if (attendanceSelect.value === "") {
      valid = false;
      errors.push("Please select your attendance option.");
    }

    // Show errors if any
    const existingErrors = document.querySelectorAll(".error-message");
    existingErrors.forEach(err => err.remove());

    if (!valid) {
      errors.forEach(msg => {
        const error = document.createElement("p");
        error.classList.add("error-message");
        error.style.color = "red";
        error.textContent = msg;
        form.appendChild(error);
      });
    }

    return valid;
  }

  // Update RSVP count
  function updateCount() {
    countDisplay.textContent = `Total RSVPs: ${guestCount}`;
  }

  // Handle form submit
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    if (validateForm()) {
      // Create a new list item for the guest
      const li = document.createElement("li");
      li.textContent = `${nameInput.value} (${attendanceSelect.value})`;

      // Add delete button
      const deleteBtn = document.createElement("button");
      deleteBtn.textContent = "Remove";
      deleteBtn.style.marginLeft = "10px";
      deleteBtn.addEventListener("click", () => {
        guestList.removeChild(li);
        guestCount--;
        updateCount();
      });

      li.appendChild(deleteBtn);
      guestList.appendChild(li);

      // Update count
      guestCount++;
      updateCount();

      // Clear form
      form.reset();
    }
  });
});
