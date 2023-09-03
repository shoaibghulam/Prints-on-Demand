$(document).ready(function () {
  let isFormSubmitting = false; // Flag to track if the form is already submitting

  $("form").submit(function (e) {
    // Reset any previous error messages
    $(".error-message").remove();

    // Validation logic here
    const firstName = $("#fname").val().trim();
    const lastName = $("#lname").val().trim();
    const email = $("#email").val().trim();
    const password = $("#password").val().trim();
    const confirmPassword = $("#cpassword").val().trim();

    let hasError = false; // Track if there are validation errors

    // Validate first name
    if (firstName === "") {
      e.preventDefault(); // Prevent form submission
      $("#fname").after('<p class="tw-text-sm tw-text-primary">First Name is required.</p>');
      hasError = true;
    } else if (!isValidName(firstName)) {
      e.preventDefault(); // Prevent form submission
      $("#fname").after('<p class="tw-text-sm tw-text-primary">First Name should contain only letters.</p>');
      hasError = true;
    }

    // Validate last name
    if (lastName === "") {
      e.preventDefault(); // Prevent form submission
      $("#lname").after('<p class="tw-text-sm tw-text-primary">Last Name is required.</p>');
      hasError = true;
    } else if (!isValidName(lastName)) {
      e.preventDefault(); // Prevent form submission
      $("#lname").after('<p class="tw-text-sm tw-text-primary">Last Name should contain only letters.</p>');
      hasError = true;
    }

    // Validate email
    if (email === "") {
      e.preventDefault(); // Prevent form submission
      $("#email").after('<p class="tw-text-sm tw-text-primary">Email is required.</p>');
      hasError = true;
    } else if (!isValidEmail(email)) {
      e.preventDefault(); // Prevent form submission
      $("#email").after('<p class="tw-text-sm tw-text-primary">Invalid email format.</p>');
      hasError = true;
    }

    // Validate password strength
    if (password === "") {
      e.preventDefault(); // Prevent form submission
      $("#password").after('<p class="tw-text-sm tw-text-primary">Password is required.</p>');
      hasError = true;
    } else if (!isStrongPassword(password)) {
      e.preventDefault(); // Prevent form submission
      $("#password").after('<p class="tw-text-sm tw-text-primary">Password must be strong (min. 8 characters, at least one uppercase letter, one lowercase letter, one number, and one special character).</p>');
      hasError = true;
    }

    // Validate confirm password only if both password fields are not empty
    if (password !== "" && confirmPassword !== "") {
      if (confirmPassword !== password) {
        e.preventDefault(); // Prevent form submission
        $("#cpassword").after('<p class="tw-text-sm tw-text-primary">Passwords do not match.</p>');
        hasError = true;
      }
    }

    // If there are no validation errors, allow form submission
    if (!hasError) {
      isFormSubmitting = true; // Set the flag to indicate that the form is submitting
    }
  });

  // Function to validate email format
  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  // Function to validate names (alphabetic characters only)
  function isValidName(name) {
    const nameRegex = /^[A-Za-z]+$/;
    return nameRegex.test(name);
  }

  // Function to check password strength
  function isStrongPassword(password) {
    // Password must be at least 8 characters long and contain
    // at least one uppercase letter, one lowercase letter,
    // one number, and one special character
    const passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordRegex.test(password);
  }
});
