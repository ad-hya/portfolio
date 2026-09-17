// Highlight the current page's nav link
document.addEventListener("DOMContentLoaded", function () {
  var currentPage = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".navbar-nav .nav-link").forEach(function (link) {
    var linkPage = link.getAttribute("href");
    if (linkPage === currentPage) {
      link.classList.add("active");
    }
  });

  // Demo contact form: this site is static (no backend), so we just
  // validate and show a success message instead of submitting anywhere.
  var contactForm = document.getElementById("contactForm");
  if (contactForm) {
    contactForm.addEventListener("submit", function (event) {
      event.preventDefault();
      event.stopPropagation();

      if (!contactForm.checkValidity()) {
        contactForm.classList.add("was-validated");
        return;
      }

      contactForm.classList.add("was-validated");
      var successAlert = document.getElementById("formSuccessAlert");
      successAlert.classList.remove("d-none");
      contactForm.reset();
      contactForm.classList.remove("was-validated");

      setTimeout(function () {
        successAlert.classList.add("d-none");
      }, 5000);
    });
  }
});
